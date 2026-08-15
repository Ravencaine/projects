"""Plugin registry tests.

Verifies register / dispatch / list_types / list_extensions behaviour.
"""

from __future__ import annotations

import pytest

from backend.ingest import REGISTRY, PluginRegistry, Source, dispatch


def test_text_extractor_registered():
    """The text extractor should be present after import."""
    assert "text" in REGISTRY.list_types()
    assert "txt" in REGISTRY.list_extensions()
    assert "md" in REGISTRY.list_extensions()


def test_dispatch_by_extension():
    src = Source(location="/tmp/foo.txt", kind="file")
    fn = dispatch(src)
    assert callable(fn)


def test_dispatch_by_url_http():
    src = Source(location="https://example.com/article", kind="url")
    # web_article is not registered in Phase 1; expect a clear error.
    with pytest.raises(Exception) as exc:
        dispatch(src)
    assert "web_article" in str(exc.value).lower() or "scheme" in str(exc.value).lower()


def test_dispatch_unknown_extension():
    src = Source(location="/tmp/foo.xyz", kind="file")
    with pytest.raises(Exception) as exc:
        dispatch(src)
    assert "no extractor" in str(exc.value).lower()


def test_dispatch_with_explicit_type_hint():
    src = Source(location="/tmp/somefile.bin", kind="file", type_hint="text")
    fn = dispatch(src)
    assert callable(fn)


def test_duplicate_registration_rejected():
    reg = PluginRegistry()
    reg.register("foo", lambda s: None)
    with pytest.raises(ValueError):
        reg.register("foo", lambda s: None)


def test_duplicate_extension_rejected():
    reg = PluginRegistry()
    reg.register("foo", lambda s: None, extensions=(".bar",))
    with pytest.raises(ValueError):
        reg.register("baz", lambda s: None, extensions=(".bar",))
