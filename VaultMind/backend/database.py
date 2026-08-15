"""SQLite + FTS5 schema, connection management, and DB helpers.

Centralises every SQL string and connection-handling concern so the rest of the
codebase doesn't touch sqlite3 directly. The external-content FTS5 pattern with
mandatory sync triggers is documented at:
https://www.sqlite.org/fts5.html#external_content_tables

Schema overview:
    sources       one row per ingested file/URL
    chunks        one row per text chunk
    chunks_fts    external-content FTS5 index over chunks.text
                  (porter unicode61 + prefix='2 3')
    messages      chat history

The triggers `chunks_ai/ad/au` are mandatory for external-content FTS5:
without them the index drifts from the content table and queries return
silently-wrong results.
"""

from __future__ import annotations

import contextlib
import json
import sqlite3
import threading
import uuid
from collections.abc import Generator
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

# SQL constants. Keep every statement here so the schema is auditable in one
# place and the triggers cannot drift from the FTS5 declaration.

# `prefix='2 3'` enables partial-term matching: a search for `confi*` will
# match `configuration` and `configured`. Cost: FTS5 index roughly doubles.
# Worth it for the recall gain.
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS sources (
    id           TEXT PRIMARY KEY,
    name         TEXT NOT NULL,
    type         TEXT NOT NULL,
    path         TEXT,
    url          TEXT,
    hash         TEXT UNIQUE NOT NULL,
    chunk_count  INTEGER NOT NULL DEFAULT 0,
    token_count  INTEGER NOT NULL DEFAULT 0,
    created_at   TEXT NOT NULL,
    metadata     TEXT
);

CREATE TABLE IF NOT EXISTS chunks (
    id           TEXT PRIMARY KEY,
    source_id    TEXT NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    chunk_index  INTEGER NOT NULL,
    page_start   INTEGER,
    page_end     INTEGER,
    text         TEXT NOT NULL,
    token_count  INTEGER,
    char_count   INTEGER,
    created_at   TEXT NOT NULL,
    UNIQUE(source_id, chunk_index)
);
CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source_id);
CREATE INDEX IF NOT EXISTS idx_chunks_token_count ON chunks(token_count);

-- External-content FTS5. The content table is `chunks` and `text` is the
-- single indexed column. `rowid` aligns 1:1 with the content table's rowid.
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    text,
    content='chunks',
    content_rowid='rowid',
    tokenize='porter unicode61',
    prefix='2 3'
);

-- Mandatory sync triggers. Without these the FTS5 index drifts from the
-- content table on every UPDATE, producing silently-wrong query results.
CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
    INSERT INTO chunks_fts(rowid, text) VALUES (new.rowid, new.text);
END;
CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
    INSERT INTO chunks_fts(chunks_fts, rowid, text) VALUES ('delete', old.rowid, old.text);
END;
CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
    INSERT INTO chunks_fts(chunks_fts, rowid, text) VALUES ('delete', old.rowid, old.text);
    INSERT INTO chunks_fts(rowid, text) VALUES (new.rowid, new.text);
END;

