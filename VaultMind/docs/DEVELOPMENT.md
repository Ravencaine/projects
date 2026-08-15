# Development

## Quick start

Two terminals in `VaultMind/`:

**Terminal 1 — backend:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn backend.main:app --port 8765 --reload
```

**Terminal 2 — Tauri shell:**
```bash
cargo install tauri-cli --version "^2.0"
cargo tauri dev
```

The Tauri window mounts after the FastAPI `/health` endpoint returns 200. Backend logs are visible in terminal 1; frontend console (DevTools) is openable from the Tauri window with `Ctrl+Shift+I` (or via the tray menu).

## Environment variables

The backend reads configuration from environment variables (loaded via `pydantic-settings`). Defaults are appropriate for local development; override as needed.

| Variable | Default | Description |
|----------|---------|-------------|
| `VAULTMIND_VAULT_DIR` | `<repo>/vault` | SQLite DB + cache directory |
| `VAULTMIND_MODEL` | `qwen2.5:7b-instruct-q4_K_M` | Ollama model name |
| `VAULTMIND_NUM_CTX` | `8192` | Context window size |
| `VAULTMIND_OLLAMA_URL` | `http://localhost:11434` | Ollama HTTP endpoint |
| `VAULTMIND_WHISPER_MODEL` | `OpenVINO/distil-whisper-large-v3-int4-ov` | Whisper IR model |
| `VAULTMIND_WHISPER_DEVICE` | `GPU` | OpenVINO device string |
| `VAULTMIND_CHUNK_TARGET_TOKENS` | `700` | Chunk size target |
| `VAULTMIND_LOG_LEVEL` | `INFO` | Python logging level |

## Per-phase verification

After completing each implementation phase, run the matching verification script. They are deterministic and exit non-zero on failure.

```bash
python scripts/verify_phase0.py     # repo structure + CLAUDE.md presence
python scripts/verify_phase1.py     # MVP: ingest → query → streamed answer
python scripts/verify_phase2.py     # Tauri shell + frontend boot
python scripts/verify_phase3.py     # text formats (PDF/DOCX/XLSX/PPTX/EPUB)
python scripts/verify_phase4.py     # Whisper (audio, video, YouTube)
python scripts/verify_phase5.py     # image OCR
python scripts/verify_phase6.py     # production build
```

## Troubleshooting

### "Ollama is not running"

The backend health check failed at `GET http://localhost:11434/api/version`. Start Ollama manually:

```bash
ollama serve
```

Or install it: `winget install Ollama.Ollama`.

### "OpenVINO model not found at models/whisper/…"

Run `scripts/bootstrap.ps1` to download the OpenVINO Whisper IR. Or manually:

```python
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="OpenVINO/distil-whisper-large-v3-int4-ov",
    local_dir="models/whisper/distil-whisper-large-v3-int4-ov",
)
```

### "Tesseract not found" when ingesting a scanned PDF or image

Install Tesseract:

```bash
winget install UB-Mannheim.TesseractOCR
```

Restart the backend after install.

### "PyMuPDF can't open a PDF"

Some PDFs are encrypted or have non-standard structure. The ingestion error will surface with a stage + message; the source is not indexed.

### Backend subprocess doesn't shut down on window close

The Tauri shell sends SIGTERM and gives a 5-second grace period. If the backend is mid-ingestion, wait — closing mid-ingest will leave the SQLite DB in a clean state (each ingestion is a single transaction).

### RAM ceiling (16 GB) hit during heavy ingest

The backend pauses Whisper if Ollama is actively generating. If both are unavoidable (e.g., a long video transcription while a chat query is in flight), reduce `num_ctx` to 4096 in `backend/config.py` to free ~1.5 GB.

## Adding a new ingest format

1. Create `backend/ingest/<format>.py`.
2. Implement an `extract(source: Source) -> ExtractionResult` function matching the `Extractor` protocol in `base.py`.
3. At module top, call `register("<format>", extract)`.
4. Add `from . import <format>` to `backend/ingest/__init__.py`.

No other code changes are needed. The Tauri shell, FastAPI surface, and frontend all consume the registry dynamically.

## Adding a new ADR

Edit `docs/DECISIONS.md`. ADRs are append-only — never delete or rewrite a previous ADR. Newest entry at the top.

## Code style

- **Python:** `ruff check` + `ruff format`. Type hints on public functions. `from __future__ import annotations` in new modules.
- **Rust:** `cargo fmt` + `cargo clippy -- -D warnings`.
- **Frontend:** vanilla — no bundler, no transpiler. ES modules (`type="module"`).

## Testing

```bash
pytest tests/ -q
```

Fixtures live under `tests/data/`.