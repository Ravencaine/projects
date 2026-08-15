# VaultMind — AI Knowledge Vault
**Spec version:** 1.0 | **Date:** 2026-08-15 | **Author:** KRLSA

---

## 1. Vision & Philosophy

VaultMind is a **private, offline AI knowledge vault** that runs entirely on the user's laptop. You ingest documents, videos, web pages, and files of all major formats by dragging them into a drop zone. You query your vault through a chat interface and a dual-pane query view — both powered entirely by local LLMs, with zero cloud dependency.

The core design principle: **the LLM reasons over retrieved context, not over a ranked subset of it.** Retrieval must be exact and complete. The LLM cannot hallucinate facts that weren't in the ingested material because it only sees what was retrieved.

This is not a semantic search engine. It is a knowledge base that an LLM interrogates faithfully.

---

## 2. Target Machine

**KNOWLEDGEBOOK** — Intel Core Ultra 7 256V (Lunar Lake), 16 GB RAM, 953 GB NVMe SSD, Windows 11 Home, Intel Arc Graphics (for Whisper/ONNX acceleration only).

| Resource | Constraint |
|----------|-------------|
| RAM | 16 GB total — LLM + backend must fit alongside OS |
| VRAM | Integrated Arc — used for Whisper (oneAPI/ipex) and ONNX, NOT for Ollama |
| Ollama | CPU-only inference. 7B Q4_K_M model is the sweet spot. |
| Whisper | Arc-accelerated via Intel oneAPI / DirectML |
| Storage | ~619 GB free — room for models + vault |

---

## 3. Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                  Tauri Desktop Shell                     │
│  ┌──────────────────────────────────────────────────┐   │
│  │              HTML/CSS/JS Frontend                 │   │
│  │   [Ingestion Pane]   [Chat Pane]  [Query Pane]   │   │
│  └──────────────────────────────────────────────────┘   │
│                         │ IPC (Tauri commands)           │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Python FastAPI Backend               │   │
│  │  ┌─────────┐ ┌──────────┐ ┌─────────────────┐   │   │
│  │  │Ingester │ │ Query    │ │ Ollama Bridge  │   │   │
│  │  │(formats)│ │(FTS5→LLM)│ │  (local LLM)   │   │   │
│  │  └────┬────┘ └────┬─────┘ └────────┬────────┘   │   │
│  │       │           │                 │             │   │
│  │  ┌────▼───────────▼─────────────────▼────┐      │   │
│  │  │         SQLite + FTS5                   │      │   │
│  │  │   (chunks, metadata, BM25 index)       │      │   │
│  │  └──────────────────────────────────────────┘      │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Ollama (separate process)             │   │
│  │  • qwen2.5:7b-q4_K_M (LLM)                       │   │
│  │  • nomic-embed-text (embeddings only)            │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Whisper (CPU + Arc)                  │   │
│  │  • faster-whisper + Intel oneAPI                 │   │
│  │  • yt-dlp for web video download                 │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**No internet calls. No cloud. No API keys.**

---

## 4. UI / UX

### 4.1 Window Layout

Single resizable window (min 900×600). Three-pane layout:

```
┌────────────────────────────────────────────────────────────────┐
│  VaultMind                                         [─][□][×]  │
├──────────────┬─────────────────────────┬─────────────────────┤
│              │                         │                     │
│  INGESTION   │      CHAT VIEW          │   QUERY VIEW        │
│  PANE        │                         │                     │
│              │  Message history        │  [Text input]       │
│  ┌────────┐  │  with citations         │  [Search]           │
│  │ DROP   │  │                         │                     │
│  │  ZONE  │  │  User: [question]       │  Results panel      │
│  │        │  │  VaultMind: [answer]    │  • source chips     │
│  └────────┘  │                         │  • citation marks   │
│              │  [text input] [Send]    │  • chunk excerpts   │
│  [Drop files │                         │                     │
│   or URLs    │                         │  LLM Answer         │
│   here]      │                         │  panel              │
│              │                         │                     │
│  Progress /  │                         │                     │
│  file list   │                         │                     │
│              │                         │                     │
├──────────────┴─────────────────────────┴─────────────────────┤
│  Status: Ready │ Vault: 0 chunks │ Model: qwen2.5:7b         │
└────────────────────────────────────────────────────────────────┘
```

