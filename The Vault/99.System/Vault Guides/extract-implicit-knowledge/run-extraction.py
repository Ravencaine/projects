#!/usr/bin/env python3
"""
Orchestrator for extract-implicit-knowledge.

Runs the full pipeline for one KB at a time:
  Phase 1: discover-and-batch.py  (deterministic)
  Phase 2: dispatch LLM agents   (requires AI)
  Phase 3: persist-as-notes.py   (deterministic)

Usage:
    python run-extraction.py <kb-path>              # full pipeline
    python run-extraction.py <kb-path> --discover  # Phase 1 only
    python run-extraction.py <kb-path> --persist    # Phase 3 only (assumes Phase 2 done)

The script pauses between phases so you can copy-paste the LLM agent commands
into Claude Code if running manually. With --llm option it attempts to dispatch
agents directly (requires an LLM API key in the environment).

Requirements:
    PYTHONIOENCODING=utf-8
    Optional LLM: OPENAI_API_KEY or ANTHROPIC_API_KEY in environment
"""

import json
import os
import subprocess
import sys
import webbrowser
from pathlib import Path
from datetime import date

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

PYTHON = os.environ.get("PYTHON", "py")
SKILL_DIR = Path(__file__).parent.resolve()
VAULT_ROOT = SKILL_DIR.parent.parent.parent  # Vault root
CACHE_DIR = VAULT_ROOT / ".extraction_cache"
MAX_CONCURRENT_BATCHES = 3  # LLM calls to run at once

PROMPT_TEMPLATE = """Analyze batch {n} of {total} for extract-implicit-knowledge skill.

Read: {cache}/batch-{n}.json
Write: {cache}/analysis-batch-{n}.json

Extract entities, claims, and implicit relationships (builds_on, contradicts, exemplifies, cites, authored_by).
Follow the analyst role in SKILL.md — be conservative, deduplicate entities, no wikilink edges.
Output schema:
{{"nodes": [{{"id","type","name","summary","tags","articles"}}], "edges": [{{"source","target","type","direction","weight","description"}}]}}
"""


def resolve_kb(kb_path: str | Path) -> tuple[Path, Path, str]:
    """Resolve KB path to (kb_root, wiki_root, kb_slug)."""
    kb_path_raw = Path(kb_path).expanduser()
    if kb_path_raw.name.lower() == "wiki":
        kb_path_raw = kb_path_raw.parent
    if not kb_path_raw.is_absolute():
        for cand in [VAULT_ROOT / "01.Knowledge" / kb_path_raw,
                     VAULT_ROOT / kb_path_raw]:
            if cand.exists():
                kb_path = cand.resolve()
                break
        else:
            kb_path = kb_path_raw.resolve()
    else:
        kb_path = kb_path_raw.resolve()
    wiki_root = kb_path / "Wiki"
    kb_slug = kb_path.name.lower().replace(" ", "-")
    return kb_path, wiki_root, kb_slug


def run_py(script: Path, *args, cwd: Path | None = None) -> subprocess.CompletedProcess:
    """Run a Python script and return the result."""
    cmd = [PYTHON, str(script)] + list(args)
    return subprocess.run(cmd, capture_output=True, text=True,
                         cwd=str(cwd or VAULT_ROOT), encoding="utf-8", errors="replace")


def phase1_discover(kb_root: Path, wiki_root: Path, kb_slug: str) -> int:
    """Run discover-and-batch.py. Returns number of batches created."""
    print(f"\n{'='*60}")
    print(f"PHASE 1 — Discover")
    print(f"{'='*60}")
    result = run_py(
        SKILL_DIR / "discover-and-batch.py",
        str(kb_root),
        cwd=kb_root
    )
    print(result.stderr)
    if result.returncode != 0:
        print(f"[ERROR] Phase 1 failed with exit code {result.returncode}")
        print(result.stdout)
        sys.exit(1)

    cache_dir = CACHE_DIR / kb_slug
    batch_files = sorted(cache_dir.glob("batch-*.json"))
    print(f"\n[BATCHES] {len(batch_files)} batches ready at:")
    print(f"  {cache_dir}/")
    for bf in batch_files:
        print(f"  - batch-{bf.stem.split('-')[1]}.json")
    return len(batch_files)


