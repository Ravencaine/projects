#!/usr/bin/env python3
"""
fix_registry_orphans.py

Fixes _INGESTED.md entries for REGISTRY orphans detected by find_orphans.py.

Root cause: the Inbox used a descriptive/SEO filename, but the ingestion skill
renamed the source to its article title + author attribution. The notes correctly
use the renamed source, but the registry kept the original Inbox filename — so
find_orphans.py sees a mismatch and flags them as orphans.

Fix: update the registry filename and notes column to match the ingested title.

One entry (3 DAX Functions You Must Learn First) was genuinely skipped and
should be marked rejected.

Dry run by default. Pass --apply to write changes.

Usage:
    python fix_registry_orphans.py        # dry run
    python fix_registry_orphans.py --apply  # apply changes
"""
import argparse
import re
import sys
from pathlib import Path

VAULT_DIR = Path(__file__).parent.parent.parent.resolve()
REGISTRY  = VAULT_DIR / "00.Inbox" / "_INGESTED.md"

# Mapping: original registry filename → (new_filename, new_notes, optional_new_status)
UPDATES = {
    # key: original filename in registry
    # value: (new_filename, updated_notes, optional_new_status)
    "3 Ways Power BI Dashboards Can Help In Decision-Making": (
        "Power BI Dashboards Decision-Making (Boniface Muchendu)",
        "6 notes (1 source + 5 atomics); Boniface Muchendu 4th source",
    ),
    "2 Powerful Tips for Using Power BI's RAND() and RAND.BETWEEN()": (
        "RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)",
        "6 notes (1 source + 2 functions + 1 pattern + 1 gotcha + 1 atomic); Boniface Muchendu 5th source",
    ),
    "How to Do Anomaly Detection in Power BI (No External Tools Needed)": (
        "How to Do Anomaly Detection in Power BI (Isabelle Bittar)",
        "9 notes (1 source + 6 Power BI + 3 Power Query); PBIX downloaded to Attachments/; Isabelle Bittar 2nd source",
    ),
    "Circular Images in Power BI (That Actually Render Properly)": (
        "Circular Images in Power BI (Isabelle Bittar)",
        "10 notes (1 source + 1 author + 6 Power BI + 2 Power Query); PBIX downloaded; Isabelle Bittar 3rd source",
    ),
    "Using Time Periods as Slicers to Enhance Power BI Line or Area Charts' Range": (
        "Using Time Periods as Slicers to Enhance Power BI Line or Area Charts' Range",
        "exact duplicate of Time-Period-Slicers.md (ingested 2026-07-29); rejected",
        "rejected",
    ),
    "3 DAX Functions You Must Learn First in Power BI": (
        "3 DAX Functions You Must Learn First in Power BI",
        "skipped — SUM, CALCULATE, FILTER all exist in vault with equal/greater depth; beginner framing only; Anurodh Kumar 4th source",
        "rejected",
    ),
}


def parse_table(content: str) -> list[tuple[int, str]]:
    """Return list of (line_number_0indexed, raw_line) for table rows."""
    rows = []
    for i, line in enumerate(content.splitlines()):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            rows.append((i, line))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fix _INGESTED.md registry entries for REGISTRY orphans (dry run)."
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Write changes to _INGESTED.md. Without this flag, changes are printed only."
    )
    args = parser.parse_args()

    if not REGISTRY.exists():
        print(f"ERROR: Registry not found at {REGISTRY}", file=sys.stderr)
        return 2

    content = REGISTRY.read_text(encoding="utf-8")
    original = content

    # Parse table rows
    lines = content.splitlines()
    changes = []

    for old_filename, update in UPDATES.items():
        if len(update) == 2:
            new_filename, new_notes = update
            new_status = None
        else:
            new_filename, new_notes, new_status = update
        # Try to find the row by the old filename
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped.startswith("|") or stripped.startswith("|---"):
                continue
            parts = [p.strip() for p in stripped.split("|")]
            if len(parts) < 7:
                continue
            # parts[1] is the filename column
            cell = parts[1].strip()
            # Strip trailing ellipsis/periods
            cell_clean = re.sub(r"[……\"]+$", "", cell).strip()
            if cell_clean == old_filename or cell == old_filename:
                final_status = new_status if new_status else parts[4]
                new_row = (
                    f"| {new_filename} | "
                    f"{parts[2]} | "
                    f"{parts[3]} | "
                    f"{final_status} | "
                    f"{parts[5]} | "
                    f"{new_notes} |"
                )
                changes.append((i, line, new_row, old_filename, new_filename, final_status))
                break

    if not changes:
        print("No matching rows found in registry. Entries may already be updated.")
        return 1

    print(f"Found {len(changes)} row(s) to update:\n")
    for _, _, _, old_fn, new_fn, final_status in changes:
        status_label = "rejected ✓" if final_status == "rejected" else "updated"
        print(f"  {old_fn}")
        print(f"  → {new_fn}  [{status_label}]")
        print()

    if not args.apply:
        print("Dry run. Pass --apply to write changes.")
        return 0

    # Apply changes
    for i, _, new_row, _, _, _ in reversed(changes):
        lines[i] = new_row

    new_content = "\n".join(lines) + "\n"
    REGISTRY.write_text(new_content, encoding="utf-8")

    print(f"Wrote {len(changes)} change(s) to {REGISTRY}")
    print("\nNOTE: You may want to re-run find_orphans.py to confirm 0 orphans:")
    print("  python 99.System/Scripts/find_orphans.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
