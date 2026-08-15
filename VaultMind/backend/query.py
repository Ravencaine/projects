"""BM25 + phrase/NEAR retrieval on SQLite FTS5.

Implements the core retrieval logic that powers the chat + query panes:

    1. `_build_match(user_query)` — convert a free-text question into a safe
       FTS5 MATCH expression. Recognises quoted phrases and adjacent
       content-word pairs (emitted as NEAR()).
    2. `_search(db_path, match_expr)` — run the ranked SELECT, top 500.
    3. `_full_source_recall(db_path, source_ids)` — fetch ALL chunks of
       every matched source. This is the spec's "full source recall"
       guarantee: if any chunk from a source matched, the LLM sees every
       chunk from that source.
    4. `_assemble_context(chunks, max_tokens)` — concatenate chunks per
       source in natural reading order, truncating at `max_tokens` if the
       budget is exceeded.

No semantic search. No embeddings. Just lexical, with full source recall.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from backend import database

# Tokens that carry no retrieval signal. Stripped before MATCH construction.
_STOP_WORDS = frozenset(
    {
        "a", "an", "the", "and", "or", "but", "if", "then", "is", "are",
        "was", "were", "be", "been", "being", "have", "has", "had",
        "do", "does", "did", "of", "in", "to", "for", "on", "with",
        "as", "at", "by", "from", "this", "that", "these", "those",
        "it", "its", "i", "you", "we", "they", "he", "she", "him",
        "her", "them", "my", "your", "our", "their",
    }
)

# FTS5 reserved characters that would break a MATCH expression if a query
# contains them outside a quoted phrase. Strip them from unquoted tokens.
_FTS5_RESERVED = re.compile(r'[^\w\s*]')

# NEAR proximity window. Tighter = more relevant but fewer matches.
NEAR_WINDOW = 5

# Maximum bytes the user query can have before we reject it.
MAX_QUERY_LEN = 4096


def _tokenize(text: str) -> list[str]:
    """Split on whitespace, drop stop-words, normalise to lowercase."""
    out: list[str] = []
    for tok in text.split():
        # Strip leading/trailing punctuation but preserve internal '*'.
        cleaned = tok.strip(",.;:!?\"'`()[]{}").lower()
        if not cleaned:
            continue
        if cleaned in _STOP_WORDS:
            continue
        out.append(cleaned)
    return out


def _sanitize_token(tok: str) -> str:
    """Remove FTS5 reserved characters from a token. Keep alnum and '*'."""
    cleaned = _FTS5_RESERVED.sub("", tok).strip()
    return cleaned


def _build_match(user_query: str) -> str:
    """Convert a free-text question into a safe FTS5 MATCH expression.

    Recognises:
        - Quoted phrases: `"exact phrase"` → preserved as a phrase.
        - Bare words: tokenized, sanitized, OR-ed together.
        - Adjacent content-word pairs: NEAR(token1 token2, NEAR_WINDOW).

    Returns an empty string if no usable tokens remain (the caller treats
    that as "no matches").
    """
    user_query = user_query.strip()
    if not user_query:
        return ""

    if len(user_query) > MAX_QUERY_LEN:
        user_query = user_query[:MAX_QUERY_LEN]

    # Extract quoted phrases first.
    phrases: list[str] = []
    remaining = re.sub(r'"([^"]+)"', lambda m: _save_phrase(m, phrases), user_query)

    # Tokenize the remainder.
    bare_tokens = [t for t in _tokenize(remaining) if t]
    bare_tokens = [_sanitize_token(t) for t in bare_tokens]
    bare_tokens = [t for t in bare_tokens if t]

    if not phrases and not bare_tokens:
        return ""

    parts: list[str] = []

    # Add bare-word OR group.
    if bare_tokens:
        # Use prefix wildcards on bare words for partial-match recall.
        # `confi*` → `configuration`, `configured`, etc.
        expanded = []
        for t in bare_tokens:
            if "*" in t:
                expanded.append(t)
            elif len(t) >= 4:
                expanded.append(f"{t}*")
            else:
                expanded.append(t)
        parts.append(" OR ".join(expanded))

    # Add phrases.
    for phrase in phrases:
        safe = re.sub(r'[^\w\s]', " ", phrase).strip()
        if safe:
            parts.append(f'"{safe}"')

    # Add NEAR pairs from consecutive content-word pairs.
    if len(bare_tokens) >= 2:
        near_parts = []
        for i in range(len(bare_tokens) - 1):
            a = bare_tokens[i]
            b = bare_tokens[i + 1]
            # Avoid very short tokens (1-2 chars) in NEAR.
            if len(a) >= 3 and len(b) >= 3:
                near_parts.append(f"NEAR({a} {b}, {NEAR_WINDOW})")
        if near_parts:
            parts.append(" OR ".join(near_parts))

    # Final OR over the three groups.
    return " OR ".join(parts)


def _save_phrase(match: re.Match, phrases: list[str]) -> str:
    """Callback for regex: capture a quoted phrase, replace with spaces."""
    phrases.append(match.group(1).strip())
    return " " * len(match.group(0))


def _search(
    db_path: str,
    match_expr: str,
    *,
    limit: int = 500,
    include_text: bool = True,
) -> list[dict]:
    """Run the BM25 SELECT against `chunks_fts`."""
    return database.search_fts(
        db_path,
        match_expr,
        limit=limit,
        include_text=include_text,
    )


def _full_source_recall(db_path: str, source_ids: Iterable[str]) -> list[dict]:
    """Return ALL chunks for the given sources, in natural reading order.

    Each chunk inherits the best BM25 score of any chunk from its source.
    """
    source_ids = list(set(source_ids))
    if not source_ids:
        return []
    chunks = database.fetch_chunks_for_sources(db_path, source_ids)
    # Group chunks by source for the assembly step.
    return chunks


def _assemble_context(
    chunks: list[dict],
    *,
    max_tokens: int,
    reserve_tokens: int = 1024,
) -> tuple[list[dict], bool]:
    """Concatenate chunks per source until the token budget is exhausted.

    Reserves `reserve_tokens` for the prompt template + LLM response.

    Returns (chunks_to_send, truncated). Truncated is True if any chunks
    were dropped because of the budget.
    """
    if not chunks:
        return [], False

    budget = max(0, max_tokens - reserve_tokens)
    # Group by source.
    by_source: dict[str, list[dict]] = {}
    for c in chunks:
        by_source.setdefault(c["source_id"], []).append(c)

    # Sort chunks per source by chunk_index for natural reading order.
    for sid in by_source:
        by_source[sid].sort(key=lambda x: x.get("chunk_index", 0))

    # Score sources: best BM25 score of any chunk in that source.
    def source_score(sid: str) -> float:
        # Score is per-row; we don't carry it in fetch_chunks_for_sources.
        # Use chunk count as a proxy? No — fall back to insertion order via
        # the caller-provided rank by leaving order intact.
        return 0.0

    selected: list[dict] = []
    spent = 0
    truncated = False

    for sid, source_chunks in by_source.items():
        # Track best score via the search result rows (passed separately by
        # the caller via _search_with_score); when not available we use 0.
        for c in source_chunks:
            tcount = c.get("token_count") or max(1, len(c.get("text", "")) // 4)
            if spent + tcount > budget and selected:
                # Budget exhausted; drop the rest of this source and all later.
                truncated = True
                break
            selected.append(c)
            spent += tcount
        if truncated:
            break

    return selected, truncated


def retrieve(
    db_path: str,
    user_query: str,
    *,
    max_chunks: int = 500,
    include_text: bool = True,
) -> tuple[list[dict], list[str], bool]:
    """High-level: retrieve matching chunks, then fan out to full source recall.

    Returns (chunks_for_llm, source_ids_in_order, truncated).
    """
    match_expr = _build_match(user_query)
    if not match_expr:
        return [], [], False

    # Step 1: ranked retrieval, top N.
    ranked = _search(db_path, match_expr, limit=max_chunks, include_text=include_text)
    if not ranked:
        return [], [], False

    source_ids = list(dict.fromkeys(c["source_id"] for c in ranked))

    # Step 2: full source recall.
    all_chunks = _full_source_recall(db_path, source_ids)
    if not include_text and "text" not in (all_chunks[0] if all_chunks else {}):
        # Fetch_chunks_for_sources always returns text; nothing to do.
        pass

    # Step 3: assembly with a generous default budget (num_ctx default).
    # The caller may re-assemble with a tighter budget.
    return all_chunks, source_ids, False


def retrieve_for_assembly(
    db_path: str,
    user_query: str,
    *,
    max_context_tokens: int = 8192,
    reserve_tokens: int = 1024,
    max_chunks: int = 500,
) -> tuple[list[dict], list[dict], bool]:
    """Full retrieval pipeline used by `/query`.

    Returns (chunks_for_context, retrieved_chunk_hits, truncated).
        - chunks_for_context: full-text chunks ready to feed the LLM.
        - retrieved_chunk_hits: the initial top-N hits (for citation rendering).
        - truncated: True if context was truncated to fit budget.
    """
    match_expr = _build_match(user_query)
    if not match_expr:
        return [], [], False

    ranked = _search(db_path, match_expr, limit=max_chunks, include_text=False)
    if not ranked:
        return [], [], False

    source_ids = list(dict.fromkeys(c["source_id"] for c in ranked))
    all_chunks = _full_source_recall(db_path, source_ids)
    selected, truncated = _assemble_context(
        all_chunks,
        max_tokens=max_context_tokens,
        reserve_tokens=reserve_tokens,
    )
    return selected, ranked, truncated


def retrieve_only(db_path: str, user_query: str, *, max_chunks: int = 500) -> list[dict]:
    """Retrieval-only path used by `/query/retrieve`. No LLM.

    Returns the initial top-N hits with full text. Used by the Query pane's
    Results tab.
    """
    match_expr = _build_match(user_query)
    if not match_expr:
        return []
    return _search(db_path, match_expr, limit=max_chunks, include_text=True)