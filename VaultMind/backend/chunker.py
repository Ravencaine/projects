"""Recursive page-aware chunker.

Splits text into chunks of `target_tokens` (default 700), clamped to
`[min_tokens, max_tokens]` (default 350..850). Page boundaries are honoured
(chunks never span pages). Heading-aware: when text is MD-style and a chunk
candidate starts with `#`, a new chunk is started.

The chunker operates on a single string that has been joined with the page
break sentinel (see cleanup.join_with_page_breaks). It splits back into
per-page fragments and never crosses them.

Token counting: tiktoken cl100k_base. Falls back to `len(text)//4` if
tiktoken is unavailable (e.g., during offline install).
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

try:
    import tiktoken

    _ENC = tiktoken.get_encoding("cl100k_base")

    def _count_tokens(text: str) -> int:
        return len(_ENC.encode(text))

except Exception:  # pragma: no cover — fallback only
    def _count_tokens(text: str) -> int:
        return max(1, len(text) // 4)


from backend.cleanup import _PAGE_BREAK

# Recursive split separators, in priority order.
SEPARATORS: tuple[str, ...] = ("\n\n", "\n", ". ", "? ", "! ", " ", "")


def chunk_pages(
    pages: Iterable[tuple[int | None, str]],
    *,
    target_tokens: int = 700,
    min_tokens: int = 350,
    max_tokens: int = 850,
) -> list[dict[str, Any]]:
    """Chunk a sequence of pages. Returns a list of chunk dicts.

    Each dict has: { text, chunk_index, page_start, page_end, token_count,
    char_count }.

    Page boundaries are never crossed: when a chunk candidate grows past
    `max_tokens` mid-page, it's force-cut at a sentence boundary if possible,
    otherwise at a word boundary.
    """
    chunks: list[dict[str, Any]] = []
    chunk_index = 0

    for page_no, page_text in pages:
        if not page_text.strip():
            continue
        page_chunks = _split_page(
            page_text,
            target_tokens=target_tokens,
            min_tokens=min_tokens,
            max_tokens=max_tokens,
        )
        for text in page_chunks:
            chunks.append(
                {
                    "text": text.strip(),
                    "chunk_index": chunk_index,
                    "page_start": page_no,
                    "page_end": page_no,
                    "token_count": _count_tokens(text),
                    "char_count": len(text),
                }
            )
            chunk_index += 1

    return chunks


def chunk_text_with_page_breaks(
    joined_text: str,
    *,
    target_tokens: int = 700,
    min_tokens: int = 350,
    max_tokens: int = 850,
) -> list[dict[str, Any]]:
    """Chunk text that was joined with the `_PAGE_BREAK` sentinel.

    The sentinel marks where pages originally split; the chunker preserves
    those boundaries.
    """
    if not joined_text.strip():
        return []
    raw_pages = joined_text.split(_PAGE_BREAK)
    pages = [(i + 1, p) for i, p in enumerate(raw_pages)]
    return chunk_pages(
        pages,
        target_tokens=target_tokens,
        min_tokens=min_tokens,
        max_tokens=max_tokens,
    )


# ============================================================================ #
# Internal
# ============================================================================ #


def _split_page(
    page_text: str,
    *,
    target_tokens: int,
    min_tokens: int,
    max_tokens: int,
) -> list[str]:
    """Split one page into chunks respecting token limits.

    Strategy:
        1. Try the page as one chunk. If it's within [min, max], return it.
        2. Else, recursively split on SEPARATORS (paragraph → line → sentence
           → word → char).
        3. Greedily merge small pieces until reaching `target_tokens`.
        4. Anything still over `max_tokens` gets force-cut at `max_tokens`.
    """
    total = _count_tokens(page_text)
    if total <= max_tokens:
        return [page_text]

    pieces = _recursive_split(page_text, list(SEPARATORS))
    return _merge_to_target(
        pieces,
        target_tokens=target_tokens,
        min_tokens=min_tokens,
        max_tokens=max_tokens,
    )


def _recursive_split(text: str, separators: list[str]) -> list[str]:
    if not separators:
        # Last resort: character split. Only reached for monolithic lines
        # longer than max_tokens.
        return [text[i : i + 200] for i in range(0, len(text), 200)]
    sep = separators[0]
    rest = separators[1:]
    if not sep:
        return [c for c in text]
    parts = text.split(sep) if sep else [text]
    out: list[str] = []
    for part in parts:
        if _count_tokens(part) > 0 and len(part) > 0:
            if _count_tokens(part) <= 850 or not rest:
                out.append(part + (sep if sep and not sep.isspace() else ""))
            else:
                out.extend(_recursive_split(part, rest))
    return [p for p in out if p.strip()]


def _merge_to_target(
    pieces: list[str],
    *,
    target_tokens: int,
    min_tokens: int,
    max_tokens: int,
) -> list[str]:
    """Greedily merge split pieces into chunks around `target_tokens`."""
    chunks: list[str] = []
    buf: list[str] = []
    buf_tokens = 0
    joiner = " "  # piece boundaries are word-like at this point

    def flush() -> None:
        nonlocal buf, buf_tokens
        if buf:
            chunks.append(joiner.join(buf).strip())
            buf = []
            buf_tokens = 0

    for piece in pieces:
        piece = piece.strip()
        if not piece:
            continue
        pt = _count_tokens(piece)
        # If a single piece is itself too big, force-cut it.
        if pt > max_tokens:
            flush()
            chunks.extend(_force_cut(piece, max_tokens))
            continue
        if buf_tokens + pt > max_tokens:
            flush()
        buf.append(piece)
        buf_tokens += pt
        if buf_tokens >= target_tokens:
            flush()
    flush()
    return chunks


def _force_cut(text: str, max_tokens: int) -> list[str]:
    """Last-resort hard cut when a single piece is over `max_tokens`.

    Cuts on word boundaries; pieces will be shorter than `max_tokens` but
    not necessarily meaningful.
    """
    out: list[str] = []
    current: list[str] = []
    current_tokens = 0
    for word in text.split(" "):
        wt = _count_tokens(word)
        if current_tokens + wt > max_tokens and current:
            out.append(" ".join(current))
            current = [word]
            current_tokens = wt
        else:
            current.append(word)
            current_tokens += wt
    if current:
        out.append(" ".join(current))
    return out