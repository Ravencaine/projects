"""Cross-platform path helpers for VaultMind.

Centralises all filesystem locations so config.py stays simple and tests can
override paths via env vars.
"""

from __future__ import annotations

import os
from pathlib import Path

# Repo root = parent of backend/ (this file lives in backend/).
REPO_ROOT: Path = Path(__file__).resolve().parent.parent


def _resolve(name: str, default: Path) -> Path:
    """Resolve a path from VAULTMIND_<NAME> env var, else default."""
    env_key = f"VAULTMIND_{name}"
    value = os.environ.get(env_key)
    if value:
        return Path(value).expanduser().resolve()
    return default


def vault_dir() -> Path:
    """Directory containing vaultmind.db and cache subdirs."""
    return _resolve("VAULT_DIR", REPO_ROOT / "vault")


def db_path() -> Path:
    """SQLite database file."""
    return _resolve("DB_PATH", vault_dir() / "vaultmind.db")


def downloads_dir() -> Path:
    """Raw downloads cache (yt-dlp output)."""
    return _resolve("DOWNLOADS_DIR", vault_dir() / "downloads")


def audio_dir() -> Path:
    """Extracted 16-kHz mono WAV (Whisper input)."""
    return _resolve("AUDIO_DIR", vault_dir() / "audio")


def cache_dir() -> Path:
    """Ephemeral temp files (extraction intermediates, thumbnails)."""
    return _resolve("CACHE_DIR", vault_dir() / ".cache")


def models_dir() -> Path:
    """Local model storage (Ollama + OpenVINO Whisper IR)."""
    return _resolve("MODELS_DIR", REPO_ROOT / "models")


def whisper_model_dir() -> Path:
    """OpenVINO Whisper IR cache."""
    return _resolve(
        "WHISPER_DIR",
        models_dir() / "whisper" / "distil-whisper-large-v3-int4-ov",
    )


def ensure_vault_dirs() -> None:
    """Create the vault/ subdirectory tree if missing. Idempotent."""
    for path in (vault_dir(), downloads_dir(), audio_dir(), cache_dir()):
        path.mkdir(parents=True, exist_ok=True)