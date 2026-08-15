"""Shared test fixtures.

Tests use a temporary DB in pytest's tmp_path and override env vars so the
settings singleton picks them up. Run with:
    pytest tests/ -q
"""

from __future__ import annotations

import os
from collections.abc import Generator
from pathlib import Path

import pytest

from backend import database


@pytest.fixture
def vault_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """A vault directory with the standard subfolders + an env override."""
    d = tmp_path / "vault"
    (d / "downloads").mkdir(parents=True)
    (d / "audio").mkdir()
    (d / ".cache").mkdir()
    os.environ["VAULTMIND_VAULT_DIR"] = str(d)
    # Reset the cached settings singleton so the env var is picked up.
    from backend import config

    config.reset_settings()
    yield d
    # Cleanup: drop the per-thread connection so SQLite releases the file
    # (Windows holds file locks until the connection is closed).
    database.close_connection(str(d / "vaultmind.db"))


@pytest.fixture
def db_path(vault_dir: Path) -> Path:
    """Database path with schema already initialised."""
    p = vault_dir / "vaultmind.db"
    database.init_db(p)
    return p


@pytest.fixture
def sample_text(tmp_path: Path) -> Path:
    """A small sample text file for ingestion tests."""
    p = tmp_path / "sample.txt"
    p.write_text(
        "The authentication middleware handles login flows.\n\n"
        "When a user signs in, the middleware creates a session cookie. "
        "Subsequent requests carry that cookie for verification.\n\n"
        "Rate limiting protects against brute force attacks.\n"
        * 5,
        encoding="utf-8",
    )
    return p
