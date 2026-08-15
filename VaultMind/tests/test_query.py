"""Query pipeline tests.

Verifies _build_match produces valid FTS5 expressions and the retrieve +
full-source-recall + assembly pipeline returns sensible chunks.
"""

from __future__ import annotations

from backend import database, query


def test_build_match_basic():
    expr = query._build_match("how does auth work")
    assert "auth" in expr and "work" in expr
    # Stop words ("how", "does") are stripped; only content words remain.


def test_build_match_phrase():
    expr = query._build_match('"rate limit" exceeded')
    assert '"rate limit"' in expr


def test_build_match_near_pair():
    expr = query._build_match("authentication middleware")
    assert "NEAR(" in expr


def test_build_match_empty():
    assert query._build_match("") == ""
    # All stop words → also empty.
    assert query._build_match("the a an") == ""


def test_build_match_strips_reserved():
    # `test` has 4+ chars → gets the wildcard; `foo` is shorter, does not.
    expr = query._build_match("test() foo")
    bare_group = expr.split(" OR NEAR(")[0]
    assert "(" not in bare_group
    assert "test*" in bare_group
    # Either `foo` (no wildcard) or `foo*` is acceptable.
    assert "foo" in bare_group


def test_build_match_prefix_wildcard():
    # 4+ char bare tokens get prefix wildcards.
    expr = query._build_match("config")
    assert "config*" in expr


def test_retrieve_only_returns_hits(db_path):
    sid = database.insert_source(db_path, name="a.txt", type_="text", hash_="h1")
    database.insert_chunks(
        db_path, sid,
        [
            {"chunk_index": 0, "text": "auth middleware handles login", "page_start": 1,
             "page_end": 1, "token_count": 4, "char_count": 29},
            {"chunk_index": 1, "text": "rate limiting blocks bots", "page_start": 1,
             "page_end": 1, "token_count": 4, "char_count": 25},
        ],
    )
    hits = query.retrieve_only(db_path, "auth middleware")
    assert len(hits) >= 1
    # Excerpt should be HTML-marked.
    assert any("<mark>" in h["excerpt"] for h in hits)


def test_full_source_recall(db_path):
    """A matching chunk triggers recall of every chunk from its source."""
    sid = database.insert_source(db_path, name="a.txt", type_="text", hash_="h2")
    database.insert_chunks(
        db_path, sid,
        [
            {"chunk_index": 0, "text": "auth intro paragraph", "page_start": 1,
             "page_end": 1, "token_count": 3, "char_count": 22},
            {"chunk_index": 1, "text": "auth method two: oauth", "page_start": 2,
             "page_end": 2, "token_count": 4, "char_count": 22},
            {"chunk_index": 2, "text": "unrelated content here", "page_start": 3,
             "page_end": 3, "token_count": 3, "char_count": 23},
        ],
    )
    selected, ranked, truncated = query.retrieve_for_assembly(
        db_path, "auth oauth", max_context_tokens=8192
    )
    # Even though only the auth chunks match, all three are returned.
    assert len(selected) == 3
    assert not truncated


def test_retrieve_empty_query(db_path):
    assert query.retrieve_only(db_path, "") == []


def test_assembly_truncates_by_token_budget(db_path):
    """Context assembly should drop chunks when budget is exceeded."""
    sid = database.insert_source(db_path, name="a.txt", type_="text", hash_="h3")
    # 5 chunks of 50 tokens each = 250 tokens.
    chunks = [
        {"chunk_index": i,
         "text": " ".join(f"word{i}_{n}" for n in range(50)),
         "page_start": 1, "page_end": 1,
         "token_count": 50, "char_count": 300}
        for i in range(5)
    ]
    database.insert_chunks(db_path, sid, chunks)
    selected, ranked, truncated = query.retrieve_for_assembly(
        db_path, "word1_0", max_context_tokens=120, reserve_tokens=20
    )
    # Budget = 100 tokens. 50 fits, 100 doesn't fit. Should be truncated.
    assert truncated
    assert len(selected) < 5
