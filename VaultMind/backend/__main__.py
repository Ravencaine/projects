"""Uvicorn entry shim for PyInstaller bundling.

Running `python -m backend` invokes uvicorn on the FastAPI app. The same
entry is used by `scripts/bootstrap.ps1` (`uvicorn backend.main:app …`)
and by the PyInstaller-bundled `.exe` (which simply calls
`uvicorn.run(app, host, port)`).
"""

from __future__ import annotations

import logging

import uvicorn

from backend.config import get_settings
from backend.main import app


def main() -> None:
    cfg = get_settings()
    logging.basicConfig(
        level=cfg.log_level,
        format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    )
    uvicorn.run(
        app,
        host=cfg.host,
        port=cfg.port,
        log_level=cfg.log_level.lower(),
        access_log=True,
    )


if __name__ == "__main__":
    main()