CREATE TABLE IF NOT EXISTS messages (
    id            TEXT PRIMARY KEY,
    role          TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
    content       TEXT NOT NULL,
    query_params  TEXT,
    created_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_messages_created ON messages(created_at);
"""

PRAGMA_SQL = """
PRAGMA journal_mode = WAL;
PRAGMA synchronous  = NORMAL;
PRAGMA foreign_keys = ON;
"""


# ============================================================================ #
# Connection management
# ============================================================================ #

_local = threading.local()


def get_connection(db_path: Path | str) -> sqlite3.Connection:
    """Return a thread-local SQLite connection.

    One connection per thread (sqlite3 connections are not shareable across
    threads in Python). Caller is responsible for closing via `close_connection`
    or via the `connection()` context manager.
    """
    key = str(db_path)
    conn = getattr(_local, "connections", {}).get(key)
    if conn is None:
        conn = sqlite3.connect(key, check_same_thread=False, isolation_level=None)
        conn.row_factory = sqlite3.Row
        conn.executescript(PRAGMA_SQL)
        # executescript() handles multi-statement scripts (including CREATE
        # TRIGGER ... BEGIN ... END;) correctly. Splitting on ';' breaks
        # trigger bodies, which is why the schema install was failing with
        # "incomplete input" before this fix.
        conn.executescript(SCHEMA_SQL)
        _local.connections = getattr(_local, "connections", {})
        _local.connections[key] = conn
    return conn


def close_connection(db_path: Path | str) -> None:
    """Close the thread-local connection for this db_path, if any."""
    key = str(db_path)
    conn = getattr(_local, "connections", {}).pop(key, None)
    if conn is not None:
        conn.close()


@contextlib.contextmanager
def connection(db_path: Path | str) -> Generator[sqlite3.Connection, None, None]:
    """Context manager that yields a (thread-local) connection.

    Does NOT close the connection on exit (the connection is cached per-thread).
    Use this for explicit transaction control; for read-only callers prefer
    `get_connection` directly.
    """
    conn = get_connection(db_path)
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise


def init_db(db_path: Path | str) -> None:
    """Open the database, install pragmas, and create schema if missing.

    Idempotent — safe to call on every startup.
    """
    p = Path(db_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = get_connection(p)
    # Verify FTS5 integrity at boot. SQLite returns ok on a well-formed index.
    conn.execute("INSERT INTO chunks_fts(chunks_fts) VALUES ('integrity-check')")


# ============================================================================ #
# ID + timestamp helpers
# ============================================================================ #


def new_id() -> str:
    """UUID4 string. Used for source, chunk, message, and job IDs."""
    return str(uuid.uuid4())


def utc_now_iso() -> str:
    """ISO-8601 UTC timestamp with 'Z' suffix."""
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def utc_now() -> datetime:
    """Timezone-aware UTC datetime."""
    return datetime.now(UTC)


# ============================================================================ #
# Source CRUD
# ============================================================================ #


def insert_source(
    db_path: Path | str,
    *,
    name: str,
    type_: str,
    hash_: str,
    path: str | None = None,
    url: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> str:
    """Insert a new source. Returns the source ID."""
    sid = new_id()
    with connection(db_path) as conn:
        conn.execute(
            """
            INSERT INTO sources (id, name, type, path, url, hash, created_at, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                sid,
                name,
                type_,
                path,
                url,
                hash_,
                utc_now_iso(),
                json.dumps(metadata) if metadata else None,
            ),
        )
    return sid


def get_source_by_hash(db_path: Path | str, hash_: str) -> dict | None:
    """Return a source row as a dict, or None if the hash is unknown."""
    with connection(db_path) as conn:
        row = conn.execute(
            "SELECT * FROM sources WHERE hash = ?", (hash_,)
        ).fetchone()
    return _row_to_source(row) if row else None


def get_source(db_path: Path | str, source_id: str) -> dict | None:
    """Return a source row as a dict, or None if the ID is unknown."""
    with connection(db_path) as conn:
        row = conn.execute("SELECT * FROM sources WHERE id = ?", (source_id,)).fetchone()
    return _row_to_source(row) if row else None


def list_sources(db_path: Path | str) -> list[dict]:
    """Return all sources, newest first."""
    with connection(db_path) as conn:
        rows = conn.execute(
            "SELECT * FROM sources ORDER BY created_at DESC"
        ).fetchall()
    return [_row_to_source(r) for r in rows if r]


def delete_source(db_path: Path | str, source_id: str) -> None:
    """Delete a source row + all its chunks (cascade). Triggers keep FTS5 in sync."""
    with connection(db_path) as conn:
        # Need CASCADE delete; ensure FK is on, then delete by source_id.
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("DELETE FROM sources WHERE id = ?", (source_id,))


# ============================================================================ #
# Chunk CRUD
# ============================================================================ #


