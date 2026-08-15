# Decision Log

Architectural Decision Records (ADR) for VaultMind. Newest first. Each entry captures one decision, its context, the choice made, and the consequences.

---

## ADR-006 — Drop semantic search from v0 retrieval

**Date:** 2026-08-15
**Status:** Accepted

**Context.** The XDA article the user linked as inspiration uses ChromaDB vector search. The user explicitly stated "The LLM should not rely on semantic search as it needs to be as accurate as possible." Embeddings-based retrieval trades exactness for paraphrase coverage, which is exactly the failure mode the user wants to avoid.

**Decision.** Retrieval in v0 is BM25 + phrase/NEAR boost on SQLite FTS5 only. No embedding model inference at runtime. `nomic-embed-text` may be pre-pulled as future-proofing but never queried.

**Consequences.**
- Retrieval is exact and reproducible; the LLM cannot hallucinate content from paraphrased but unrelated material.
- Synonym / paraphrase queries (e.g., "car" matching "automobile") will not match. Acceptable trade-off given the user's accuracy requirement.
- `nomic-embed-text` pull is optional; future v0.1+ can add semantic as a *complement* to BM25 (hybrid), never as a replacement.

**Reversibility.** Trivial — re-enable semantic by adding a hybrid retrieval path that unions BM25 hits with vector nearest-neighbors.

---

## ADR-005 — Whisper backend: OpenVINO GenAI (not faster-whisper)

**Date:** 2026-08-15
**Status:** Accepted

**Context.** The SPEC.md draft listed `faster-whisper` + `intel-extension-for-pytorch` for Whisper. faster-whisper is built on CTranslate2, which supports CPU and NVIDIA CUDA only — it has no Intel Arc backend. `intel-extension-for-pytorch` provides a SYCL path for Arc but the integration with faster-whisper is unofficial and fragile.

**Decision.** Use `openvino-genai` (≥ 2024.4) with `WhisperPipeline(device="GPU")`. Pre-converted OpenVINO IR models live in the `OpenVINO/speech-to-text` HuggingFace collection. Default model is `distil-whisper-large-v3-int4-ov` (INT4 quantized, ~750 MB).

**Consequences.**
- Native Intel GPU support; ~6× speedup vs CPU for the chosen model.
- WhisperPipeline API is simple; segmentation via ffmpeg `-ss`/`-t` before passing audio to the pipeline.
- First-call compile latency is ~30s on Arc (cached after first run).
- Falls back to CPU if `device="GPU"` fails at construction time.

**Reversibility.** None needed — OpenVINO GenAI is the only mature Arc path.

---

## ADR-004 — LLM model: qwen2.5:7b-instruct-q4_K_M

**Date:** 2026-08-15
**Status:** Accepted

**Context.** Need a 7B-class instruction-tuned model that fits in the 16 GB RAM budget and produces faithful, grounded answers.

**Decision.** Default is `qwen2.5:7b-instruct-q4_K_M` (~4.7 GB). Verified working on the target hardware at ~18 tok/s generation, leaving ~10 GB for OS + backend + context.

**Alternatives considered.**
- `qwen2.5:3b` (~3.3 GB) — smaller and faster but weaker at long-form reasoning; rejected as the default but available via config.
- `Llama-3.1-Nemotron-70B` — RAG-tuned but way too large for 16 GB; Ollama library does not ship a 7B/8B Nemotron-RAG variant.
- `nemotron-mini:4b` — RAG-tuned but smaller and less proven; available via config as opt-in.

**Consequences.** Users on hardware with discrete GPUs can bump to `qwen2.5:14b-q5_K_M` by editing `backend/config.py`.

---

## ADR-003 — Tauri 2.x spawns Python as a subprocess (no pyo3)

**Date:** 2026-08-15
**Status:** Accepted

**Context.** The Tauri shell needs to run the Python backend. Two options: (a) `pyo3` Python bindings embedded in Rust, (b) spawn the backend as a sidecar subprocess.

**Decision.** Use a sidecar subprocess. The backend ships as a PyInstaller-bundled `.exe` (`vaultmind-backend-x86_64-pc-windows-msvc.exe`) referenced by `tauri.conf.json → bundle.externalBin`.

**Rationale.**
- No Python C-API binding friction across Python versions.
- The Python backend can run standalone (for tests, dev mode, and CI) without Tauri.
- Streaming responses (SSE) bypass Tauri commands entirely; the frontend calls FastAPI directly via `fetch` — simpler and faster than proxying a stream through Rust.

**Consequences.**
- Startup adds ~250 ms–1 s for `/health` poll while the backend initializes.
- PyInstaller bundle is ~80 MB. Acceptable.
- Backend lifecycle is tied to the Tauri shell's lifecycle — closing the window SIGTERMs the subprocess.

---

## ADR-002 — SQLite FTS5 with `porter unicode61` + `prefix='2 3'`

**Date:** 2026-08-15
**Status:** Accepted

**Context.** Need a lexical retrieval layer that is local, fast, and produces exact, reproducible results. SQLite FTS5 with BM25 ranking is the canonical solution for this.

**Decision.**
- Tokenize with `porter unicode61` (English-oriented stemming + Unicode-aware tokenization + case folding).
- Enable `prefix='2 3'` so partial matches like `confi*` hit `configuration` and `configured`.
- Weight BM25 with title-vs-body weighting disabled in v0 (single `text` column); can be added later.
- Use external-content FTS5 with mandatory `INSERT/DELETE/UPDATE` triggers to keep the FTS index synchronized with the `chunks` table.
- Run `INSERT INTO chunks_fts(chunks_fts) VALUES ('integrity-check')` periodically to detect drift.

**Consequences.** Slightly larger FTS5 index (prefix='2 3' doubles size). Acceptable.

**Reversibility.** Re-tokenization is destructive — would require a re-ingest migration.

---

## ADR-001 — Plugin registry for ingestion extractors

**Date:** 2026-08-15
**Status:** Accepted

**Context.** Ingestion must support many file formats (PDF, DOCX, XLSX, PPTX, EPUB, TXT, MD, PNG, JPG, audio, video, web URLs, YouTube URLs) and the SPEC explicitly states "This software needs to be able to add more functionality in the future."

**Decision.** Implement a plugin registry in `backend/ingest/__init__.py`:
- `register(source_type: str, fn: Callable)` — adds an extractor.
- `get_extractor(source_type: str) -> Callable` — registry lookup.
- `detect_and_dispatch(source) -> ExtractionResult` — given a `Source`, picks and runs the right extractor.

Each extractor module calls `register()` at import time. `__init__.py` imports each submodule in alphabetical order to trigger registration. **No if/elif dispatch.**

**Consequences.**
- Adding a new format is one file + one import line in `__init__.py`.
- The Tauri shell, FastAPI surface, and frontend are decoupled from the set of formats — they consume the registry.
- Extractors must follow the `Extractor` protocol defined in `base.py`.

**Reversibility.** Trivial — a future major version could refactor to dynamic plugin discovery from `~/.vaultmind/plugins/` without breaking the surface.