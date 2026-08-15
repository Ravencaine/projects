"""Pydantic schemas for VaultMind's FastAPI surface.

All request/response shapes live here. Keep them flat and serializable.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# ============================================================================ #
# Ingestion
# ============================================================================ #


class IngestAccepted(BaseModel):
    """Returned by POST /ingest immediately after job enqueue."""

    model_config = ConfigDict(extra="forbid")

    job_id: str = Field(..., description="Background job identifier.")
    status: Literal["queued"] = "queued"


class IngestResult(BaseModel):
    """Final result for an ingestion job (also stored in job registry)."""

    model_config = ConfigDict(extra="forbid")

    job_id: str
    source_id: str | None = None
    name: str
    type: str
    status: Literal["done", "already_indexed", "error"]
    chunk_count: int = 0
    token_count: int = 0
    error: str | None = None
    duration_s: float = 0.0
    created_at: datetime


# ============================================================================ #
# Sources
# ============================================================================ #


class Source(BaseModel):
    """One row of the `sources` table."""

    model_config = ConfigDict(extra="forbid")

    id: str
    name: str
    type: str
    path: str | None = None
    url: str | None = None
    hash: str
    chunk_count: int = 0
    token_count: int = 0
    created_at: datetime
    metadata: dict | None = None


# ============================================================================ #
# Query
# ============================================================================ #


class ChunkHit(BaseModel):
    """A single retrieved chunk (also serialised in QueryResponse.chunks)."""

    model_config = ConfigDict(extra="forbid")

    chunk_id: str
    source_id: str
    source_name: str
    page_start: int | None = None
    page_end: int | None = None
    excerpt: str
    score: float
    text: str | None = Field(
        default=None,
        description="Full chunk text (only present in retrieval-only responses).",
    )


class RetrieveRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(..., min_length=1, max_length=4096)
    max_chunks: int = Field(default=500, ge=1, le=5000)
    include_text: bool = Field(
        default=False,
        description="If true, include full chunk text in the response (use for /query/retrieve).",
    )


class RetrieveResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    chunks: list[ChunkHit]
    sources: list[Source]
    truncated: bool = Field(
        default=False,
        description="True if context was truncated to fit num_ctx - 1024.",
    )


class QueryRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(..., min_length=1, max_length=4096)
    max_context_tokens: int = Field(default=8192, ge=512, le=16384)
    model: str | None = Field(
        default=None,
        description="Override the default Ollama model for this query only.",
    )


# ============================================================================ #
# Chat history
# ============================================================================ #


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    role: Literal["user", "assistant"]
    content: str
    created_at: datetime
    query_params: dict | None = None


# ============================================================================ #
# Stats
# ============================================================================ #


class Stats(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_count: int
    chunk_count: int
    token_count: int
    model: str
    num_ctx: int
    ollama_reachable: bool
    whisper_model_path: str


# ============================================================================ #
# Health
# ============================================================================ #


class Health(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["ok", "degraded"]
    ollama_reachable: bool
    ollama_model: str
    whisper_model: str
    vault_dir: str
    db_path: str