"""Text cleanup after extraction, before chunking.

Goals:
    - Strip repeating headers/footers (lines that appear identically on ≥3
      consecutive pages).
    - Fix hyphenated line-break artefacts ("confi-\ndence" → "confidence").
    - Normalise whitespace.
    - Drop zero-length "pages".

Pure functions, no I/O. Operates on the list of (page_no, text) tuples
returned by extractors.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Iterable

# Lines shorter than this are skipped when hunting for headers/footers.
HEADER_FOOTER_MIN_LEN = 8
# A line is considered a header/footer if it appears at least this many times
# across the input. Three is a safe threshold for typical PDFs/documents.
HEADER_FOOTER_MIN_COUNT = 3

# Hyphenated newline: a word ending in `-` followed by an EOL and a lowercase
# letter (most common case for joined words). Restore by removing the `-` and
# the newline.
_HYPHEN_NEWLINE = re.compile(r"(\w)-\n(\w)")

# Collapse runs of horizontal whitespace within a line.
_HORIZ_WS = re.compile(r"[ \t]+")

# Collapse 3+ blank lines into 2.
_BLANK_RUN = re.compile(r"\n{3,}")

# Page boundary marker (used internally by chunker.py).
_PAGE_BREAK = "\n\n\x1ePAGE_BREAK\x1e\n\n"


def clean_pages(pages: Iterable[tuple[int | None, str]]) -> list[tuple[int | None, str]]:
    """Apply cleanup to a list of (page_no, text) tuples. Returns a new list."""
    # Materialise once so the iterable isn't drained by the header/footer scan.
    pages_list = list(pages)
    headers_footers = _detect_headers_footers(pages_list)
    cleaned: list[tuple[int | None, str]] = []
    for page_no, text in pages_list:
        text = _strip_headers_footers(text, headers_footers)
        text = _fix_hyphenated_newlines(text)
        text = _normalize_whitespace(text)
        if text.strip():
            cleaned.append((page_no, text))
    return cleaned


def join_with_page_breaks(pages: Iterable[tuple[int | None, str]]) -> str:
    """Concatenate pages with a sentinel separator the chunker uses to honour
    page boundaries."""
    parts = [t for _, t in pages]
    return _PAGE_BREAK.join(parts)


# ============================================================================ #
# Internal helpers
# ============================================================================ #


def _detect_headers_footers(pages: Iterable[tuple[int | None, str]]) -> set[str]:
    """Return a set of lines that appear on >= HEADER_FOOTER_MIN_COUNT pages."""
    counts: Counter[str] = Counter()
    for _, text in pages:
        seen_on_this_page: set[str] = set()
        for line in text.splitlines():
            stripped = line.strip()
            if (
                len(stripped) >= HEADER_FOOTER_MIN_LEN
                and not stripped.isdigit()
                and stripped not in seen_on_this_page
            ):
                counts[stripped] += 1
                seen_on_this_page.add(stripped)
    return {
        line
        for line, n in counts.items()
        if n >= HEADER_FOOTER_MIN_COUNT
    }


def _strip_headers_footers(text: str, headers_footers: set[str]) -> str:
    if not headers_footers:
        return text
    kept: list[str] = []
    for line in text.splitlines():
        if line.strip() in headers_footers:
            continue
        kept.append(line)
    return "\n".join(kept)


def _fix_hyphenated_newlines(text: str) -> str:
    return _HYPHEN_NEWLINE.sub(r"\1\2", text)


def _normalize_whitespace(text: str) -> str:
    # Trim trailing whitespace per line, then collapse internal horizontal
    # whitespace, then collapse blank-line runs.
    lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(lines)
    text = _HORIZ_WS.sub(" ", text)
    text = _BLANK_RUN.sub("\n\n", text)
    return text.strip()