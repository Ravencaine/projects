"""Extractor protocol + dataclasses for the plugin registry.

Every format-specific extractor returns an `ExtractionResult` containing a
list of `Page` objects. The registry's `detect_and_dispatch()` picks the
right extractor based on the Source's URI or path type.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal, Protocol

SourceType = Literal[
    "text", "pdf", "docx", "xlsx", "pptx", "epub",
    "image", "audio", "video", "youtube", "url", "web_article",
]


@dataclass
class Source:
    """A source to be ingested. Either `path` or `url` is set, not both.

    Not frozen: callers (the FastAPI orchestrator) may set `type_hint` after
    construction based on extension detection.
    """

    location: str
    kind: Literal["file", "url"]
    type_hint: str | None = None

    @property
    def path(self) -> Path | None:
        return Path(self.location) if self.kind == "file" else None

    @property
    def url(self) -> str | None:
        return self.location if self.kind == "url" else None


@dataclass
class Page:
    """A single page (or equivalent) of extracted text."""

    text: str
    page_number: int | None = None
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExtractionResult:
    """The full output of an extractor."""

    pages: list[Page]
    metadata: dict[str, Any] = field(default_factory=dict)
    media_path: str | None = None

    @property
    def joined_text(self) -> str:
        """Concatenate page texts with newlines, suitable for hashing."""
        return "\n".join(p.text for p in self.pages)


class Extractor(Protocol):
    """Protocol every extractor must satisfy."""

    async def __call__(self, source: Source) -> ExtractionResult: ...


class ExtractorError(Exception):
    """Wraps any failure raised during extraction. Includes the source kind."""

    def __init__(self, message: str, *, source_kind: str, stage: str) -> None:
        super().__init__(message)
        self.source_kind = source_kind
        self.stage = stage
