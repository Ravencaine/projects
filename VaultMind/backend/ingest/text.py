"""TXT and Markdown text extractor.

The only extractor in Phase 1 MVP. Reads UTF-8 (or detected encoding) text
and splits on form-feed (`\f`) for per-page boundaries. Heading-aware
chunking is handled at the chunker level.
"""

from __future__ import annotations

from pathlib import Path

from backend.ingest.base import ExtractorError, ExtractionResult, Page, Source


async def extract(source: Source) -> ExtractionResult:
    """Read a TXT or MD file. One page per form-feed block."""
    if source.kind != "file" or source.path is None:
        raise ExtractorError(
            "text extractor requires a local file path",
            source_kind=source.kind,
            stage="extract",
        )
    path = source.path
    if not path.exists():
        raise ExtractorError(
            f"file not found: {path}", source_kind="file", stage="extract"
        )

    raw = _read_text(path)
    blocks = raw.split("\f") if "\f" in raw else [raw]
    pages = [
        Page(text=block.strip(), page_number=i + 1)
        for i, block in enumerate(blocks)
        if block.strip()
    ]
    if not pages:
        raise ExtractorError(
            "file is empty or unreadable",
            source_kind="file",
            stage="extract",
        )
    return ExtractionResult(
        pages=pages,
        metadata={
            "encoding": _detect_encoding(path),
            "size_bytes": path.stat().st_size,
        },
    )


def _read_text(path: Path) -> str:
    """Read with UTF-8 first, then chardet fallback, then latin-1."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        pass
    try:
        import chardet

        raw = path.read_bytes()
        detected = chardet.detect(raw)
        return raw.decode(detected.get("encoding") or "utf-8", errors="replace")
    except Exception:
        return path.read_bytes().decode("latin-1", errors="replace")


def _detect_encoding(path: Path) -> str:
    try:
        import chardet

        with path.open("rb") as f:
            sample = f.read(65536)
        return chardet.detect(sample).get("encoding") or "utf-8"
    except Exception:
        return "utf-8"


# Plugin registry hook. Imported by `backend/ingest/__init__.py`.
def register(registry) -> None:
    """Register this extractor with the plugin registry."""
    registry.register("text", extract, extensions=(".txt", ".md", ".markdown"))
    registry.register_url("text", extract, schemes=("file",))
