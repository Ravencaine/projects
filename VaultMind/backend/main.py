"""FastAPI application entry point for VaultMind.

Endpoints:
    POST /ingest               multipart file or JSON URL → enqueue job
    GET  /ingest/{job_id}/events  SSE stream of job progress
    GET  /sources              list sources
    DELETE /sources/{id}       delete source + chunks
    POST /query                SSE stream of retrieval + LLM answer
    GET  /query/retrieve       retrieval-only (no LLM)
    GET  /chat/history         list messages
    DELETE /chat/history       clear all messages
    GET  /stats                vault stats
    GET  /health               health + Ollama reachability

Run dev mode:
    uvicorn backend.main:app --port 8765 --reload
"""

from __future__ import annotations

import asyncio
import io
import json
import logging
import shutil
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import (
    FastAPI,
    File,
    Form,
    HTTPException,
    Request,
    UploadFile,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse

from backend import database, ollama_client, progress, query
from backend.chunker import chunk_pages
from backend.cleanup import clean_pages, join_with_page_breaks
from backend.config import get_settings
from backend.citations import CitationStreamParser
from backend.hashes import hash_text_streaming
from backend.ingest import Source, detect_and_dispatch
from backend.models import (
    ChunkHit,
    Health,
    IngestAccepted,
    Message,
    QueryRequest,
    RetrieveRequest,
    RetrieveResponse,
    Source as SourceModel,
    Stats,
)
from backend.prompts import (
    NO_CONTEXT_REFUSAL,
    SYSTEM_PROMPT,
    build_user_prompt,
)

logger = logging.getLogger("vaultmind")

# ============================================================================ #
# Lifespan
# ============================================================================ #


@asynccontextmanager
async def lifespan(app: FastAPI):
    cfg = get_settings()
    paths = cfg.db_path
    database.init_db(paths)
    logger.info("VaultMind backend ready (model=%s, num_ctx=%d)", cfg.model, cfg.num_ctx)
    yield
    # No tear-down required: thread-local SQLite connections close on process
    # exit. WAL files are checkpointed by SQLite automatically.


# ============================================================================ #
# App
# ============================================================================ #


app = FastAPI(
    title="VaultMind",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,
)


cfg = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.cors_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


# ============================================================================ #
# Health + stats
# ============================================================================ #


@app.get("/health", response_model=Health)
async def health():
    cfg = get_settings()
    reachable = await ollama_client.is_reachable()
    return Health(
        status="ok" if reachable else "degraded",
        ollama_reachable=reachable,
        ollama_model=cfg.model,
        whisper_model=cfg.whisper_model,
        vault_dir=str(cfg.vault_dir),
        db_path=str(cfg.db_path),
    )


@app.get("/stats", response_model=Stats)
async def stats():
    cfg = get_settings()
    counts = database.get_stats(str(cfg.db_path))
    return Stats(
        source_count=counts["source_count"],
        chunk_count=counts["chunk_count"],
        token_count=counts["token_count"],
        model=cfg.model,
        num_ctx=cfg.num_ctx,
        ollama_reachable=await ollama_client.is_reachable(),
        whisper_model_path=str(cfg.whisper_model_dir),
    )


# ============================================================================ #
# Ingestion
# ============================================================================ #


@app.post("/ingest", response_model=IngestAccepted)
async def ingest(
    request: Request,
    file: UploadFile | None = File(default=None),
    url: str | None = Form(default=None),
):
    """Enqueue an ingestion job.

    Either `file` (multipart) or `url` (form field / JSON body) is required.
    Returns immediately with a job_id; the actual work runs in a background
    task. Subscribe to `/ingest/{job_id}/events` for progress.
    """
    # Also accept JSON body for URL ingest.
    if file is None and url is None:
        ct = request.headers.get("content-type", "")
        if "application/json" in ct:
            body = await request.json()
            url = body.get("url")
    if file is None and not url:
        raise HTTPException(status_code=400, detail="Provide a file or url.")

    if file is not None:
        location = file.filename or "(unnamed)"
        # Save to a temp file under cache_dir — extractors need a real path.
        cfg = get_settings()
        cfg.cache_dir.mkdir(parents=True, exist_ok=True)
        suffix = Path(file.filename or "").suffix or ".bin"
        tmp_path = cfg.cache_dir / f"{int(time.time() * 1000)}{suffix}"
        with tmp_path.open("wb") as f:
            shutil.copyfileobj(file.file, f)
        return await _enqueue_file(tmp_path, location)
    return await _enqueue_url(url)


async def _enqueue_file(path: Path, display_name: str) -> IngestAccepted:
    """Save the file to a stable location and enqueue an extract job."""
    cfg = get_settings()
    target = cfg.cache_dir / path.name
    if target.exists() and target.resolve() != path.resolve():
        # Avoid overwriting an existing file; use a unique name.
        target = cfg.cache_dir / f"{int(time.time() * 1000)}_{path.name}"
    if target.resolve() != path.resolve():
        shutil.move(str(path), str(target))
    source = Source(location=str(target), kind="file")
    # Determine type_hint from the extension.
    suffix = target.suffix.lower().lstrip(".")
    if suffix in ("txt", "md", "markdown"):
        source.type_hint = "text"
    job_id = progress.REGISTRY.create(display_name, source.type_hint or "text", str(target), "file")

    asyncio.create_task(_run_ingest(job_id, source, display_name))
    return IngestAccepted(job_id=job_id)


async def _enqueue_url(url: str) -> IngestAccepted:
    source = Source(location=url, kind="url")
    job_id = progress.REGISTRY.create(url, "url", url, "url")
    asyncio.create_task(_run_ingest(job_id, source, url))
    return IngestAccepted(job_id=job_id)


async def _run_ingest(job_id: str, source: Source, display_name: str) -> None:
    """Background orchestrator: detect → extract → hash → chunk → index.

    Each major step yields to the event loop with `await asyncio.sleep(0)` so
    the SSE consumer can drain the progress queue concurrently.
    """
    job = progress.REGISTRY.get(job_id)
    if job is None:
        return
    cfg = get_settings()
    db = cfg.db_path
    started = time.monotonic()

    try:
        # ---- 1. Detect & extract ---- #
        progress.make_event(job, status="extracting", progress=0.05)
        logger.info("orchestrator %s: extracting", job_id)
        await asyncio.sleep(0)  # let SSE consumer catch up
        try:
            result = await detect_and_dispatch(source)
        except Exception as exc:
            raise RuntimeError(f"extraction failed: {exc}") from exc

        if not result.pages:
            raise RuntimeError("extractor produced no pages")

        logger.info("orchestrator %s: extracted %d pages", job_id, len(result.pages))
        await asyncio.sleep(0)

        # ---- 2. Hash for dedup ---- #
        progress.make_event(job, status="cleaning", progress=0.4)
        cleaned = clean_pages(
            (p.page_number, p.text) for p in result.pages
        )

        joined = join_with_page_breaks(cleaned)
        # Iterate page texts for streaming hash (so the loop can yield).
        hash_input = [text for _, text in cleaned]
        hash_value = hash_text_streaming(hash_input)

        progress.make_event(job, progress=0.55)
        existing = database.get_source_by_hash(db, hash_value)
        if existing is not None:
            progress.make_event(
                job,
                status="already_indexed",
                progress=1.0,
                source_id=existing["id"],
                duration_s=time.monotonic() - started,
            )
            await asyncio.sleep(0)
            job.mark_done()
            return

        await asyncio.sleep(0)

        # ---- 3. Chunk ---- #
        progress.make_event(job, status="chunking", progress=0.6)
        chunks = chunk_pages(
            cleaned,
            target_tokens=cfg.chunk_target_tokens,
            min_tokens=cfg.chunk_min_tokens,
            max_tokens=cfg.chunk_max_tokens,
        )
        if not chunks:
            raise RuntimeError("chunker produced no chunks")

        await asyncio.sleep(0)

        # ---- 4. Index ---- #
        progress.make_event(job, status="indexing", progress=0.85)
        metadata = {
            **result.metadata,
            "ingest_via": source.kind,
            "original_location": source.location,
        }
        sid = database.insert_source(
            db,
            name=display_name,
            type_=job.source_type,
            hash_=hash_value,
            path=str(source.path) if source.path else None,
            url=source.url,
            metadata=metadata,
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
        database.insert_chunks(db, sid, chunk_records)

        total_tokens = sum(c["token_count"] for c in chunks)

        progress.make_event(
            job,
            status="done",
            progress=1.0,
            source_id=sid,
            chunk_count=len(chunks),
            token_count=total_tokens,
            duration_s=time.monotonic() - started,
        )
        logger.info("orchestrator %s: done", job_id)
        await asyncio.sleep(0)
    except Exception as exc:
        logger.exception("ingest job %s failed", job_id)
        progress.make_event(
            job,
            status="error",
            progress=1.0,
            error=str(exc),
            duration_s=time.monotonic() - started,
        )
    finally:
        job.mark_done()


@app.get("/ingest/{job_id}/events")
async def ingest_events(job_id: str):
    job = progress.REGISTRY.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="unknown job_id")
    return StreamingResponse(
        progress.sse_stream(job),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


# ============================================================================ #
# Sources
# ============================================================================ #


@app.get("/sources", response_model=list[SourceModel])
async def list_sources():
    cfg = get_settings()
    rows = database.list_sources(cfg.db_path)
    return [SourceModel(**_serialise_source(r)) for r in rows]


@app.delete("/sources/{source_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_source(source_id: str):
    cfg = get_settings()
    existing = database.get_source(cfg.db_path, source_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="unknown source")
    database.delete_source(cfg.db_path, source_id)


# ============================================================================ #
# Query
# ============================================================================ #


@app.post("/query/retrieve", response_model=RetrieveResponse)
async def query_retrieve(req: RetrieveRequest):
    cfg = get_settings()
    hits = query.retrieve_only(cfg.db_path, req.query, max_chunks=req.max_chunks)
    chunk_hits = [
        ChunkHit(
            chunk_id=h["chunk_id"],
            source_id=h["source_id"],
            source_name=h.get("source_name", ""),
            page_start=h.get("page_start"),
            page_end=h.get("page_end"),
            excerpt=h.get("excerpt", ""),
            score=h.get("score", 0.0),
            text=h.get("text") if req.include_text else None,
        )
        for h in hits
    ]
    sources = {
        h["source_id"]: h.get("source_name", "")
        for h in hits
    }
    src_models: list[SourceModel] = []
    for sid in sources:
        row = database.get_source(cfg.db_path, sid)
        if row:
            src_models.append(SourceModel(**_serialise_source(row)))
    return RetrieveResponse(chunks=chunk_hits, sources=src_models)


@app.post("/query")
async def query_vault(req: QueryRequest):
    """Stream a retrieval + LLM response as Server-Sent Events.

    Events emitted:
        data: {"event": "retrieval", "chunks": [...], "sources": [...]}
        data: {"event": "token", "token": "..."}
        data: {"event": "done", "citations": [...], "source_ids": [...]}

    If retrieval returns zero chunks, the assistant message is the locked
    NO_CONTEXT_REFUSAL and no LLM call is made.
    """
    cfg = get_settings()

    selected, ranked, truncated = query.retrieve_for_assembly(
        cfg.db_path,
        req.query,
        max_context_tokens=req.max_context_tokens,
        reserve_tokens=1024,
    )

    # Persist the user message immediately.
    user_msg_id = database.insert_message(
        cfg.db_path,
        role="user",
        content=req.query,
        query_params={
            "max_context_tokens": req.max_context_tokens,
            "model": req.model or cfg.model,
        },
    )

    if not selected:
        # No context. Stream refusal as the assistant message and finish.
        async def no_context_stream():
            yield progress.sse_format({
                "event": "retrieval",
                "chunks": [],
                "sources": [],
                "truncated": False,
            })
            yield progress.sse_format({
                "event": "token",
                "token": NO_CONTEXT_REFUSAL,
            })
            database.insert_message(
                cfg.db_path,
                role="assistant",
                content=NO_CONTEXT_REFUSAL,
                query_params={
                    "retrieved_chunk_ids": [],
                    "source_count": 0,
                    "model": req.model or cfg.model,
                    "message_id": user_msg_id,
                },
            )
            yield progress.sse_format({
                "event": "done",
                "citations": [],
                "source_ids": [],
            })

        return StreamingResponse(
            no_context_stream(),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    # Build LLM-bound chunks (subset of fields the prompt needs).
    context_chunks = [
        {
            "source_id": c["source_id"],
            "source_name": c.get("source_name", ""),
            "page_start": c.get("page_start"),
            "page_end": c.get("page_end"),
            "text": c["text"],
        }
        for c in selected
    ]
    user_prompt = build_user_prompt(req.query, context_chunks)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    async def event_stream():
        # 1. Retrieval summary
        retrieval_payload = {
            "event": "retrieval",
            "chunks": [
                {
                    "chunk_id": h["chunk_id"],
                    "source_id": h["source_id"],
                    "source_name": h.get("source_name", ""),
                    "page_start": h.get("page_start"),
                    "page_end": h.get("page_end"),
                    "excerpt": h.get("excerpt", ""),
                    "score": h.get("score", 0.0),
                }
                for h in ranked[:50]  # cap to 50 for UI
            ],
            "source_count": len({c["source_id"] for c in selected}),
            "truncated": truncated,
        }
        yield progress.sse_format(retrieval_payload).encode("utf-8")

        # 2. LLM stream
        parser = CitationStreamParser()
        collected_tokens: list[str] = []
        try:
            async for token in ollama_client.chat_stream(
                messages,
                model=req.model,
                num_ctx=req.max_context_tokens,
            ):
                cleaned, new_cits = parser.feed(token)
                collected_tokens.append(cleaned)
                payload = {
                    "event": "token",
                    "token": cleaned,
                }
                if new_cits:
                    payload["new_citations"] = new_cits
                yield progress.sse_format(payload).encode("utf-8")
        except ollama_client.OllamaError as exc:
            err_payload = {
                "event": "error",
                "message": str(exc),
            }
            yield progress.sse_format(err_payload).encode("utf-8")
            return

        full_text = "".join(collected_tokens)
        all_citations = parser.all()

        # 3. Persist assistant message
        database.insert_message(
            cfg.db_path,
            role="assistant",
            content=full_text,
            query_params={
                "retrieved_chunk_ids": [c.get("id") for c in selected if c.get("id")],
                "source_count": len({c["source_id"] for c in selected}),
                "model": req.model or cfg.model,
                "citations": all_citations,
                "message_id": user_msg_id,
                "truncated": truncated,
            },
        )

        # 4. Done
        done_payload = {
            "event": "done",
            "citations": all_citations,
            "source_ids": list({c["source_id"] for c in selected}),
        }
        yield progress.sse_format(done_payload).encode("utf-8")

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ============================================================================ #
# Chat history
# ============================================================================ #


@app.get("/chat/history", response_model=list[Message])
async def get_chat_history(limit: int = 200):
    cfg = get_settings()
    rows = database.list_messages(cfg.db_path, limit=limit)
    return [_message_from_row(r) for r in rows]


@app.delete("/chat/history", status_code=status.HTTP_204_NO_CONTENT)
async def clear_chat_history():
    cfg = get_settings()
    database.clear_messages(cfg.db_path)


# ============================================================================ #
# Helpers
# ============================================================================ #


def _serialise_source(row: dict) -> dict[str, Any]:
    """Coerce a DB row dict into the SourceModel shape."""
    out = dict(row)
    # Rename `type` (Python builtin) -> the schema name is also `type`.
    out["type"] = row.get("type") or row.get("type_") or "unknown"
    out["created_at"] = row.get("created_at")
    return out


def _message_from_row(row: dict) -> Message:
    params = row.get("query_params")
    if params:
        try:
            params = json.loads(params)
        except (TypeError, json.JSONDecodeError):
            params = None
    return Message(
        id=row["id"],
        role=row["role"],
        content=row["content"],
        created_at=row["created_at"],
        query_params=params,
    )