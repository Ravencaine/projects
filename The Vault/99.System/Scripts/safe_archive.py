#!/usr/bin/env python
"""
safe_archive.py — Safe source-file archiver with verification gate.

Usage:
    python safe_archive.py <source_filename> [--dry-run]

Examples:
    python safe_archive.py "Article - CALCULATE in Power BI.md"
    python safe_archive.py "Article - CALCULATE in Power BI.md" --dry-run

Behaviour:
    1. Looks up the source in 00.Inbox/_INGESTED.md to find its target KB(s).
    2. Searches those KB Wikis for notes whose frontmatter `source:` field
       matches the source filename.
    3. If >= 1 matching note is found → archives the source and updates
       _INGESTED.md status to "archived".
    4. If no matching notes are found → prints an error and exits 1.
       The source stays in the Inbox.

Exit codes:
    0  — archived successfully (or --dry-run: would archive)
    1  — no notes found for this source (BLOCKED)
    2  — usage error
    3  — source not found in Inbox
"""

import argparse
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

# ── paths ─────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
VAULT_DIR   = SCRIPT_DIR.parent.parent.resolve()          # The Vault/
INBOX_DIR   = VAULT_DIR / "00.Inbox"
ARCHIVE_DIRS = [
    INBOX_DIR / "_Archive",                    # legacy flat archive
    VAULT_DIR / "99.System" / "InboxArchive",  # date-bucketed archive
]
REGISTRY    = INBOX_DIR / "_INGESTED.md"

KB_NAMES = [
    "Data Modeling",
    "DAX Code",
    "Excel",
    "Power BI",
    "Power Query",
    "VBA",
]

# ── helpers ────────────────────────────────────────────────────────────────────

def _normalise(s: str) -> str:
    """Collapse all Unicode quote variants to a plain ASCII string for comparison.

    Handles:
    - write_file YAML quoting: \' → ', \" → "
    - Curly/smart quotes in filenames or frontmatter: U+2019 → '
    - Em-dash variant in filenames: U+2014 → -
    """
    stripped = (s.strip()
                .replace("\\'", "'")
                .replace('\\"', '"')
                .replace('\u201c', '')
                .replace('\u201d', '')
                .replace('\u2018', '')
                .replace('\u2019', "'")
                .replace('\u2014', '-'))
    # Strip only outer YAML quotes, not all quote characters (Python's
    # strip("'") strips every quote-char from BOTH ends, including mid-string).
    # Use lstrip/rstrip on the specific outer char instead.
    if len(stripped) >= 2:
        if stripped[0] == '"' and stripped[-1] == '"':
            stripped = stripped[1:-1]
        elif stripped[0] == "'" and stripped[-1] == "'":
            stripped = stripped[1:-1]
    return stripped


def parse_frontmatter(text: str) -> dict:
    """Return key:value dict from YAML frontmatter block."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    result = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = _normalise(val)
        result[key.strip()] = val
    return result


def find_notes_for_source(source_name: str) -> list[Path]:
    """Return paths of notes in all KB Wikis whose frontmatter source: matches."""
    matches = []
    for kb in KB_NAMES:
        wiki_dir = VAULT_DIR / "01.Knowledge" / kb / "Wiki"
        if not wiki_dir.is_dir():
            continue
        for note_path in wiki_dir.glob("*.md"):
            if note_path.name in ("INDEX.md", "QUESTIONS.md"):
                continue
            try:
                text = note_path.read_text(encoding="utf-8")
                fm   = parse_frontmatter(text)
                if _normalise(fm.get("source", "").removesuffix(".md")) == _normalise(source_name.removesuffix(".md")):
                    matches.append(note_path)
            except Exception:
                pass
    return matches


def lookup_source_in_registry(source_name: str) -> dict | None:
    """Return dict with status + KB info for a source, or None if not found."""
    if not REGISTRY.exists():
        return None
    content = REGISTRY.read_text(encoding="utf-8")
    for line in content.splitlines():
        if source_name in line and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")]
            # columns: (empty), filename, date, KB, status, archive_path, notes
            if len(parts) >= 6 and parts[1] == source_name:
                return {
                    "status":      parts[4],
                    "archive_path": parts[5],
                    "notes":       parts[6] if len(parts) > 6 else "",
                }
    return None


def update_registry_archived(source_name: str) -> bool:
    """Update _INGESTED.md: change status to 'archived', set archive path."""
    if not REGISTRY.exists():
        return False
    content = REGISTRY.read_text(encoding="utf-8")
    today = date.today().strftime("%Y-%m")
    archive_rel = f"99.System/InboxArchive/{today}/"
    lines = content.splitlines()
    new_lines = []
    changed = False
    for line in lines:
        if source_name in line and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5 and parts[1] == source_name.removesuffix(".md"):
                # Patch status + archive path
                parts[4] = "archived"
                if len(parts) >= 5:
                    parts[5] = archive_rel
                new_lines.append("| " + " | ".join(parts[1:]) + " |")
                changed = True
                continue
        new_lines.append(line)
    if changed:
        REGISTRY.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return changed


# ── main ───────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Safe archive: verify notes before moving source.")
    parser.add_argument("source", help="Source filename as it appears in 00.Inbox/ (must include .md)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without moving anything")
    args = parser.parse_args()

    source_name = args.source.strip()
    if not source_name.endswith(".md"):
        source_name += ".md"

    source_path = INBOX_DIR / source_name

    # Step 1: check source exists in Inbox
    if not source_path.exists():
        print(f"ERROR: Source not found in Inbox: {source_name}", file=sys.stderr)
        return 3

    # Step 2: look up in registry
    reg_info = lookup_source_in_registry(source_name)
    if reg_info:
        current_status = reg_info["status"]
        if current_status == "archived":
            print(f"INFO: Source already marked 'archived' in registry: {source_name}")
            return 0
    else:
        current_status = "unknown"

    # Step 3: find notes that reference this source
    notes = find_notes_for_source(source_name)

    if not notes:
        print(f"BLOCKED: No notes found in any KB for '{source_name}'", file=sys.stderr)
        print(f"  Registry status : {current_status}", file=sys.stderr)
        print(f"  Hint: ingest this source first, then archive only after notes exist.", file=sys.stderr)
        return 1

    print(f"Found {len(notes)} note(s) referencing this source:")
    for n in notes:
        print(f"  {n.relative_to(VAULT_DIR)}")

    if args.dry_run:
        print(f"\n[DRY RUN] Would archive: {source_name}")
        print(f"  Source  : {source_path}")
        print(f"  Archive : {ARCHIVE_DIRS[1] / date.today().strftime('%Y-%m') / source_name}")
        print(f"  Registry: status → 'archived'")
        return 0

    # Step 4: archive
    today_str = date.today().strftime("%Y-%m")
    month_dir = ARCHIVE_DIRS[1] / today_str   # prefer date-bucketed archive
    month_dir.mkdir(parents=True, exist_ok=True)

    dest = month_dir / source_name
    shutil.move(str(source_path), str(dest))

    # Step 5: update registry
    update_registry_archived(source_name)

    print(f"\nArchived: {source_name}")
    print(f"  → {dest.relative_to(VAULT_DIR)}")
    print(f"  Registry updated to 'archived'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
