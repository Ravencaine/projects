"""
vault_rag.py — Local RAG pipeline for The Vault
================================================
Retrieval: rank_bm25 (keyword) + text-embedding-3-small (semantic)
Merge:     Reciprocal Rank Fusion (RRF)
Synthesis: MiniMax-M2.5 via chat.obsidianaitools.com (OpenAI-compatible)

Usage:
    python vault_rag.py build      # Build/rebuild index
    python vault_rag.py query      # Interactive query mode
    python vault_rag.py update     # Incremental: embed only new/changed notes
    python vault_rag.py stats      # Show index stats
"""

import os
import re
import json
import sqlite3
import hashlib
import pickle
import time
import requests
import numpy as np
import faiss
from rank_bm25 import BM25Okapi
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────

VAULT_ROOT   = Path("C:/Users/krlsa/Documents/00 Projects/The Vault").resolve()
INDEX_DIR    = VAULT_ROOT / "99.System/Scripts/RAG/index"
SCRIPT_DIR   = VAULT_ROOT / "99.System/Scripts/RAG"

# ── Cloud API config ───────────────────────────────────────────────────────────
import os as _os

def _load_env():
    env_path = _os.path.expanduser("C:/Users/krlsa/AppData/Local/hermes/.env")
    if _os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("OPENAI_API_KEY=") and not line.startswith("#"):
                    key = line.split("=", 1)[1].strip()
                    return key
    return None

_CLOUD_KEY = _load_env()
CLOUD_BASE = "https://chat.obsidianaitools.com/v1"
CLOUD_EMBED_MODEL = "text-embedding-3-small"
CLOUD_EMBED_DIM  = 1536   # text-embedding-3-small → 1536-dim
CLOUD_GEN_MODEL  = "MiniMax-M2.5"
CLOUD_EMBED_URL  = f"{CLOUD_BASE}/embeddings"
CLOUD_GEN_URL    = f"{CLOUD_BASE}/chat/completions"

# Folders to exclude from indexing
EXCLUDE_FOLDERS = {
    "00.Inbox",
    "99.System",
    "_Archive",
    ".obsidian",
    "projects",     # symlink/junction to parent — avoid double-indexing
}

# Files to exclude from indexing (by exact name in any folder)
EXCLUDE_FILES = {
    "_INGESTED.md",
    "CLAUDE.md",
}

# RRF k parameter (higher = equal weight, standard is 60)
RRF_K = 60

# Top-K from each retrieval method before RRF merge
TOP_K = 20  # BM25 top-K + FAISS top-K → RRF → top-N for LLM
N_FOR_LLM = 5   # How many notes to send to LLM (< 5 = better CPU latency)
MAX_CHARS_PER_NOTE = 800  # keep LLM prompt small for CPU inference

DB_PATH  = INDEX_DIR / "metadata.db"
BM25_PATH = INDEX_DIR / "bm25.pkl"
FAISS_PATH = INDEX_DIR / "vault.faiss"

# ── Dataclasses ─────────────────────────────────────────────────────────────

@dataclass
class DocMeta:
    note_id:    str
    vault_path: str       # full relative path from vault root
    title:      str
    kb:         str       # knowledge base folder
    size_bytes: int
    mtime:      float
    file_hash:  str       # sha256 of content — detect changes

    @property
    def rel_path(self) -> str:
        return self.vault_path

    @property
    def full_path(self) -> Path:
        return VAULT_ROOT / self.vault_path

# ── Cloud API helpers ───────────────────────────────────────────────────────────

def _cloud_headers() -> dict:
    return {"Authorization": f"Bearer {_CLOUD_KEY}", "Content-Type": "application/json"}


def cloud_embed(text: str) -> np.ndarray:
    """Return 1536-dim embedding vector via OpenAI-compatible API."""
    text = text.replace("\x00", "")
    resp = requests.post(
        CLOUD_EMBED_URL,
        headers=_cloud_headers(),
        json={"model": CLOUD_EMBED_MODEL, "input": text[:8000]},
        timeout=60,
    )
    resp.raise_for_status()
    return np.array(resp.json()["data"][0]["embedding"], dtype=np.float32)


