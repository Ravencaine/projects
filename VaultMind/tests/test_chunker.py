"""Chunker tests.

Verifies page-awareness, token-target range, and recursive splitting
behaviour.
"""

from __future__ import annotations

from backend.chunker import chunk_pages, chunk_text_with_page_breaks


def test_short_page_one_chunk():
    pages = [(1, "Hello world. This is a short page.")]
    chunks = chunk_pages(pages)
    assert len(chunks) == 1
    assert chunks[0]["chunk_index"] == 0
    assert chunks[0]["page_start"] == 1
    assert chunks[0]["page_end"] == 1


def test_page_boundaries_respected():
    """A chunk must never span a page boundary."""
    page1 = "Page one content. " * 100  # ~300 tokens
    page2 = "Page two content. " * 100  # ~300 tokens
    page3 = "Page three content. " * 100  # ~300 tokens
    chunks = chunk_pages([(1, page1), (2, page2), (3, page3)])

    for c in chunks:
        assert c["page_start"] == c["page_end"], (
            f"chunk spans pages {c['page_start']}–{c['page_end']}: {c['text'][:60]}"
        )


def test_long_page_splits_into_multiple():
    """A long page should produce multiple chunks around the target size."""
    long_page = " ".join(f"sentence {i}." for i in range(500))  # ~1000 tokens
    chunks = chunk_pages(
        [(1, long_page)],
        target_tokens=100,
        min_tokens=40,
        max_tokens=160,
    )
    assert len(chunks) >= 4  # 1000 tokens / ~100 target → at least 4 chunks


def test_empty_pages_skipped():
    pages = [(1, ""), (2, "real content"), (3, "   "), (4, "more")]
    chunks = chunk_pages(pages)
    assert len(chunks) == 2
    assert chunks[0]["page_start"] == 2
    assert chunks[1]["page_start"] == 4


def test_chunk_text_with_page_breaks_preserves_pages():
    """The page-break sentinel should preserve the original page split."""
    from backend.cleanup import _PAGE_BREAK

    text = _PAGE_BREAK.join(["page one body.", "page two body.", "page three body."])
    chunks = chunk_text_with_page_breaks(text)
    assert len(chunks) == 3
    assert [c["page_start"] for c in chunks] == [1, 2, 3]


def test_chunk_index_monotonic():
    pages = [
        (1, "alpha. " * 200),
        (2, "beta. " * 200),
        (3, "gamma. " * 200),
    ]
    chunks = chunk_pages(pages, target_tokens=80, max_tokens=120)
    indices = [c["chunk_index"] for c in chunks]
    assert indices == sorted(indices)
    assert indices == list(range(len(chunks)))
