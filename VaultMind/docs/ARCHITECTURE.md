# Architecture

This document is the implementation-facing mirror of [`SPEC.md`](../SPEC.md) §3. Read `SPEC.md` first for the design rationale; this page covers the data flow and module boundaries.

## Process topology

```
┌────────────────────────────────────────────────────────────────────┐
│ Windows 11 host                                                     │
│                                                                    │
│  ┌──────────────────┐         ┌──────────────────────────────┐    │
│  │ Tauri shell      │  IPC    │ Python FastAPI backend       │    │
│  │ (Rust, src-tauri)│ ◄─────► │ (uvicorn, backend/main.py)   │    │
│  │                  │         │                              │    │
│  │  Spawns backend  │         │  ├─ /ingest     (multipart,  │    │
│  │  as subprocess   │         │  │              JSON URL)    │    │
│  │  on startup      │         │  ├─ /sources    (CRUD)       │    │
│  │                  │         │  ├─ /query      (SSE stream) │    │
│  │  Owns window,    │         │  ├─ /query/retrieve (JSON)  │    │
│  │  tray, system    │         │  ├─ /chat/history (CRUD)    │    │
│  │  file assoc      │         │  └─ /stats, /health         │    │
│  └──────────────────┘         └──────────────────────────────┘    │
│         │                                  │                       │
│         │ Direct fetch (SSE)               │ HTTP                  │
│         ▼                                  ▼                       │
│  ┌──────────────────┐         ┌──────────────────────────────┐    │
│  │ Frontend         │         │ Ollama (separate process)    │    │
│  │ (HTML/CSS/JS in  │         │ localhost:11434              │    │
│  │  frontend/)      │         │ qwen2.5:7b-instruct-q4_K_M   │    │
│  └──────────────────┘         │ (CPU-only inference)         │    │
│                               └──────────────────────────────┘    │
│                                                                    │
│                               ┌──────────────────────────────┐    │
│                               │ OpenVINO GenAI Whisper       │    │
│                               │ models/whisper/distil-       │    │
│                               │   whisper-large-v3-int4-ov   │    │
│                               │ device=GPU → Arc 140V        │    │
│                               └──────────────────────────────┘    │
│                                                                    │
│                               ┌──────────────────────────────┐    │
│                               │ SQLite + FTS5                │    │
│                               │ vault/vaultmind.db           │    │
│                               │  sources / chunks / FTS5     │    │
│                               │  / messages                  │    │
│                               └──────────────────────────────┘    │
└────────────────────────────────────────────────────────────────────┘
```

## Data flow

### Ingestion (drop a file)

```
Frontend                Tauri shell              FastAPI              SQLite           Extractor
────────                ───────────              ────────             ──────           ─────────
drag-drop                                                                              
  │                                                                                    
  ▼                                                                                    
  Tauri command:                                                                       
   ingest_file(path) ─────────► POST /ingest (multipart)                              
                                  │                                                    
                                  │ enqueue job_id                                   
                                  ◄─────── { job_id, status: "queued" }               
                                  │                                                    
                                  │ BackgroundTask starts                            
                                  │   detect_and_dispatch() ──────────────────────►  pdf.py, docx.py, …
                                  │   extract() → [Page(text, page_no)]              
                                  │   hash streaming SHA-256                         
                                  │   clean, chunk                                   
                                  │   ─────── INSERT sources / chunks ──────────►   (FTS5 triggers fire)
                                  │                                                    
                                  │ SSE events ◄──── progress events                 
                                  │                                                    
  EventSource('/ingest/{id}/events')                                                  
  progress bar updates                                                                 
```

### Query (ask a question)

```
Frontend              FastAPI               SQLite              Ollama
────────              ────────              ──────              ──────
POST /query (SSE)
  query="…"
  │   _build_match()  → FTS5 MATCH expr
  │   SELECT top 500  ──────────►  bm25() ranking, snippet()
  │   fan-out full-source recall
  │   assemble context (≤ num_ctx - 1024 tokens)
  │   build prompt with locked SYSTEM template
  │   POST /api/chat (stream) ─────────────────────►  qwen2.5:7b
  │                                                        │
  │   ◄──────────── token chunks (SSE) ────────────────────┘
  ▼
render tokens, parse [Source: x, p.N] markers, append to bubble
```

## Module boundaries

### Backend (`backend/`)