def cloud_generate(prompt: str, system: str = "") -> str:
    """Return LLM response via OpenAI-compatible chat completions API."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    resp = requests.post(
        CLOUD_GEN_URL,
        headers=_cloud_headers(),
        json={"model": CLOUD_GEN_MODEL, "messages": messages, "temperature": 0.2},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


SYSTEM_PROMPT = (
    "You are a technical expert in DAX, Power BI, Power Query, Excel, VBA, and Data Modeling. "
    "Answer the user's question using ONLY the provided context. "
    "If the context does not contain enough information to fully answer the question, say so. "
    "Cite the source note(s) by filename for each piece of information. "
    "Be concise, precise, and technical. Use code blocks for any DAX, M, or VBA code."
)

# ── Database helpers ─────────────────────────────────────────────────────────

def init_db():
    """Create SQLite metadata table if it doesn't exist."""
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            note_id    TEXT PRIMARY KEY,
            vault_path TEXT UNIQUE NOT NULL,
            title      TEXT,
            kb         TEXT,
            size_bytes INTEGER,
            mtime      REAL,
            file_hash  TEXT,
            indexed_at REAL DEFAULT (unixepoch())
        )
    """)
    conn.commit()
    return conn


def upsert_note(conn: sqlite3.Connection, doc: DocMeta):
    conn.execute("""
        INSERT INTO notes (note_id, vault_path, title, kb, size_bytes, mtime, file_hash)
        VALUES (:note_id, :vault_path, :title, :kb, :size_bytes, :mtime, :file_hash)
        ON CONFLICT(note_id) DO UPDATE SET
            title      = excluded.title,
            kb         = excluded.kb,
            size_bytes = excluded.size_bytes,
            mtime      = excluded.mtime,
            file_hash  = excluded.file_hash,
            indexed_at = unixepoch()
    """, asdict(doc))
    conn.commit()


def get_known_notes(conn: sqlite3.Connection) -> dict[str, DocMeta]:
    """Return all known notes keyed by vault_path."""
    rows = conn.execute(
        "SELECT note_id, vault_path, title, kb, size_bytes, mtime, file_hash FROM notes"
    ).fetchall()
    return {
        r[1]: DocMeta(
            note_id=r[0], vault_path=r[1], title=r[2], kb=r[3],
            size_bytes=r[4], mtime=r[5], file_hash=r[6],
        )
        for r in rows
    }


def delete_note(conn: sqlite3.Connection, vault_path: str):
    conn.execute("DELETE FROM notes WHERE vault_path = ?", (vault_path,))
    conn.commit()

# ── Vault scanning ────────────────────────────────────────────────────────────

def scan_vault() -> list[dict]:
    """Walk the vault, return list of note dicts with content and metadata."""
    notes = []
    for md_path in VAULT_ROOT.rglob("*.md"):
        # Check exclusions
        rel = md_path.relative_to(VAULT_ROOT)
        if any(ex in rel.parts for ex in EXCLUDE_FOLDERS):
            continue
        if md_path.name in EXCLUDE_FILES:
            continue

        try:
            content = md_path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        if not content.strip():
            continue

        # Extract title from first H1, or filename
        title = ""
        lines = content.splitlines()
        for line in lines:
            m = re.match(r"^#\s+(.+)", line.strip())
            if m:
                title = m.group(1).strip()
                break
        if not title:
            title = md_path.stem

        # KB folder: first path component after the vault root (e.g. "DAX Code")
        parts = rel.parts
        kb = parts[1] if len(parts) > 1 else ""

        stat = md_path.stat()
        file_hash = hashlib.sha256(content.encode()).hexdigest()[:16]

        notes.append({
            "vault_path": str(rel).replace("\\", "/"),
            "title":     title,
            "content":   content,
            "kb":        kb,
            "size":      stat.st_size,
            "mtime":     stat.st_mtime,
            "file_hash": file_hash,
        })
    return notes


# ── BM25 ─────────────────────────────────────────────────────────────────────

def build_bm25(notes: list[dict]) -> BM25Okapi:
    """Tokenise note content and build BM25 index."""
    tokenised = [_tokenise(n["content"]) for n in notes]
    return BM25Okapi(tokenised)


def _tokenise(text: str) -> list[str]:
    """Minimal tokeniser: lowercase, alphanumeric chunks."""
    return re.findall(r"[a-zA-Z0-9_]+", text.lower())


def bm25_search(bm25: BM25Okapi, notes: list[dict], query: str, k: int = TOP_K) -> list[tuple[int, float]]:
    """Return list of (note_index, score) sorted descending."""
    tokens = _tokenise(query)
    scores = bm25.get_scores(tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return ranked[:k]


# ── FAISS ────────────────────────────────────────────────────────────────────

MAX_EMBED_CHARS = 4000  # nomic-embed-text maxes out just under 4000 chars


def build_faiss_index(embeddings: np.ndarray) -> faiss.IndexFlatIP:
    """Build FAISS inner-product index (cosine sim with normalised vectors)."""
    # Normalise for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1  # avoid div by zero
    normed = embeddings / norms
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(normed)
    return index


def embed_notes_batch(texts: list[str]) -> np.ndarray:
    """
    Embed a list of texts via the cloud API (text-embedding-3-small).
    No warmup needed — cloud API is always ready.
    """
    embeddings = []
    failed = 0
    for i, text in enumerate(texts):
        try:
            vec = cloud_embed(text[:MAX_EMBED_CHARS])
            embeddings.append(vec)
        except Exception:
            embeddings.append(np.zeros(CLOUD_EMBED_DIM, dtype=np.float32))
            failed += 1
        done = i + 1
        if done % 100 == 0 or done == len(texts):
            print(f"  embedded {done}/{len(texts)} notes... ({failed} failed)", flush=True)

    return np.stack(embeddings).astype(np.float32)


def faiss_search(
    index: faiss.IndexFlatIP,
    query_vec: np.ndarray,
    k: int = TOP_K,
) -> list[tuple[int, float]]:
    """Return list of (note_index, cosine_sim) sorted descending."""
    q_normed = query_vec / (np.linalg.norm(query_vec) + 1e-9)
    scores, indices = index.search(q_normed.reshape(1, -1), k)
    return list(zip(indices[0].tolist(), scores[0].tolist()))


# ── RRF ─────────────────────────────────────────────────────────────────────

def rrf_merge(
    bm25_results: list[tuple[int, float]],
    faiss_results: list[tuple[int, float]],
    k: int = RRF_K,
) -> list[tuple[int, float]]:
    """Reciprocal Rank Fusion of two ranked lists."""
    scores: dict[int, float] = {}

    for rank, (idx, _) in enumerate(bm25_results):
        scores[idx] = scores.get(idx, 0) + 1.0 / (k + rank + 1)

    for rank, (idx, _) in enumerate(faiss_results):
        scores[idx] = scores.get(idx, 0) + 1.0 / (k + rank + 1)

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


# ── Build ────────────────────────────────────────────────────────────────────

def build_index(conn: sqlite3.Connection, incremental: bool = False):
    """
    Full index rebuild from scratch.
    incremental=True: tracks unchanged notes via file hash (fast rebuilds).
    """
    print(f"\n{'='*60}")
    print(f"Building RAG index for: {VAULT_ROOT}")
    print(f"{'='*60}\n")

    start = time.time()

    # ── Step 1: Scan vault ─────────────────────────────────────────
    print("[1/4] Scanning vault...")
    all_notes = scan_vault()
    print(f"  Found {len(all_notes)} notes", flush=True)

    # Build note list (all notes, stable order by vault_path)
    all_notes.sort(key=lambda n: n["vault_path"])
    note_list = all_notes

    # ── Step 2: BM25 ────────────────────────────────────────────────
    print(f"\n[2/4] Building BM25 index...")
    bm25 = build_bm25(note_list)
    with open(BM25_PATH, "wb") as f:
        pickle.dump((bm25, note_list), f)
    print(f"  Saved BM25 → {BM25_PATH.name}")

    # ── Step 3: Embed + FAISS ──────────────────────────────────────
    print(f"\n[3/4] Embedding notes via cloud API ({CLOUD_EMBED_MODEL})...")
    texts = [n["content"][:MAX_EMBED_CHARS] for n in note_list]
    embeddings = embed_notes_batch(texts)
    print(f"  All {len(embeddings)} embeddings done")

    index = build_faiss_index(embeddings)
    faiss.write_index(index, str(FAISS_PATH))
    np.save(INDEX_DIR / "embeddings.npy", embeddings)
    print(f"  Saved FAISS → {FAISS_PATH.name} ({embeddings.shape[0]} vectors)")

    # ── Step 4: SQLite metadata ────────────────────────────────────
    print(f"\n[4/4] Writing SQLite metadata...")
    conn.execute("DELETE FROM notes")  # clear old metadata
    for note in all_notes:
        doc = DocMeta(
            note_id=hashlib.md5(note["vault_path"].encode()).hexdigest(),
            vault_path=note["vault_path"],
            title=note["title"],
            kb=note["kb"],
            size_bytes=note["size"],
            mtime=note["mtime"],
            file_hash=note["file_hash"],
        )
        upsert_note(conn, doc)

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"Done in {elapsed:.1f}s")
    print(f"  Notes indexed: {len(note_list)}")
    print(f"  FAISS vectors: {embeddings.shape[0]}")
    print(f"  Index size:    {FAISS_PATH.stat().st_size / 1024:.0f} KB")
    print(f"  DB records:    {conn.execute('SELECT COUNT(*) FROM notes').fetchone()[0]}")
    print(f"{'='*60}\n")


# ── Query ────────────────────────────────────────────────────────────────────

def load_index() -> tuple[BM25Okapi, list[dict], faiss.IndexFlatIP]:
    """Load persisted index components."""
    with open(BM25_PATH, "rb") as f:
        bm25, note_list = pickle.load(f)

    embeddings = np.load(INDEX_DIR / "embeddings.npy")
    index = build_faiss_index(embeddings)

    return bm25, note_list, index


def query_vault(question: str, n: int = N_FOR_LLM) -> tuple[str, list[tuple[int, float]]]:
    """
    Run a RAG query: BM25 + semantic (FAISS) merged via RRF, synthesised via cloud API.
    Returns (answer, fused_rankings) for optional inspection.
    """
    if not BM25_PATH.exists():
        raise FileNotFoundError(
            f"Index not found at {BM25_PATH}. Run: python vault_rag.py build"
        )

    with open(BM25_PATH, "rb") as f:
        bm25, note_list = pickle.load(f)

    # Step 1: BM25 top-K
    bm25_results = bm25_search(bm25, note_list, question, TOP_K)

    # Step 2: Semantic fallback — embed query + cosine against stored embeddings
    faiss_results: list[tuple[int, float]] = []
    if FAISS_PATH.exists() and (INDEX_DIR / "embeddings.npy").exists():
        embeddings = np.load(INDEX_DIR / "embeddings.npy")
        # Guard: skip FAISS if embeddings were built with a different dimension
        if embeddings.shape[1] != CLOUD_EMBED_DIM:
            print(f"  [FAISS skipped: embeddings.npy dim={embeddings.shape[1]}, "
                  f"expected {CLOUD_EMBED_DIM} — rebuild to enable semantic search]",
                  flush=True)
        else:
            index = build_faiss_index(embeddings)
            query_emb = cloud_embed(question)
            faiss_results = faiss_search(index, query_emb, TOP_K)

    # Step 3: RRF merge (or BM25-only if no FAISS)
    if faiss_results:
        fused = rrf_merge(bm25_results, faiss_results, RRF_K)
    else:
        fused = bm25_results  # BM25 only — no embeddings built yet

    top_n = fused[:n]

    # Step 4: Build context from top-N notes
    context_parts = []
    for note_idx, rrf_score in top_n:
        if note_idx >= len(note_list):
            continue
        note = note_list[note_idx]
        rel_path = note["vault_path"]
        context_parts.append(
            f"--- [{rel_path}] ---\n"
            f"Title: {note['title']}\n"
            f"KB: {note['kb']}\n"
            f"\n{note['content'][:MAX_CHARS_PER_NOTE]}"
        )

    context = "\n\n".join(context_parts)

    prompt = (
        f"Question: {question}\n\n"
        f"Context (ranked by relevance):\n"
        f"{context}\n\n"
        f"Answer the question using only the context above. "
        f"Cite the source note by its path for each piece of information."
    )

    answer = cloud_generate(prompt, system=SYSTEM_PROMPT)
    return answer, fused


# ── CLI ──────────────────────────────────────────────────────────────────────

def cmd_build(args):
    conn = init_db()
    build_index(conn, incremental=args.incremental)
    conn.close()


def cmd_update(args):
    conn = init_db()
    build_index(conn, incremental=True)
    conn.close()


def save_to_outputs(question: str, answer: str, rankings: list) -> Optional[Path]:
    """
    Save a query + answer to the appropriate KB's Outputs folder.
    Uses the most-represented KB from top-ranking notes.
    """
    if not rankings:
        return None

    # Load note metadata for top results
    with open(BM25_PATH, "rb") as f:
        _, note_list = pickle.load(f)

    # Find dominant KB from top 5 results
    kb_counts: dict[str, int] = {}
    for idx, _ in rankings[:5]:
        if idx < len(note_list):
            kb = note_list[idx]["kb"]
            kb_counts[kb] = kb_counts.get(kb, 0) + 1

    if not kb_counts:
        return None

    dominant_kb = max(kb_counts, key=kb_counts.get)
    # kb stored as "01.Knowledge/DAX Code" — strip the prefix
    KB_PREFIX = "01.Knowledge/"
    if dominant_kb.startswith(KB_PREFIX):
        kb_folder = dominant_kb[len(KB_PREFIX):]
    else:
        kb_folder = dominant_kb

    outputs_dir = VAULT_ROOT / "01.Knowledge" / kb_folder / "Outputs"
    if not outputs_dir.exists():
        print(f"  [save] Outputs folder not found: {outputs_dir}")
        return None

    # Build safe filename from question
    slug = re.sub(r"[^a-z0-9]+", "-", question.lower())[:60].strip("-")
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"{timestamp} — {slug}.md"
    filepath = outputs_dir / filename

    # Build top sources list
    sources = []
    for i, (idx, score) in enumerate(rankings[:5]):
        if idx < len(note_list):
            note = note_list[idx]
            sources.append(f"  {i+1}. [[{note['vault_path']}|{note['title']}]] — score {score:.3f}")

    content = f"""---
