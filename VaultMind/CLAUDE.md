# VaultMind — Architectural Rules

VaultMind is a private, offline AI knowledge vault. The rules below are non-negotiable.

## Non-negotiable constraints

- **RULE-VM-1: No semantic search in v0.** Retrieval is BM25 + phrase/NEAR boost only
  on SQLite FTS5. Do not add vector embeddings, sentence-transformers, FAISS, or any
  ANN library to the retrieval path. `nomic-embed-text` may be pulled but must never
  be used at runtime.
- **RULE-VM-2: LLM context is only retrieved chunks.** Context assembly contains only
  chunks returned by `query.retrieve()` plus the locked system prompt. No examples,
  no injected knowledge.
- **RULE-VM-3: Zero cloud.** Network calls only at ingestion time for explicit URL /
  YouTube download paths. No analytics, telemetry, CDN, or font fetches.
- **RULE-VM-4: Whisper backend is OpenVINO GenAI.** Not faster-whisper, not
  transformers, not whisper.cpp. Use `openvino_genai.WhisperPipeline` with the
  `distil-whisper-large-v3-int4-ov` model.
- **RULE-VM-5: Ollama is CPU-only.** Never target a GPU device string. Call Ollama at
  `http://localhost:11434`. Default model is `qwen2.5:7b-instruct-q4_K_M`.
- **RULE-VM-6: 16 GB RAM is the ceiling.** `num_ctx=8192` is the safe max. Never run
  Whisper concurrently with Ollama generation. Segment long audio into ≤10-min chunks.
- **RULE-VM-7: SHA-256 dedup at source level.** Compute hash over full extracted text
  (not chunk text). Skip ingestion if hash exists; expose force-reindex.
- **RULE-VM-8: Plugin registry for extractors.** Each format in `backend/ingest/<fmt>.py`
  registers itself via `register(fmt, fn)` at import time. `__init__.py` imports each
  submodule to trigger registration. No if/elif dispatch.
- **RULE-VM-9: Tauri 2.x spawns Python as a subprocess.** No pyo3. Backend is a
  PyInstaller-bundled `.exe` sidecar at `src-tauri/binaries/`. Tauri waits for
  FastAPI `/health` before mounting the window.
- **RULE-VM-10: All long-running work is background.** Tauri commands return a
  `job_id` immediately. Frontend subscribes to SSE for progress. No sync ingestion.
- **RULE-VM-11: Streaming responses are SSE.** `/query` is `text/event-stream`. Tauri
  proxies the stream to the frontend via direct `fetch` + ReadableStream — not via
  Tauri commands.
- **RULE-VM-12: Pins.** Python 3.12, Tauri 2.x, FastAPI ≥ 0.115, Ollama ≥ 0.4,
  OpenVINO GenAI ≥ 2024.4.

## Working in this repo

- Backend lives in `backend/`. Frontend is vanilla — no Node bundler in v0.
- Tauri serves `frontend/` directly.
- Run `python scripts/verify_phase{N}.py` after each phase.
- Architectural decisions go in `docs/DECISIONS.md` (ADR format).

## Conventions

- Python: 4-space indent, type hints on public functions, `from __future__ import
  annotations` in new modules.
- Rust: stable toolchain ≥ 1.82, `cargo fmt` + `cargo clippy` clean.
- Frontend: vanilla HTML/CSS/JS. No bundler, no transpiler. ES modules only.
- Commits: conventional commits (`feat:`, `fix:`, `chore:`, `docs:`).