**Pane widths:**
- Ingestion pane: fixed 240px
- Chat pane: flex-grow (primary)
- Query pane: flex-grow (secondary)
- Chat and Query panes are visible simultaneously (side by side)

**Responsive:** Below 1100px width, Query pane collapses to a tab.

### 4.2 Ingestion Pane

- Large drag-and-drop zone with dashed border and icon
- Accepts: files (PDF, DOCX, XLSX, PPTX, TXT, MD, EPUB, PNG, JPG, MP3, MP4, AVI, MKV, WEBM) and URLs (YouTube, web articles)
- When URL is pasted, show URL type detection badge
- Progress list below drop zone:
  - Per-file: filename, status (queued/processing/done/error), progress bar
  - Click to expand: extracted chunk count, page count, duration (video)
- "Clear completed" button
- Status bar: total chunks indexed, total sources

### 4.3 Chat View

- Scrollable message history
- User messages: right-aligned, blue bubble
- VaultMind responses: left-aligned, dark bubble
- Each VaultMind message:
  - Formatted answer text
  - "Sources" expandable section: list of source chips (filename/page)
  - Citation marks [1] [2] inline with clickable links to chunk in Query pane
- Input: single-line text input + Send button + Enter key
- "Clear chat" button (top right of pane)

### 4.4 Query View

- Top: large text input (multiline, like a code editor)
- "Search Vault" button
- Below input: two tabs — **Results** | **LLM Answer**
- **Results tab:**
  - List of matching chunks, grouped by source document
  - Each chunk: source chip, page/timestamp, relevance snippet
  - Click chip → scroll to chunk; click chunk → highlight in Query pane
- **LLM Answer tab:**
  - Answer text with inline citations
  - "Show context" toggle: expands all retrieved chunks below answer
  - "Regenerate" button
- Both tabs update simultaneously when a query is issued

### 4.5 Visual Style

- **Theme:** Dark mode (system follows OS dark/light)
- **Font:** System sans-serif (Segoe UI on Windows)
- **Accent color:** `#6C63FF` (violet — used for buttons, active states, highlights)
- **Background:** `#1A1A2E` (dark navy)
- **Surface:** `#16213E` (slightly lighter, for cards/panes)
- **Text:** `#E8E8E8` (off-white)
- **Muted:** `#6B7280` (gray for metadata, timestamps)
- **Success:** `#10B981` | **Error:** `#EF4444` | **Warning:** `#F59E0B`

---

## 5. Ingestion Pipeline

### 5.1 Supported Formats

| Format | Extractor | Notes |
|--------|-----------|-------|
| PDF | PyMuPDF (fitz) | Text + page numbers. Images → pytesseract OCR. |
| DOCX | python-docx | Text + heading structure |
| XLSX | openpyxl | Sheet-by-sheet text extraction |
| PPTX | python-pptx | Text + slide numbers |
| TXT / MD | raw read | Direct ingestion |
| EPUB | epublib | Text extraction |
| PNG / JPG | pytesseract OCR | Image → text |
| MP3 / WAV / M4A | faster-whisper | Audio → transcript |
| MP4 / AVI / MKV / WEBM | faster-whisper | Video → transcript (audio track) |
| YouTube URL | yt-dlp → faster-whisper | Download + transcribe |
| Web article URL | requests + BeautifulSoup | Scrape article text |
| Web video URL | yt-dlp → faster-whisper | Download + transcribe |

### 5.2 Chunking

- **Target size:** 700 tokens (range 350–850)
- **Algorithm:** Recursive character split with heading/page awareness
- Pages or slides are respected — chunks don't span page boundaries
- Each chunk stores: `id, source_id, file_path, chunk_index, page_start, page_end, text, token_count, created_at`
- **Chunk metadata** (stored in SQLite alongside text):
  - `source_id` (UUID) — groups chunks by original file
  - `source_type` (pdf/docx/youtube/…)
  - `source_name` (filename or URL)
  - `page_range`, `char_count`, `token_count`, `sha256`

### 5.3 Ingestion Steps

1. **Detect type** — file extension or URL scheme
2. **Extract** — run appropriate extractor
3. **Clean** — strip headers/footers, fix broken lines, normalize whitespace
4. **Chunk** — heading/page-aware splitting
5. **Index** — write to SQLite FTS5 with BM25

