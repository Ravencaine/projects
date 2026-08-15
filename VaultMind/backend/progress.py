"""In-process pub/sub for background ingest progress.

A `Job` is created when `/ingest` is called. A background task runs the
extraction, periodically pushing events into the job's queue. The frontend
subscribes to `/ingest/{job_id}/events` (SSE) and receives those events.

Designed for a single-process FastAPI app — no Redis, no external broker.
"""

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from backend.database import new_id, utc_now_iso


@dataclass
class Job:
    """A single background ingestion job."""

    job_id: str
    source_name: str
    source_type: str
    location: str
    kind: str  # "file" or "url"
    created_at: str = field(default_factory=utc_now_iso)
    status: str = "queued"
    """queued | extracting | cleaning | chunking | indexing | done | already_indexed | error"""
    progress: float = 0.0
    chunk_count: int = 0
    token_count: int = 0
    error: str | None = None
    source_id: str | None = None
    duration_s: float = 0.0
    finished_at: str | None = None
    queue: asyncio.Queue[dict] = field(default_factory=asyncio.Queue)
    _done: asyncio.Event = field(default_factory=asyncio.Event)
    # Last event emitted before mark_done — replayed to late subscribers so
    # clients that connect after the job finished still see the terminal state.
    _final_event: dict | None = None

    def emit(self, event: dict) -> None:
        """Non-blocking push to the SSE queue. Used by the orchestrator."""
        # Always keep the last emitted event as a snapshot for late subscribers.
        # The queue is still used for live delivery.
        self._final_event = event
        try:
            self.queue.put_nowait(event)
        except asyncio.QueueFull:  # pragma: no cover
            pass

    def mark_done(self) -> None:
        self._done.set()


class JobRegistry:
    """Singleton holding all live jobs."""

    def __init__(self) -> None:
        self._jobs: dict[str, Job] = {}
        self._lock = asyncio.Lock()

    def create(self, source_name: str, source_type: str, location: str, kind: str) -> Job:
        jid = new_id()
        job = Job(
            job_id=jid,
            source_name=source_name,
            source_type=source_type,
            location=location,
            kind=kind,
        )
        self._jobs[jid] = job
        return jid

    def get(self, job_id: str) -> Job | None:
        return self._jobs.get(job_id)

    def all(self) -> list[Job]:
        return list(self._jobs.values())

    def remove(self, job_id: str) -> None:
        self._jobs.pop(job_id, None)


REGISTRY = JobRegistry()


def make_event(
    job: Job,
    *,
    status: str | None = None,
    progress: float | None = None,
    chunk_count: int | None = None,
    token_count: int | None = None,
    error: str | None = None,
    source_id: str | None = None,
    duration_s: float | None = None,
    extra: dict[str, Any] | None = None,
) -> dict:
    """Build a serialisable event payload for the SSE stream."""
    if status is not None:
        job.status = status
    if progress is not None:
        job.progress = progress
    if chunk_count is not None:
        job.chunk_count = chunk_count
    if token_count is not None:
        job.token_count = token_count
    if error is not None:
        job.error = error
    if source_id is not None:
        job.source_id = source_id
    if duration_s is not None:
        job.duration_s = duration_s
    if status in ("done", "already_indexed", "error"):
        job.finished_at = utc_now_iso()
    payload = {
        "job_id": job.job_id,
        "status": job.status,
        "progress": job.progress,
        "chunk_count": job.chunk_count,
        "token_count": job.token_count,
        "error": job.error,
        "source_id": job.source_id,
        "duration_s": job.duration_s,
        "ts": job.finished_at or utc_now_iso(),
    }
    if extra:
        payload.update(extra)
    # Push the event to the queue for live SSE consumers, and snapshot it so
    # late subscribers can replay the terminal state.
    job.emit(payload)
    return payload


def sse_format(event: dict) -> str:
    """Format an event dict as a Server-Sent Events frame.

    Each frame is `data: <json>\\n\\n`. The frontend's EventSource parses
    each `data:` line as a JSON object.
    """
    return f"data: {json.dumps(event)}\n\n"


async def sse_stream(job: Job, *, heartbeat_s: float = 15.0) -> AsyncIterator[bytes]:
    """Yield SSE frames for a job's progress queue.

    Streams events until the job sets its `_done` event. Includes a periodic
    heartbeat to keep the connection alive through corporate proxies.

    If the job is already done when a client subscribes (late subscriber),
    replays the snapshot of the last terminal event once and exits.
    """
    if job._done.is_set():
        if job._final_event is not None:
            yield sse_format(job._final_event).encode("utf-8")
        return

    while True:
        try:
            # Race: get event with timeout so we can emit heartbeats.
            event = await asyncio.wait_for(job.queue.get(), timeout=heartbeat_s)
        except asyncio.TimeoutError:
            # Heartbeat
            yield b": heartbeat\n\n"
            continue
        yield sse_format(event).encode("utf-8")
        if job._done.is_set() and job.queue.empty():
            return