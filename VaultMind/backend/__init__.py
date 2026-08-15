"""VaultMind backend package.

Layout:
    backend/
        main.py            FastAPI app + lifespan + routers
        __main__.py        uvicorn entry shim for PyInstaller bundle
        config.py          pydantic-settings (env-driven config)
        paths.py           cross-platform path helpers
        database.py        SQLite + FTS5 + triggers
        models.py          Pydantic request/response schemas
        chunker.py         700-token recursive splitter
        cleanup.py         header/footer strip + whitespace normalize
        query.py           BM25 + phrase/NEAR retrieval + context assembly
        ollama_client.py   httpx async streaming client to Ollama
        prompts.py         locked system prompt template
        citations.py       citation marker extraction
        progress.py        in-process pub/sub for SSE ingest events
        hashes.py          streaming SHA-256
        ingest/
            __init__.py    plugin registry (register, get_extractor, dispatch)
            base.py        Extractor protocol + Page/ExtractionResult dataclasses
            text.py        TXT + MD extractor (only one in Phase 1 MVP)
"""

__version__ = "0.1.0"