### 5.4 Deduplication

- SHA-256 of full source text (not chunk text)
- If source hash already in DB → skip, report as "already indexed"
- User can force re-index via context menu

---

## 6. Query Pipeline

**Core principle: retrieve all relevant chunks, pass all to LLM. No top-K cutoff.**

### 6.1 Query Execution

1. Parse user query text
2. Build FTS5 BM25 query from query terms (handles quoted phrases, boolean)
3. Execute against all chunks — collect ALL matches (no limit)
4. Group matches by `source_id`
5. If any chunk from a source matches → include ALL chunks from that source (full recall)
6. Assemble chunk set into context window (truncate at model context limit if needed, oldest chunks first)
7. Build system prompt with context + user query
8. Stream response from Ollama
9. Stream to frontend, extract citation markers from response

### 6.2 Prompt Template

```
You are VaultMind, a private AI knowledge assistant. You answer questions
strictly from the provided context. Do not use any knowledge outside
the provided context. If the context does not contain the answer, say
"Based on the provided materials, I cannot find information about this."

CONTEXT:
---
[SOURCE: {source_name}, pages {page_range}]
{chunk_text}
---
[SOURCE: {source_name}, pages {page_range}]
{chunk_text}
---
...

QUESTION: {user_query}

Answer with inline citations in brackets, e.g. [Source: {source_name}, p.{page}].
```

### 6.3 Chat History

- Chat messages stored in SQLite (separate table from vault chunks)
- History loaded on startup, persisted across sessions
- Each message links to the query params + retrieved chunk set (for reproducibility)

---

## 7. Data Model

### 7.1 SQLite Schema

```sql
-- Sources: one row per ingested file/URL
CREATE TABLE sources (
    id TEXT PRIMARY KEY,           -- UUID
    name TEXT NOT NULL,            -- filename or URL
    type TEXT NOT NULL,            -- pdf, docx, youtube, web_article, etc.
    path TEXT,                     -- local path (null for URLs)
    url TEXT,                      -- original URL (null for local files)
    hash TEXT UNIQUE NOT NULL,     -- SHA-256 of full source text
    chunk_count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    metadata TEXT                  -- JSON: page_count, duration, etc.
);

-- Chunks: one row per text chunk
CREATE TABLE chunks (
    id TEXT PRIMARY KEY,           -- UUID
    source_id TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    text TEXT NOT NULL,
    token_count INTEGER,
    char_count INTEGER,
    created_at TEXT NOT NULL,
    FOREIGN KEY (source_id) REFERENCES sources(id)
);

-- FTS5 virtual table
CREATE VIRTUAL TABLE chunks_fts USING fts5(
    text,
    content='chunks',
    content_rowid='rowid',
    tokenize='porter unicode61'
);

-- Chat messages
CREATE TABLE messages (
    id TEXT PRIMARY KEY,
    role TEXT NOT NULL,            -- user | assistant
    content TEXT NOT NULL,
    query_params TEXT,            -- JSON: retrieved_chunk_ids, source_count
    created_at TEXT NOT NULL
);

-- Indexes
CREATE INDEX idx_chunks_source ON chunks(source_id);
CREATE INDEX idx_chunks_token_count ON chunks(token_count);
CREATE INDEX idx_messages_created ON messages(created_at);
```

---

## 8. Backend API (FastAPI)

### 8.1 Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/ingest` | Ingest a file (multipart) or URL (JSON body with `url`) |
| GET | `/sources` | List all indexed sources |
| DELETE | `/sources/{id}` | Delete a source and its chunks |
| POST | `/query` | Execute a query, return answer + sources |
| GET | `/query/retrieve` | Execute retrieval only (no LLM), return chunks |
| GET | `/chat/history` | Get chat message history |
| DELETE | `/chat/history` | Clear chat history |
| GET | `/stats` | Vault stats: chunk count, source count, model info |
| GET | `/health` | Health check + Ollama connectivity |

### 8.2 Request/Response Shapes

**POST /ingest (file)**
```
Form: file: <binary>
Response: { "source_id": "uuid", "name": "...", "chunk_count": N, "status": "done" }
```

