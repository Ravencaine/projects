"""Streaming SHA-256 over extracted text.

Computes a content hash for dedup. The hash is over the full extracted text
(not per-chunk) so re-ingesting the same source skips work.

Implementation note: this is intentionally sync because hashing is fast and
inlining it inside the extractor's async coroutine gives a natural
`asyncio.sleep(0)` opportunity to keep the loop responsive.
"""

from __future__ import annotations

import hashlib

CHUNK_SIZE = 65536  # 64 KB read buffer


def hash_text(text: str) -> str:
    """Return the SHA-256 hex digest of a string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hash_text_streaming(chunks: list[str], on_progress=None) -> str:
    """Stream-hash a list of text chunks (e.g., one per page).

    Calls `on_progress(n)` after each chunk if provided. The hash itself is
    stable across runs because the input order is preserved.
    """
    h = hashlib.sha256()
    for i, chunk in enumerate(chunks):
        if chunk:
            h.update(chunk.encode("utf-8"))
        if on_progress is not None:
            on_progress(i + 1)
    return h.hexdigest()