| File | Responsibility |
|------|----------------|
| `main.py` | FastAPI app, lifespan, routers, `/health` |
| `config.py` | Pydantic settings (paths, model name, num_ctx, chunk size) |
| `database.py` | SQLite connection, schema bootstrap, FTS5 triggers, pragmas |
| `models.py` | Pydantic schemas (IngestResult, Chunk, Source, Message, QueryRequest) |
| `chunker.py` | 700-token recursive splitter, page/heading-aware |
| `cleanup.py` | Header/footer strip, whitespace normalize, hyphenated-newline fix |
| `query.py` | BM25 + phrase/NEAR query construction, full-source recall, context assembly |
| `ollama_client.py` | Async httpx streaming client to `localhost:11434`, `num_ctx` enforcement |
| `prompts.py` | Locked system prompt template |
| `citations.py` | Citation marker extraction from streaming tokens |
| `progress.py` | In-memory job registry + SSE broadcaster for ingest progress |
| `hashes.py` | Streaming SHA-256 over extracted text |
| `paths.py` | Cross-platform path helpers |
| `__main__.py` | uvicorn entry shim (for PyInstaller bundle) |

### Ingest plugin registry (`backend/ingest/`)

| File | Responsibility |
|------|----------------|
| `__init__.py` | `register(source_type, fn)`, `get_extractor(source_type)`, `detect_and_dispatch()` |
| `base.py` | `Extractor` protocol, `Page`, `ExtractionResult` dataclasses |
| `pdf.py` | PyMuPDF + pytesseract fallback for scanned pages |
| `docx.py` | python-docx paragraph + heading iter |
| `xlsx.py` | openpyxl sheet-by-sheet |
| `pptx.py` | python-pptx slide-by-slide |
| `text.py` | TXT / MD with `chardet` encoding detection |
| `epub.py` | ebooklib + BeautifulSoup (chapter-by-chapter via spine walk) |
| `image.py` | Pillow EXIF orientation correction + pytesseract |
| `media.py` | Audio + video: `ffmpeg` extract → OpenVINO Whisper |
| `url.py` | Web article: `requests` + `readability-lxml` |
| `youtube.py` | YouTube URL: `yt-dlp` → `ffmpeg` → OpenVINO Whisper |

**Plugin contract:** each extractor module calls `register(source_type, fn)` at import time. `__init__.py` imports each submodule in alphabetical order, triggering registration. Adding a new format is one file + one import line in `__init__.py`.

### Tauri shell (`src-tauri/src/`)

| File | Responsibility |
|------|----------------|
| `main.rs` | Window setup, subprocess spawn, health-check, lifecycle |
| `lib.rs` | Tauri builder, command registration |
| `commands.rs` | `#[tauri::command]` fns (thin HTTP proxies to FastAPI) |
| `backend.rs` | Subprocess manager (spawn, health-ping, kill on exit) |
| `tray.rs` | System tray icon + menu |
| `state.rs` | `AppState` struct (backend URL, subprocess handle) |

### Frontend (`frontend/`)

| File | Responsibility |
|------|----------------|
| `index.html` | Three-pane layout, dark theme |
| `styles.css` | CSS vars from SPEC §4.5, flex/grid layout |
| `app.js` | View controllers, mount logic |
| `api.js` | `fetch` wrapper for FastAPI |
| `sse.js` | `EventSource` + `ReadableStream` SSE helpers |
| `ingest.js` | Drag-and-drop zone, URL paste, progress list |
| `chat.js` | Message history, send, citation rendering |
| `query.js` | Search input, results tab, LLM answer tab |
| `citations.js` | `[Source: x, p.N]` marker parser → clickable chips |

## RAM budget (16 GB ceiling)

| Process | Idle | Active | Notes |
|---------|------|--------|-------|
| Windows 11 OS | ~4 GB | ~4 GB | |
| Ollama (qwen2.5:7b Q4_K_M) | ~4.7 GB | ~5 GB | resident |
| FastAPI backend | ~200 MB | ~500 MB | peaks during ingestion |
| Whisper (INT4 model + activation) | 0 MB | ~1 GB | only during media transcription |
| Frontend (Tauri WebView) | ~300 MB | ~500 MB | |
| **Total typical** | **~9.2 GB** | **~11 GB** | leaves ~5 GB for file caches |

Rule: **never run Whisper and Ollama concurrently.** Segment audio into ≤10-minute chunks so the total pipeline fits the budget.

## Extensibility points

The plugin registry under `backend/ingest/` is the primary extension surface. To add a new format:

1. Create `backend/ingest/<format>.py`.
2. Define an extractor function matching the `Extractor` protocol.
3. Call `register("<format>", extractor_fn)` at module top.
4. Add `from . import <format>` to `backend/ingest/__init__.py`.

The Tauri shell, FastAPI surface, and frontend don't need to change — they consume the registry's `detect_and_dispatch()` output.

Future v0.1+ extensions (each is a separate ADR):
- Vector retrieval as a complement to BM25 (not a replacement — see CLAUDE.md RULE-VM-1).
- Multi-vault support (per-vault DB).
- Custom prompts / system prompt overrides.
- Per-source chunk-size override.