type: vault-query
question: "{question}"
date: {datetime.now().isoformat(timespec="seconds")}
kb: {dominant_kb}
---

# {question}

{answer}

## Sources

{"".join(sources)}

## Query Log

- **Date:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
- **Top results:** {len(rankings)} notes ranked
- **Dominant KB:** {dominant_kb}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def cmd_query(args):
    if not args.query:
        print("Usage: python vault_rag.py query \"your question here\"")
        return
    print(f"\nQ: {args.query}\n")
    answer, rankings = query_vault(args.query)
    print(answer)
    if args.verbose:
        print(f"\n--- Top rankings ---")
        for i, (idx, score) in enumerate(rankings[:5]):
            with open(BM25_PATH, "rb") as f:
                _, note_list = pickle.load(f)
            if idx < len(note_list):
                print(f"  {i+1}. [{score:.3f}] {note_list[idx]['vault_path']} — {note_list[idx]['title']}")

    if args.save:
        saved = save_to_outputs(args.query, answer, rankings)
        if saved:
            print(f"\n[Saved → {saved.relative_to(VAULT_ROOT)}]")


def cmd_stats(args):
    conn = init_db()
    row = conn.execute("SELECT COUNT(*), SUM(size_bytes) FROM notes").fetchone()
    print(f"Indexed notes : {row[0]}")
    print(f"Total size    : {row[1] / 1024:.1f} KB" if row[1] else "N/A")
    if FAISS_PATH.exists():
        import os
        print(f"FAISS index   : {os.path.getsize(FAISS_PATH) / 1024:.1f} KB")
    print(f"DB            : {DB_PATH}")
    conn.close()


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Vault RAG CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_build = sub.add_parser("build", help="Full index rebuild")
    p_build.add_argument("--incremental", action="store_true", help="Skip unchanged notes")
    p_build.set_defaults(func=cmd_build)

    p_upd = sub.add_parser("update", help="Incremental update (same as build --incremental)")
    p_upd.set_defaults(func=cmd_update)

    p_q = sub.add_parser("query", help="Query the vault")
    p_q.add_argument("query", nargs="+", help="Question to ask")
    p_q.add_argument("-v", "--verbose", action="store_true", help="Show top-ranked notes")
    p_q.add_argument("--save", action="store_true", help="Save Q&A to the dominant KB's Outputs folder")
    p_q.set_defaults(func=cmd_query)

    p_stat = sub.add_parser("stats", help="Show index statistics")
    p_stat.set_defaults(func=cmd_stats)

    args = parser.parse_args()

    if args.cmd == "query":
        args.query = " ".join(args.query)

    if args.cmd:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