**POST /ingest (URL)**
```
Body: { "url": "https://..." }
Response: { "source_id": "uuid", "name": "...", "chunk_count": N, "status": "done" }
```

**POST /query**
```
Body: { "query": "...", "max_context_tokens": 8192 }
Response (streaming): SSE with chunks of answer text + source citations
```

**GET /query/retrieve**
```
Query: ?q=...&group_by_source=true
Response: { "chunks": [...], "sources": [...] }
```

---

## 9. Tauri Integration

### 9.1 Tauri Commands (Rust → Python)

```rust
#[tauri::command] fn ingest_file(path: String) -> Result<IngestResult, String>
#[tauri::command] fn ingest_url(url: String) -> Result<IngestResult, String>
#[tauri::command] fn query_vault(query: String) -> Result<String, String>
#[tauri::command] fn retrieve(query: String) -> Result<Vec<Chunk>, String>
#[tauri::command] fn get_sources() -> Result<Vec<Source>, String>
#[tauri::command] fn delete_source(id: String) -> Result<(), String>
#[tauri::command] fn get_stats() -> Result<Stats, String>
#[tauri::command] fn get_chat_history() -> Result<Vec<Message>, String>
#[tauri::command] fn clear_chat() -> Result<(), String>
```

### 9.2 System Tray

- Minimize to tray (window hide)
- Tray icon with context menu:
  - "Open VaultMind" → show window
  - "Ingest clipboard URL" → read clipboard, detect URL, ingest
  - Separator
  - "Quit"

### 9.3 File Associations

- `.v vault` project files (future)

---

## 10. Setup & Installation

### 10.1 Ollama Setup

```bash
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama pull nomic-embed-text:latest
```

**Model choice rationale:** qwen2.5:7b Q4_K_M fits in ~5GB, runs on 16GB laptop CPU at ~15-20 tok/sec. If VRAM is later available (eGPU), swap to qwen2.5:14b Q5_K_M.

### 10.2 Whisper Setup

```bash
pip install faster-whisper
# Optional: Intel oneAPI for Arc acceleration
pip install intel-extension-for-pytorch
```

### 10.3 Python Dependencies

```
fastapi
uvicorn
pymupdf
python-docx
openpyxl
python-pptx
epublib
pytesseract
faster-whisper
yt-dlp
requests
beautifulsoup4
httpx
```

### 10.4 Tauri Build

- Tauri 2.x with Python backend via `pyo3` or subprocess bridge
- Frontend: vanilla HTML/CSS/JS (no framework — minimal footprint)
- Build target: Windows x64 `.exe`

---

## 11. File Structure

```
VaultMind/
├── SPEC.md
├── README.md
├── CLAUDE.md
├── src/                       # Rust (Tauri shell)
│   ├── main.rs
│   ├── lib.rs
│   └── commands.rs
├── frontend/                  # HTML/CSS/JS
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── icons/
├── backend/                   # Python FastAPI
│   ├── main.py
│   ├── config.py
│   ├── database.py            # SQLite + FTS5
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── pdf.py
│   │   ├── docx.py
│   │   ├── xlsx.py
│   │   ├── pptx.py
│   │   ├── text.py
│   │   ├── epub.py
│   │   ├── image.py
│   │   ├── audio.py
│   │   ├── video.py
│   │   ├── url.py
│   │   └── youtube.py
│   ├── chunker.py
│   ├── query.py
│   ├── ollama_client.py
│   └── models.py              # Pydantic schemas
├── models/                    # Ollama model storage
│   └── .gitkeep
└── vault/                     # SQLite DB + vault data
    └── .gitkeep
```

---

## 12. Out of Scope (v1)

- Multi-user / server mode
- Mobile companion app
- Cloud sync
- Plugin/extension system
- Version history on documents
- Annotation / highlighting
- Export to external formats

---

## 13. Open Questions

- [ ] Preferred chunk size — 700 tokens (spec default) or adjustable?
- [ ] Should chat history be per-vault or global?
- [ ] Whisper model size — `base` (fast, less accurate) vs `medium` (slower, better)? On Arc, both are viable.
- [ ] Include web scraping for article URLs? (Already spec'd — confirm.)
- [ ] Should the Query pane have a "filter by source" feature?
