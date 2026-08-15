"""Database layer tests.

Verifies the SQLite + FTS5 schema, the sync triggers, BM25 search with
snippet generation, full-source recall via fetch_chunks_for_sources, and
the dedup-by-hash path.
"""

from __future__ import annotations

from backend import database


def _make_source(db, *, name: str, hash_: str, type_: str = "text") -> str:
    return database.insert_source(db, name=name, type_=type_, hash_=hash_)


def test_schema_initialises(tmp_path):
    """init_db creates all tables and the FTS5 integrity check passes."""
    db = tmp_path / "test.db"
    database.init_db(db)
    # Should not raise.
    database.init_db(db)
    # FTS5 integrity check.
    database.get_connection(db).execute(
        "INSERT INTO chunks_fts(chunks_fts) VALUES ('integrity-check')"
    )


def test_insert_and_get_source(db_path):
    sid = _make_source(db_path, name="a.txt", hash_="abc")
    row = database.get_source(db_path, sid)
    assert row is not None
    assert row["name"] == "a.txt"
    assert row["type"] == "text"


def test_source_dedup_by_hash(db_path):
    _make_source(db_path, name="a.txt", hash_="same-hash")
    row = database.get_source_by_hash(db_path, "same-hash")
    assert row is not None
    # Re-insert would conflict at the DB level; dedup logic in _run_ingest
    # catches it earlier via get_source_by_hash.


def test_chunks_fts_trigger(db_path):
    """Inserting a chunk should populate the FTS5 index automatically."""
    sid = _make_source(db_path, name="a.txt", hash_="h1")
    database.insert_chunks(
        db_path,
        sid,
        [
            {"chunk_index": 0, "text": "the quick brown fox", "page_start": 1,
             "page_end": 1, "token_count": 4, "char_count": 20},
            {"chunk_index": 1, "text": "lazy dogs and cats", "page_start": 1,
             "page_end": 1, "token_count": 4, "char_count": 18},
        ],
    )

    # BM25 search via the database layer.
    hits = database.search_fts(db_path, "quick fox", include_text=False)
    assert len(hits) >= 1
    # snippet() should wrap matched terms in <mark>.
    assert "<mark>" in hits[0]["excerpt"]


def test_chunks_fts_update_trigger(db_path):
    """Updating chunks.text should update the FTS5 index."""
    sid = _make_source(db_path, name="a.txt", hash_="h2")
    database.insert_chunks(
        db_path,
        sid,
        [{"chunk_index": 0, "text": "alpha content", "page_start": 1, "page_end": 1,
          "token_count": 2, "char_count": 14}],
    )
    # Find the chunk rowid.
    conn = database.get_connection(db_path)
    rowid = conn.execute("SELECT rowid FROM chunks WHERE source_id = ?", (sid,)).fetchone()[0]
    conn.execute("UPDATE chunks SET text = ? WHERE rowid = ?", ("beta content", rowid))

    hits_old = database.search_fts(db_path, "alpha", include_text=False)
    hits_new = database.search_fts(db_path, "beta", include_text=False)
    assert hits_old == []
    assert len(hits_new) == 1


def test_chunks_fts_delete_trigger(db_path):
    """Deleting a source should remove its chunks from the FTS5 index."""
    sid = _make_source(db_path, name="a.txt", hash_="h3")
    database.insert_chunks(
        db_path,
        sid,
        [{"chunk_index": 0, "text": "unique keyword xyzzy", "page_start": 1,
          "page_end": 1, "token_count": 3, "char_count": 19}],
    )
    assert len(database.search_fts(db_path, "xyzzy", include_text=False)) == 1
    database.delete_source(db_path, sid)
    assert len(database.search_fts(db_path, "xyzzy", include_text=False)) == 0


def test_full_source_recall(db_path):
    """fetch_chunks_for_sources should return all chunks of all matched sources."""
    sid_a = _make_source(db_path, name="a.txt", hash_="ha")
    sid_b = _make_source(db_path, name="b.txt", hash_="hb")
    database.insert_chunks(
        db_path, sid_a,
        [
            {"chunk_index": 0, "text": "alpha alpha alpha", "page_start": 1, "page_end": 1,
             "token_count": 3, "char_count": 18},
            {"chunk_index": 1, "text": "beta", "page_start": 2, "page_end": 2,
             "token_count": 1, "char_count": 4},
        ],
    )
    database.insert_chunks(
        db_path, sid_b,
        [
            {"chunk_index": 0, "text": "gamma gamma", "page_start": 1, "page_end": 1,
             "token_count": 2, "char_count": 12},
        ],
    )

    chunks = database.fetch_chunks_for_sources(db_path, [sid_a, sid_b])
    assert len(chunks) == 3
    # All chunks from A are returned even though only "alpha" matched.
    texts = sorted(c["text"] for c in chunks)
    assert "alpha alpha alpha" in texts
    assert "beta" in texts
    assert "gamma gamma" in texts


def test_phrase_search(db_path):
    """Quoted phrase should be matched exactly."""
    sid = _make_source(db_path, name="a.txt", hash_="hp")
    database.insert_chunks(
        db_path, sid,
        [
            {"chunk_index": 0, "text": "rate limit exceeded", "page_start": 1, "page_end": 1,
             "token_count": 3, "char_count": 19},
            {"chunk_index": 1, "text": "request rate was high", "page_start": 1, "page_end": 1,
             "token_count": 4, "char_count": 22},
        ],
    )
    # Phrase match via FTS5 syntax directly.
    hits = database.search_fts(db_path, '"rate limit"', include_text=False)
    assert len(hits) == 1
    assert "rate limit" in hits[0]["excerpt"].lower()


def test_stats(db_path):
    sid = _make_source(db_path, name="a.txt", hash_="hs")
    database.insert_chunks(
        db_path, sid,
        [
            {"chunk_index": 0, "text": "one", "page_start": 1, "page_end": 1,
             "token_count": 1, "char_count": 3},
            {"chunk_index": 1, "text": "two three", "page_start": 1, "page_end": 1,
             "token_count": 2, "char_count": 9},
        ],
    )
    s = database.get_stats(db_path)
    assert s["source_count"] == 1
    assert s["chunk_count"] == 2
    assert s["token_count"] == 3


def test_messages(db_path):
    mid = database.insert_message(db_path, role="user", content="hello")
    msgs = database.list_messages(db_path)
    assert len(msgs) == 1
    assert msgs[0]["id"] == mid
    assert msgs[0]["role"] == "user"

    database.clear_messages(db_path)
    assert database.list_messages(db_path) == []
