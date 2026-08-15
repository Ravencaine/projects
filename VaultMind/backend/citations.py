"""Citation marker extraction from streamed LLM tokens.

The LLM is instructed to produce markers of the form `[Source: <name>, p.<n>]`.
This module parses those markers out of a streaming buffer and yields:

    - the cleaned text (markers stripped) for display
    - the de-duplicated list of `{source_name, page}` pairs

Used by the SSE stream handler in `main.py` to attach citation chips to
each assistant bubble.
"""

from __future__ import annotations

import re
from collections.abc import Iterator

# Match [Source: <name>, p.<n>] — name may contain spaces, digits, punctuation.
# We also tolerate variations like `p. 12`, `page 12`, `p 12`.
_CITATION_RE = re.compile(
    r"\[Source:\s*([^,\]]+?),\s*(?:p\.?|page)\s*(\d+)\s*\]",
    re.IGNORECASE,
)


def extract_citations(text: str) -> list[dict]:
    """Return all (source_name, page) pairs found in `text`, in order, deduped."""
    seen: set[tuple[str, int]] = set()
    out: list[dict] = []
    for m in _CITATION_RE.finditer(text):
        name = m.group(1).strip()
        try:
            page = int(m.group(2))
        except (TypeError, ValueError):
            continue
        key = (name.lower(), page)
        if key in seen:
            continue
        seen.add(key)
        out.append({"source_name": name, "page": page})
    return out


def strip_citations(text: str) -> str:
    """Remove citation markers from display text.

    Leaves the surrounding whitespace intact and collapses any double-space
    left behind.
    """
    cleaned = _CITATION_RE.sub("", text)
    # Collapse double spaces that may result from markers mid-word.
    cleaned = re.sub(r"  +", " ", cleaned)
    return cleaned


class CitationStreamParser:
    """Streaming extractor that handles citation markers split across tokens.

    Buffers the last 64 characters so a marker like `[Source: foo, p.1`
    arriving in one chunk and `]` in the next is captured correctly.
    """

    BUFFER = 64

    def __init__(self) -> None:
        self._buf = ""
        self._seen: set[tuple[str, int]] = set()
        self._citations: list[dict] = []

    def feed(self, token: str) -> tuple[str, list[dict]]:
        """Append `token` to the buffer.

        Returns:
            (cleaned_text, new_citations)

        `cleaned_text` is the raw token with any complete citation markers
        stripped. `new_citations` is the list of citations newly found in
        this token (across the buffer).
        """
        self._buf += token
        # Drain the buffer up to the last complete `]`.
        last_close = self._buf.rfind("]")
        if last_close < 0:
            # No complete marker yet; keep buffering.
            return token, []
        flushable = self._buf[: last_close + 1]
        self._buf = self._buf[last_close + 1 :]

        # Find new citations in the flushable portion.
        new: list[dict] = []
        for m in _CITATION_RE.finditer(flushable):
            name = m.group(1).strip()
            try:
                page = int(m.group(2))
            except (TypeError, ValueError):
                continue
            key = (name.lower(), page)
            if key in self._seen:
                continue
            self._seen.add(key)
            citation = {"source_name": name, "page": page}
            self._citations.append(citation)
            new.append(citation)

        return strip_citations(token), new

    def all(self) -> list[dict]:
        """Return every citation seen so far, in order."""
        return list(self._citations)


def iter_citations(text: str) -> Iterator[dict]:
    """Yield citations in `text` without dedup. Use `extract_citations` for dedup."""
    for m in _CITATION_RE.finditer(text):
        yield {"source_name": m.group(1).strip(), "page": int(m.group(2))}