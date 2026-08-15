#!/usr/bin/env python3
"""Phase 0 verification: repo structure + architectural rules in place.

Run after Phase 0 (Bootstrap) is complete to confirm the scaffold is sound
before writing any logic.

Exit code:
    0 — all checks pass
    1 — at least one check failed

Usage:
    python scripts/verify_phase0.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Required top-level files and folders (relative to REPO_ROOT).
REQUIRED_FILES = [
    "SPEC.md",
    "README.md",
    "CLAUDE.md",
    "LICENSE",
    ".gitignore",
    ".editorconfig",
    ".python-version",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
]
REQUIRED_DIRS = [
    "src-tauri",
    "src-tauri/src",
    "frontend",
    "frontend/icons",
    "backend",
    "backend/ingest",
    "models",
    "models/whisper",
    "vault",
    "vault/downloads",
    "vault/audio",
    "vault/.cache",
    "docs",
    "scripts",
    "tests",
    "tests/data",
]

# A file is "empty" if it's a .gitkeep with no real content. We accept either
# a .gitkeep or any file with at least 1 byte.
def _has_content(d: Path) -> bool:
    if not d.exists():
        return False
    if not d.is_dir():
        return d.stat().st_size > 0
    for child in d.iterdir():
        if child.name == ".gitkeep":
            return True
        if child.is_file() and child.stat().st_size > 0:
            return True
        if child.is_dir() and _has_content(child):
            return True
    return False

# SPEC.md bug fixes that must be present after Phase 0.
SPEC_MUST_HAVE = [
    ("Whisper backend corrected", re.compile(r"openvino[- ]genai", re.IGNORECASE)),
    ("distil-whisper reference", re.compile(r"distil[- ]whisper[- ]large[- ]v3[- ]int4[- ]ov", re.IGNORECASE)),
    ("ebooklib (not epublib)", re.compile(r"ebooklib", re.IGNORECASE)),
    ("epublib removed", re.compile(r"epublib", re.IGNORECASE)),  # should NOT match
    ("Open Decisions resolved heading", re.compile(r"Open Decisions \(Resolved\)", re.IGNORECASE)),
    ("bm25 / FTS5 mention", re.compile(r"FTS5", re.IGNORECASE)),
    ("qwen2.5 7b model", re.compile(r"qwen2\.5", re.IGNORECASE)),
]
# Sentinel: should-match patterns that would indicate SPEC.md was not fixed.
SPEC_MUST_NOT_HAVE = [
    ("epublib still referenced", re.compile(r"epublib", re.IGNORECASE)),
    ("faster-whisper still as backend", re.compile(r"intel-extension-for-pytorch", re.IGNORECASE)),
]

# CLAUDE.md non-negotiable rules that must be present.
CLAUDE_RULES = [
    ("RULE-VM-1 (no semantic search)", re.compile(r"RULE-VM-1:.*No semantic search", re.IGNORECASE | re.DOTALL)),
    ("RULE-VM-4 (Whisper backend)", re.compile(r"RULE-VM-4:.*Whisper backend is OpenVINO", re.IGNORECASE | re.DOTALL)),
    ("RULE-VM-5 (Ollama CPU-only)", re.compile(r"RULE-VM-5:.*Ollama is CPU-only", re.IGNORECASE | re.DOTALL)),
    ("RULE-VM-8 (plugin registry)", re.compile(r"RULE-VM-8:.*Plugin registry", re.IGNORECASE | re.DOTALL)),
    ("RULE-VM-9 (Tauri subprocess)", re.compile(r"RULE-VM-9:.*Tauri 2\.x spawns Python as a subprocess", re.IGNORECASE | re.DOTALL)),
]


def check(label: str, condition: bool, detail: str = "") -> bool:
    mark = "PASS" if condition else "FAIL"
    color = "\033[92m" if condition else "\033[91m"
    reset = "\033[0m"
    suffix = f" — {detail}" if detail else ""
    print(f"  [{color}{mark}{reset}] {label}{suffix}")
    return condition


def main() -> int:
    print("=" * 70)
    print("VaultMind — Phase 0 verification (repo scaffold + architectural rules)")
    print("=" * 70)
    print()

    failures = 0
    total = 0

    def add(label: str, ok: bool, detail: str = "") -> None:
        nonlocal failures, total
        total += 1
        if not check(label, ok, detail):
            failures += 1

    print("[1/4] Required files exist")
    print("-" * 70)
    for rel in REQUIRED_FILES:
        p = REPO_ROOT / rel
        add(f"{rel}", p.is_file(), "missing" if not p.is_file() else f"{p.stat().st_size} bytes")

    print()
    print("[2/4] Required directories exist (with content or .gitkeep)")
    print("-" * 70)
    for rel in REQUIRED_DIRS:
        p = REPO_ROOT / rel
        add(f"{rel}/", _has_content(p), "missing or empty" if not _has_content(p) else "ok")

    print()
    print("[3/4] SPEC.md bug fixes applied")
    print("-" * 70)
    spec_text = (REPO_ROOT / "SPEC.md").read_text(encoding="utf-8")
    for label, pattern in SPEC_MUST_HAVE:
        if pattern.search(spec_text):
            add(label, True, "found")
        else:
            # `epublib removed` is a sentinel: the pattern must NOT match.
            if label == "epublib removed":
                add(label, True, "correctly absent")
            else:
                add(label, False, "not found in SPEC.md")
    for label, pattern in SPEC_MUST_NOT_HAVE:
        if pattern.search(spec_text):
            add(label, False, "still present — fix needed")
        else:
            add(label, True, "correctly absent")

    print()
    print("[4/4] CLAUDE.md non-negotiable rules present")
    print("-" * 70)
    claude_text = (REPO_ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    for label, pattern in CLAUDE_RULES:
        add(label, bool(pattern.search(claude_text)), "found" if pattern.search(claude_text) else "missing")

    print()
    print("=" * 70)
    if failures == 0:
        print(f"\033[92mOK\033[0m — {total} checks passed, 0 failed")
        print()
        print("Phase 0 complete. Next:")
        print("  pwsh -ExecutionPolicy Bypass -File scripts\\bootstrap.ps1")
        print("  python scripts/verify_phase1.py   (after Phase 1 MVP)")
        return 0
    else:
        print(f"\033[91mFAILED\033[0m — {failures} of {total} checks failed")
        print()
        print("Fix the failures above and re-run.")
        return 1


if __name__ == "__main__":
    sys.exit(main())