def insert_chunks(
    db_path: Path | str,
    source_id: str,
    chunks: list[dict],
) -> None:
    """Bulk-insert chunks. Each chunk dict must have: chunk_index, text, page_start, page_end, token_count, char_count.

    FTS5 trigger `chunks_ai` keeps the index in sync per row.
    """
    if not chunks:
        return
    now = utc_now_iso()
    rows = [
        (
            new_id(),
            source_id,
            c["chunk_index"],
            c.get("page_start"),
            c.get("page_end"),
            c["text"],
            c.get("token_count"),
            c.get("char_count"),
            now,
        )
        for c in chunks
    ]
    with connection(db_path) as conn:
        conn.executemany(
            """
            INSERT INTO chunks (
                id, source_id, chunk_index, page_start, page_end,
                text, token_count, char_count, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
        # Update aggregate counts on the source row.
        conn.execute(
            """
            UPDATE sources
            SET chunk_count = (SELECT COUNT(*) FROM chunks WHERE source_id = ?),
                token_count = (SELECT COALESCE(SUM(token_count), 0) FROM chunks WHERE source_id = ?)
            WHERE id = ?
            """,
            (source_id, source_id, source_id),
        )


def fetch_chunks_for_sources(
    db_path: Path | str, source_ids: list[str]
) -> list[dict]:
    """Return ALL chunks for the given sources, ordered for natural reading."""
    if not source_ids:
        return []
    placeholders = ",".join("?" for _ in source_ids)
    query = f"""
        SELECT c.id, c.source_id, c.chunk_index, c.page_start, c.page_end,
               c.text, c.token_count, c.char_count, s.name AS source_name
        FROM chunks c
        JOIN sources s ON s.id = c.source_id
        WHERE c.source_id IN ({placeholders})
        ORDER BY c.source_id, c.chunk_index
    """
    with connection(db_path) as conn:
        rows = conn.execute(query, source_ids).fetchall()
    return [dict(r) for r in rows]


def fetch_chunk_by_id(db_path: Path | str, chunk_id: str) -> dict | None:
    with connection(db_path) as conn:
        row = conn.execute(
            """
            SELECT c.*, s.name AS source_name
            FROM chunks c JOIN sources s ON s.id = c.source_id
            WHERE c.id = ?
            """,
            (chunk_id,),
        ).fetchone()
    return dict(row) if row else None


# ============================================================================ #
# FTS5 retrieval
# ============================================================================ #


def search_fts(
    db_path: Path | str,
    match_expr: str,
    *,
    limit: int = 500,
    include_text: bool = False,
) -> list[dict]:
    """Run an FTS5 MATCH query with BM25 ranking.

    Returns rows shaped like:
        {chunk_id, source_id, page_start, page_end, excerpt, score,
         (optional) text, source_name}

    `match_expr` must be a pre-built FTS5 MATCH expression (built by
    `backend.query._build_match`). Never concatenate user input directly —
    this function does not sanitise.

    `score` is the BM25 score; lower is better in FTS5 (rank-based).
    """
    text_select = ", c.text" if include_text else ""
    query = f"""
        SELECT
            c.id            AS chunk_id,
            c.source_id     AS source_id,
            c.page_start    AS page_start,
            c.page_end      AS page_end,
            s.name          AS source_name,
            snippet(chunks_fts, 0, '<mark>', '</mark>', '...', 24) AS excerpt,
            bm25(chunks_fts) AS score{text_select}
        FROM chunks_fts
        JOIN chunks c ON c.rowid = chunks_fts.rowid
        JOIN sources s ON s.id = c.source_id
        WHERE chunks_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """
    with connection(db_path) as conn:
        try:
            rows = conn.execute(query, (match_expr, limit)).fetchall()
        except sqlite3.OperationalError as exc:
            # Malformed MATCH expression (e.g., unbalanced quotes). Surface as
            # an empty result rather than crashing.
            if "fts5" in str(exc).lower() or "syntax" in str(exc).lower():
                return []
            raise
    return [dict(r) for r in rows]


# ============================================================================ #
# Chat history
# ============================================================================ #


def insert_message(
    db_path: Path | str,
    *,
    role: str,
    content: str,
    query_params: dict | None = None,
) -> str:
    """Insert a chat message. Returns the message ID."""
    mid = new_id()
    with connection(db_path) as conn:
        conn.execute(
            """
            INSERT INTO messages (id, role, content, query_params, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                mid,
                role,
                content,
                json.dumps(query_params) if query_params else None,
                utc_now_iso(),
            ),
        )
    return mid


def list_messages(db_path: Path | str, limit: int = 200) -> list[dict]:
    """Return chat history, newest last (so it reads chronologically)."""
    with connection(db_path) as conn:
        rows = conn.execute(
            "SELECT * FROM messages ORDER BY created_at ASC LIMIT ?", (limit,)
        ).fetchall()
    return [dict(r) for r in rows]


def clear_messages(db_path: Path | str) -> None:
    """Delete all messages."""
    with connection(db_path) as conn:
        conn.execute("DELETE FROM messages")


# ============================================================================ #
# Stats
# ============================================================================ #


def get_stats(db_path: Path | str) -> dict:
    """Return aggregate counts."""
    with connection(db_path) as conn:
        row = conn.execute(
            """
            SELECT
                (SELECT COUNT(*) FROM sources)              AS source_count,
                (SELECT COUNT(*) FROM chunks)               AS chunk_count,
                (SELECT COALESCE(SUM(token_count), 0)
                 FROM chunks)                              AS token_count
            """
        ).fetchone()
    return dict(row)


# ============================================================================ #
# Internal
# ============================================================================ #


def _row_to_source(row: sqlite3.Row) -> dict:
    d = dict(row)
    # Decode JSON metadata if present.
    if d.get("metadata"):
        try:
            d["metadata"] = json.loads(d["metadata"])
        except (json.JSONDecodeError, TypeError):
            d["metadata"] = None
    return d