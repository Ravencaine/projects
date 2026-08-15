"""VaultMind configuration.

Single source of truth for tunables. Loaded from environment variables with
sensible defaults. See docs/DEVELOPMENT.md for the full list.
"""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from backend import paths


class Settings(BaseSettings):
    """Application settings.

    All values are overridable via VAULTMIND_<NAME> environment variables.
    See README.md and docs/DEVELOPMENT.md for the full list.
    """

    model_config = SettingsConfigDict(
        env_prefix="VAULTMIND_",
        case_sensitive=False,
        extra="ignore",
    )

    # ---- Ollama ---------------------------------------------------------- #

    ollama_url: str = "http://localhost:11434"
    """Base URL of the local Ollama HTTP server."""

    model: str = "qwen2.5:7b-instruct-q4_K_M"
    """Default LLM model. Must be pulled via `ollama pull <model>`."""

    num_ctx: int = 8192
    """Context window size. 8192 is the safe max on 16 GB RAM."""

    temperature: float = 0.2
    """LLM sampling temperature. Low for grounded answers."""

    request_timeout_s: float = 300.0
    """Per-request timeout for Ollama calls."""

    # ---- Whisper --------------------------------------------------------- #

    whisper_model: str = "OpenVINO/distil-whisper-large-v3-int4-ov"
    """OpenVINO Whisper IR model (downloaded by bootstrap.ps1)."""

    whisper_device: str = "GPU"
    """OpenVINO device string. 'GPU' → Arc 140V on Windows. Use 'CPU' to disable iGPU."""

    # ---- Chunking -------------------------------------------------------- #

    chunk_target_tokens: int = 700
    """Target chunk size in tokens (cl100k_base)."""

    chunk_min_tokens: int = 350
    chunk_max_tokens: int = 850

    # ---- Paths ----------------------------------------------------------- #

    vault_dir: Path = paths.vault_dir()
    db_path: Path = paths.db_path()
    downloads_dir: Path = paths.downloads_dir()
    audio_dir: Path = paths.audio_dir()
    cache_dir: Path = paths.cache_dir()
    models_dir: Path = paths.models_dir()
    whisper_model_dir: Path = paths.whisper_model_dir()

    # ---- Server ---------------------------------------------------------- #

    host: str = "127.0.0.1"
    port: int = 8765
    """Tauri shell connects to this address. localhost only — never expose 0.0.0.0."""

    log_level: str = "INFO"
    cors_origins: list[str] = [
        "tauri://localhost",
        "http://localhost:1420",
        "http://127.0.0.1:8765",
    ]


_settings: Settings | None = None


def get_settings() -> Settings:
    """Return the cached Settings singleton (instantiated on first call)."""
    global _settings
    if _settings is None:
        _settings = Settings()
        paths.ensure_vault_dirs()
    return _settings


def reset_settings() -> None:
    """Clear the cached singleton. Used by tests when overriding env vars."""
    global _settings
    _settings = None