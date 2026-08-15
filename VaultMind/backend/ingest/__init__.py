"""Plugin registry for ingestion extractors.

Each format-specific extractor calls `register()` at import time. This
module imports each submodule to trigger registration. The Tauri shell, the
FastAPI surface, and the frontend never need to know which formats exist;
they consume the registry's `dispatch()`.

Adding a new format:
    1. Create `backend/ingest/<format>.py`.
    2. Define `extract(source: Source) -> ExtractionResult` and `register(registry)`.
    3. Add `from . import <format>` below.
    4. (Optional) Add URL schemes or extension mappings inside `register()`.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from backend.ingest.base import (
    ExtractorError,
    ExtractionResult,
    Page,
    Source,
)


# ============================================================================ #
# Registry
# ============================================================================ #


class PluginRegistry:
    """Holds all registered extractors and dispatches based on input type."""

    def __init__(self) -> None:
        self._by_type: dict[str, Callable[[Source], ExtractionResult]] = {}
        self._by_ext: dict[str, Callable[[Source], ExtractionResult]] = {}
        self._by_url_scheme: dict[str, Callable[[Source], ExtractionResult]] = {}

    # ---- registration ------------------------------------------------- #

    def register(
        self,
        source_type: str,
        fn: Callable[[Source], ExtractionResult],
        *,
        extensions: tuple[str, ...] = (),
    ) -> None:
        """Register an extractor for a source type and (optionally) file extensions."""
        if not isinstance(source_type, str) or not source_type:
            raise ValueError("source_type must be a non-empty string")
        if not callable(fn):
            raise TypeError(f"extractor for {source_type!r} is not callable")
        if source_type in self._by_type:
            raise ValueError(f"duplicate extractor registration for {source_type!r}")
        self._by_type[source_type] = fn
        for ext in extensions:
            ext_norm = ext.lower().lstrip(".")
            if ext_norm in self._by_ext:
                raise ValueError(f"duplicate extension registration: .{ext_norm}")
            self._by_ext[ext_norm] = fn

    def register_url(
        self,
        source_type: str,
        fn: Callable[[Source], ExtractionResult],
        *,
        schemes: tuple[str, ...] = (),
    ) -> None:
        """Register an extractor for URL schemes (e.g., 'youtube')."""
        if source_type not in self._by_type:
            raise ValueError(
                f"register_url({source_type!r}) requires register({source_type!r}) first"
            )
        for scheme in schemes:
            scheme_norm = scheme.lower().rstrip(":")
            if scheme_norm in self._by_url_scheme:
                raise ValueError(f"duplicate URL scheme registration: {scheme}")
            self._by_url_scheme[scheme_norm] = fn

    # ---- lookup ------------------------------------------------------- #

    def get(self, source_type: str) -> Callable[[Source], ExtractionResult]:
        if source_type not in self._by_type:
            raise ExtractorError(
                f"no extractor registered for {source_type!r}",
                source_kind=source_type,
                stage="dispatch",
            )
        return self._by_type[source_type]

    def list_types(self) -> list[str]:
        """Return registered source type names, sorted."""
        return sorted(self._by_type)

    def list_extensions(self) -> list[str]:
        """Return registered file extensions, sorted (without leading dot)."""
        return sorted(self._by_ext)

    # ---- dispatch ----------------------------------------------------- #

    def dispatch(self, source: Source) -> Callable[[Source], ExtractionResult]:
        """Pick the right extractor for a Source.

        Resolution order:
            1. Explicit `source.type_hint` (if set).
            2. URL scheme (for URL sources).
            3. File extension (for file sources).
            4. Fallback to "text" if the file has no known extension.
        """
        if source.type_hint:
            return self.get(source.type_hint)

        if source.kind == "url":
            url = source.url or ""
            host = url.lower()
            # Special-case well-known URLs.
            if "youtube.com" in host or "youtu.be" in host:
                return self.get("youtube")
            if host.startswith("http://") or host.startswith("https://"):
                return self.get("web_article")
            scheme = url.split(":", 1)[0].lower()
            fn = self._by_url_scheme.get(scheme)
            if fn is not None:
                return fn
            raise ExtractorError(
                f"no URL extractor registered for scheme {scheme!r}",
                source_kind="url",
                stage="dispatch",
            )

        # File source
        if source.path is None:
            raise ExtractorError(
                "file source has no path", source_kind="file", stage="dispatch"
            )
        ext = source.path.suffix.lower().lstrip(".")
        if ext in self._by_ext:
            return self._by_ext[ext]
        if not ext:
            return self.get("text")
        raise ExtractorError(
            f"no extractor registered for .{ext} files",
            source_kind="file",
            stage="dispatch",
        )


# Singleton registry. Importing submodules mutates this.
REGISTRY = PluginRegistry()


def register(source_type: str, fn, *, extensions: tuple[str, ...] = ()):
    """Convenience wrapper for the global registry."""
    REGISTRY.register(source_type, fn, extensions=extensions)


def register_url(source_type: str, fn, *, schemes: tuple[str, ...] = ()):
    """Convenience wrapper for the global registry."""
    REGISTRY.register_url(source_type, fn, schemes=schemes)


def get_extractor(source_type: str):
    """Return the extractor for a given source type."""
    return REGISTRY.get(source_type)


def dispatch(source: Source):
    """Return the extractor for a given source."""
    return REGISTRY.dispatch(source)


def detect_and_dispatch(source: Source) -> ExtractionResult:
    """Resolve the extractor and run it. Convenience for the orchestrator."""
    fn = dispatch(source)
    return fn(source)


# ============================================================================ #
# Submodule registrations — each submodule's `register()` is called here.
# ============================================================================ #

# Importing each submodule for its `register()` function, then calling it.
from . import text  # noqa: E402, F401

text.register(REGISTRY)

# Future extractors (Phase 3+):
# from . import pdf, docx, xlsx, pptx, epub, image, media, url, youtube  # noqa
# pdf.register(REGISTRY)
# ...


__all__ = [
    "ExtractorError",
    "ExtractionResult",
    "Page",
    "PluginRegistry",
    "REGISTRY",
    "Source",
    "detect_and_dispatch",
    "dispatch",
    "get_extractor",
    "register",
    "register_url",
]
