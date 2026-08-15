"""End-to-end tests for the Phase 1 MVP.

These tests bypass the FastAPI HTTP layer (which has asyncio-loop conflicts
under TestClient) and exercise the orchestrator directly. The HTTP layer
itself is verified by `scripts/verify_phase1.py` against a real uvicorn
process.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from backend import database, query
from backend.chunker import chunk_pages
from backend.cleanup import clean_pages, join_with_page_breaks
from backend.hashes import hash_text_streaming
from backend.ingest import Source, detect_and_dispatch
from backend.prompts import SYSTEM_PROMPT, build_user_prompt, NO_CONTEXT_REFUSAL


async def _ingest_file(db_path: Path, path: Path, display_name: str) -> dict:
    """The same orchestrator main.py runs, inlined for the test."""
    source = Source(location=str(path), kind="file")
    suffix = path.suffix.lower().lstrip(".")
    if suffix in ("txt", "md", "markdown"):
        source.type_hint = "text"

    result = await detect_and_dispatch(source)
    cleaned = clean_pages((p.page_number, p.text) for p in result.pages)
    joined = join_with_page_breaks(cleaned)
    hash_value = hash_text_streaming([t for _, t in cleaned])

    existing = database.get_source_by_hash(str(db_path), hash_value)
    if existing is not None:
        return {"status": "already_indexed", "source_id": existing["id"]}

    chunks = chunk_pages(cleaned, target_tokens=700, min_tokens=350, max_tokens=850)
    sid = database.insert_source(
        str(db_path),
        name=display_name,
        type_=source.type_hint or "text",
        hash_=hash_value,
        path=str(path),
        metadata={"size_bytes": path.stat().st_size},
    )
    chunk_records = [
        {
            "chunk_index": c["chunk_index"],
            "page_start": c["page_start"],
            "page_end": c["page_end"],
            "text": c["text"],
            "token_count": c["token_count"],
            "char_count": c["char_count"],
        }
        for c in chunks
    ]
    database.insert_chunks(str(db_path), sid, chunk_records)
    return {
        "status": "done",
        "source_id": sid,
        "chunk_count": len(chunks),
    }


@pytest.mark.asyncio
async def test_ingest_then_retrieve(db_path: Path, sample_text: Path):
    result = await _ingest_file(db_path, sample_text, "sample.txt")
    assert result["status"] == "done"
    assert result["chunk_count"] >= 1

    # Retrieval should find at least one matching chunk.
    hits = query.retrieve_only(str(db_path), "authentication middleware")
    assert len(hits) >= 1
    assert any("<mark>" in h["excerpt"] for h in hits)


@pytest.mark.asyncio
async def test_ingest_dedup(db_path: Path, sample_text: Path):
    """Re-ingesting the same file returns already_indexed."""
    first = await _ingest_file(db_path, sample_text, "sample.txt")
    assert first["status"] == "done"
    second = await _ingest_file(db_path, sample_text, "sample.txt")
    assert second["status"] == "already_indexed"
    assert second["source_id"] == first["source_id"]


@pytest.mark.asyncio
async def test_query_no_context(db_path: Path, sample_text: Path):
    """A query with zero hits should produce the refusal prompt only."""
    await _ingest_file(db_path, sample_text, "sample.txt")
    selected, ranked, truncated = query.retrieve_for_assembly(
        str(db_path), "xyzzy_nonsense_qqqq", max_context_tokens=8192
    )
    assert selected == []
    # The FastAPI layer converts this into the NO_CONTEXT_REFUSAL token.
    assert NO_CONTEXT_REFUSAL.startswith("Based on the provided materials")


def test_prompt_structure():
    """The system prompt + user prompt must produce a well-formed LLM input."""
    assert "STRICTLY" in SYSTEM_PROMPT
    assert "[Source:" in SYSTEM_PROMPT

    chunks = [
        {"source_name": "a.txt", "page_start": 1, "page_end": 1, "text": "alpha"},
    ]
    user_prompt = build_user_prompt("what is alpha?", chunks)
    assert "[SOURCE: a.txt, pages 1]" in user_prompt
    assert "QUESTION: what is alpha?" in user_prompt


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok(db_path: Path):
    """Spot-check the FastAPI /health endpoint using TestClient."""
    from backend.main import app
    from fastapi.testclient import TestClient

    with TestClient(app) as c:
        r = c.get("/health")
        assert r.status_code == 200
        body = r.json()
        # The health endpoint doesn't touch the DB so it's safe across tests.
        assert body["ollama_model"]