"""Async streaming client for the local Ollama HTTP server.

Uses httpx with `stream=True` to forward tokens to the SSE handler without
buffering. Caller is responsible for handling the httpx timeouts.

The default model is set in `backend/config.py`. Callers can override via
the `model` parameter on a per-query basis.
"""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any

import httpx

from backend.config import get_settings


class OllamaError(Exception):
    """Wraps any failure reaching the Ollama server."""

    def __init__(self, message: str, *, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


async def is_reachable() -> bool:
    """Return True if Ollama is up and responding to /api/version."""
    cfg = get_settings()
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get(f"{cfg.ollama_url}/api/version")
            return r.status_code == 200
    except Exception:
        return False


async def get_version() -> str | None:
    """Return the Ollama version string, or None if not reachable."""
    cfg = get_settings()
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get(f"{cfg.ollama_url}/api/version")
            if r.status_code == 200:
                return r.json().get("version")
    except Exception:
        return None
    return None


async def chat_stream(
    messages: list[dict[str, str]],
    *,
    model: str | None = None,
    num_ctx: int | None = None,
    temperature: float | None = None,
) -> AsyncIterator[str]:
    """Yield text tokens from Ollama's chat endpoint.

    `messages` is a list of {role, content} dicts. The default system prompt
    is added by the FastAPI caller (see `prompts.SYSTEM_PROMPT`).

    `num_ctx` defaults to settings.num_ctx (8192). `temperature` defaults to
    settings.temperature (0.2).
    """
    cfg = get_settings()
    model = model or cfg.model
    num_ctx = num_ctx if num_ctx is not None else cfg.num_ctx
    temperature = temperature if temperature is not None else cfg.temperature

    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": True,
        "options": {
            "num_ctx": num_ctx,
            "temperature": temperature,
        },
    }

    timeout = httpx.Timeout(cfg.request_timeout_s, connect=10.0)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            async with client.stream(
                "POST",
                f"{cfg.ollama_url}/api/chat",
                json=payload,
            ) as response:
                if response.status_code != 200:
                    body = await response.aread()
                    raise OllamaError(
                        f"Ollama returned {response.status_code}: {body.decode('utf-8', errors='replace')[:200]}",
                        status_code=response.status_code,
                    )
                async for line in response.aiter_lines():
                    if not line:
                        continue
                    try:
                        chunk = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if chunk.get("done"):
                        return
                    msg = chunk.get("message") or {}
                    token = msg.get("content")
                    if token:
                        yield token
    except httpx.ConnectError as exc:
        raise OllamaError(
            f"cannot reach Ollama at {cfg.ollama_url}. Is `ollama serve` running?"
        ) from exc
    except httpx.TimeoutException as exc:
        raise OllamaError(
            f"Ollama request timed out after {cfg.request_timeout_s}s"
        ) from exc


async def chat_complete(
    messages: list[dict[str, str]],
    *,
    model: str | None = None,
    num_ctx: int | None = None,
    temperature: float | None = None,
) -> str:
    """Non-streaming variant. Returns the full response as a string."""
    out: list[str] = []
    async for token in chat_stream(
        messages,
        model=model,
        num_ctx=num_ctx,
        temperature=temperature,
    ):
        out.append(token)
    return "".join(out)