def phase2_llm_dispatch(kb_slug: str, num_batches: int) -> None:
    """Print Claude Code agent commands for each batch."""
    cache_dir = CACHE_DIR / kb_slug
    cache_path = str(cache_dir).replace("\\", "/")

    print(f"\n{'='*60}")
    print(f"PHASE 2 — LLM Analysis ({num_batches} batches)")
    print(f"{'='*60}")
    print("""
Run these in Claude Code (paste into chat). Up to 3 can run in parallel.

For each batch, dispatch an agent with this pattern:
""")

    for n in range(num_batches):
        prompt = PROMPT_TEMPLATE.format(
            n=n, total=num_batches, cache=cache_path
        )
        print(f"\n--- Batch {n} / {num_batches} ---")
        print(f"/agent Analyze batch {n} of {num_batches}")
        print(f"Prompt:\n{prompt}")

    print(f"""

When all agents finish, press Enter to continue to Phase 3...
(Or run: py "{SKILL_DIR / 'persist-as-notes.py'}" "{kb_slug}")
""")
    input("Press Enter when all LLM batches are complete...")


def phase3_persist(kb_root: Path, kb_slug: str) -> None:
    """Run persist-as-notes.py."""
    print(f"\n{'='*60}")
    print(f"PHASE 3 — Persist")
    print(f"{'='*60}")
    result = run_py(
        SKILL_DIR / "persist-as-notes.py",
        str(kb_root),
        cwd=kb_root
    )
    print(result.stderr)
    if result.returncode == 0:
        print("[OK] Notes written successfully")
    elif result.returncode == 2:
        print("[WARN] Some notes failed — check errors above")
    else:
        print(f"[ERROR] Phase 3 failed with exit code {result.returncode}")
        sys.exit(1)

    # Print summary of what was created
    wiki_root = kb_root / "Wiki"
    implicit = wiki_root / "Implicit"
    if implicit.exists():
        entities = list((implicit / "Entities").glob("*.md")) if (implicit / "Entities").exists() else []
        claims = list((implicit / "Claims").glob("*.md")) if (implicit / "Claims").exists() else []
        edges = list(implicit.rglob("Edges/*.md")) if implicit.exists() else []
        print(f"\n[CREATED]")
        print(f"  Entities:     {len(entities)}")
        print(f"  Claims:       {len(claims)}")
        print(f"  Relationships: {sum(1 for _ in implicit.rglob('*.md')) - len(entities) - len(claims)}")

    # Offer to open in Obsidian
    print(f"""
[INDEX] New notes added to: Wiki/Implicit/
[OUTPUTS] Report: Outputs/{date.today()}_implicit-extraction-{kb_slug}.md

Run orphan check:
  py 99.System/Scripts/find_orphans.py
""")


def phase4_cleanup(kb_slug: str) -> None:
    """Remove the extraction cache."""
    cache_dir = CACHE_DIR / kb_slug
    if cache_dir.exists():
        import shutil
        shutil.rmtree(cache_dir)
        print(f"[CLEANUP] Removed {cache_dir}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    kb_path = sys.argv[1] if len(sys.argv) > 1 else None
    if not kb_path:
        print("Usage: python run-extraction.py <kb-path> [--discover|--persist|--cleanup]")
        print("  <kb-path>: KB name, path, or full path")
        print("  --discover: Phase 1 only")
        print("  --persist:  Phase 3 only (assumes Phase 2 done)")
        print("  --cleanup:  Remove cache only")
        print("  No flag:    Full pipeline (Phases 1→2→3)")
        sys.exit(1)

    kb_root, wiki_root, kb_slug = resolve_kb(kb_path)
    print(f"[KB] {kb_root.name} ({kb_slug})")
    print(f"[WIKI] {wiki_root}")

    phase = sys.argv[2] if len(sys.argv) > 2 else None

    if phase == "--discover":
        phase1_discover(kb_root, wiki_root, kb_slug)
    elif phase == "--persist":
        phase3_persist(kb_root, kb_slug)
    elif phase == "--cleanup":
        phase4_cleanup(kb_slug)
    else:
        num_batches = phase1_discover(kb_root, wiki_root, kb_slug)
        phase2_llm_dispatch(kb_slug, num_batches)
        phase3_persist(kb_root, kb_slug)


if __name__ == "__main__":
    main()
