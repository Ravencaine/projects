#!/usr/bin/env python
"""
find_orphans.py — Detect orphan notes across the vault.

Checks three orphan types:
  1. INDEX orphans  — notes in KB Wikis not linked from INDEX.md (excludes nav files: INDEX.md, CHANGELOG.md, QUESTIONS.md)
  2. SOURCE orphans — notes whose source: frontmatter field has no matching
                      file in Inbox or InboxArchive (excluding known external
                      sources like dax.pdf, system:, etc.)
  3. REGISTRY orphans — sources logged in _INGESTED.md but no note in any KB
                        has a matching source: field

Usage:
    python find_orphans.py
    python find_orphans.py --fix          # propose wikilink additions to INDEX.md
    python find_orphans.py --verbose       # show all notes checked
    python find_orphans.py --source "Article Name.md"  # check a specific source

Exit codes:
    0 — no orphans found
    1 — orphans found (see output)
    2 — usage / path error

Known safe source values that are never orphans (external/virtual sources):
    dax.pdf, system, manual, cli, user
"""

import argparse
import re
import sys
from pathlib import Path

# ── paths ─────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
VAULT_DIR  = SCRIPT_DIR.parent.parent.resolve()   # The Vault/
INBOX_DIR  = VAULT_DIR / "00.Inbox"
ARCHIVE_DIRS = [
    INBOX_DIR / "_Archive",               # legacy flat archive
    VAULT_DIR / "99.System" / "InboxArchive",  # date-bucketed archive
]
REGISTRY   = INBOX_DIR / "_INGESTED.md"

KB_NAMES = [
    "Data Modeling",
    "DAX Code",
    "Excel",
    "Power BI",
    "Power Query",
    "VBA",
]

# Source values that are external/virtual — never orphans
EXTERNAL_SOURCES = {
    "system", "manual", "cli", "user", "session",
    "dax.pdf", "m-code.pdf",
    "dax_for_humans_extracted.txt",
    "m-code_extracted.txt",
    "m-code_full.txt",
    "unknown",          # notes with no identifiable source file
}

# ── helpers ────────────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    result = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        result[key.strip()] = val.strip().strip('"').strip("'")
    return result


def get_indexed_wikilinks(kb: str) -> set[str]:
    """Return set of note stems (basename without .md) linked from INDEX.md."""
    index_path = VAULT_DIR / "01.Knowledge" / kb / "Wiki" / "INDEX.md"
    if not index_path.exists():
        return set()
    text = index_path.read_text(encoding="utf-8")
    # [[note-name]] or [[note-name|display]]
    # Extract stem (filename without .md) from wikilinks to match note_path.stem
    stems = set()
    for m in re.finditer(r"\[\[(.+?)(?:\|.*?)?\]\]", text):
        link = m.group(1)
        stems.add(Path(link).stem)  # strip .md if present
    return stems


def _normalise_for_lookup(val: str) -> str:
    """
    Normalise an archive filename the same way normalise_source() normalises
    a note's source: field value. Both sides must use the same rules so that
    en-dash → hyphen, apostrophes stripped, etc.
    """
    import unicodedata
    val = unicodedata.normalize("NFKD", val)
    val = val.encode("ascii", errors="replace").decode("ascii")
    val = re.sub(r"['\u2018\u2019\u201a\u201b]", "", val)
    val = re.sub(r"[\u2014\u2013\u2010\u2011]", "-", val)
    val = re.sub(r"[\"\u201c\u201d\u201e]", '"', val)
    val = re.sub(r"[?:!]", " ", val)
    val = re.sub(r"[^\w\s-]", " ", val)
    val = re.sub(r"\s+", " ", val)
    return val.lower().strip(" -")


def get_all_source_files() -> set[str]:
    """
    Return set of all potential source filenames in Inbox and InboxArchive,
    lowercased for comparison. Includes .md files plus non-md source files
    (PDFs, .txt extraction outputs, etc.) that notes may reference.
    Filenames are normalised via _normalise_for_lookup() so they match
    the output of normalise_source() — en-dashes → hyphens, apostrophes
    stripped, etc.
    """
    sources = set()
    if INBOX_DIR.exists():
        for f in INBOX_DIR.iterdir():
            if f.is_file():
                sources.add(_normalise_for_lookup(f.name))
    for arch_dir in ARCHIVE_DIRS:
        if arch_dir.exists():
            for f in arch_dir.rglob("*"):
                if f.is_file():
                    sources.add(_normalise_for_lookup(f.name))
    return sources


def strip_wikilink(val: str) -> str:
    """Extract the target from [[target|display]] or [[target]]."""
    m = re.match(r"\[\[(.+?)(?:\|.+?)?\]\]", val.strip())
    if m:
        return m.group(1)
    return val


def normalise_source(val: str) -> str:
    """
    Canonicalise a source: field value to match archive filenames.
    - Strips surrounding [[ ]] wiki-link brackets
    - Strips .md extension
    - Normalises Unicode punctuation to ASCII equivalents
    - Lower-cases and strips whitespace
    Returns the normalised title slug.
    """
    import unicodedata
    val = val.strip()
    val = strip_wikilink(val)
    # Normalise Unicode punctuation → ASCII
    val = unicodedata.normalize("NFKD", val)
    val = val.encode("ascii", errors="replace").decode("ascii")
    # Normalise dashes, quotes, apostrophes (strip apostrophes entirely — "pro's" → "pros")
    val = re.sub(r"['\u2018\u2019\u201a\u201b]", "", val)    # all apostrophes → gone
    val = re.sub(r"[\u2014\u2013\u2010\u2011]", "-", val)    # em/en dash → hyphen
    val = re.sub(r"[\"\u201c\u201d\u201e]", '"', val)         # smart quotes → straight
    val = re.sub(r"[?:!]", " ", val)                          # strip terminal punctuation
    val = re.sub(r"[^\w\s-]", " ", val)                       # strip remaining punctuation
    val = re.sub(r"\s+", " ", val)                           # collapse whitespace
    # Strip .md extension
    if val.lower().endswith(".md"):
        val = val[:-3]
    return val.lower().strip(" -")


def source_matches_file(source_val: str, all_sources: set[str]) -> bool:
    """
    Check if a source: field value matches a real file in Inbox/Archive.
    Handles:
      - Normal title matches (case-insensitive, strip .md)
      - Wiki-link sources: [[Title]] → extract bare title
      - URL sources → always external
      - Author names (e.g. "Greg Deckler") → external
      - Book titles (e.g. "DAX for Humans — Deckler") → external
    all_sources is lowercased; comparisons are case-insensitive.
    """
    if not source_val.strip():
        return False

    norm = normalise_source(source_val)
    if is_external_source_name(norm):
        return False

    norm_nopunct = norm.replace("'", "")   # strip apostrophes for cross-match

    # 1. Try exact match (bare title + .md)
    if f"{norm}.md" in all_sources:
        return True

    # 2. Try substring match: source title is a substring of archive filename
    for fname in all_sources:
        fname_nopunct = fname.replace("'", "")
        if norm in fname or fname in norm:
            return True
        if norm_nopunct in fname_nopunct or fname_nopunct in norm_nopunct:
            return True

    # 3. Token-overlap match
    # Split into tokens; require THRESHOLD of the longer token set to match.
    # This is the most tolerant strategy — handles stripped punctuation between
    # the article title and the archive filename.
    src_tokens = set(norm.split())
    THRESHOLD = 0.60   # fraction of source tokens that must appear in filename
    MIN_MATCH  = 3     # absolute minimum tokens that must match
    for fname in all_sources:
        fname_norm = fname.rsplit(".", 1)[0]   # strip .md extension
        fname_tokens = set(fname_norm.split())
        # Count how many src tokens appear in the filename
        overlap = len(src_tokens & fname_tokens)
        if overlap >= min(THRESHOLD * len(src_tokens), len(src_tokens) - 1) \
           and overlap >= MIN_MATCH:
            return True

    return False


def is_external_source_name(val: str, all_sources: set[str] | None = None) -> bool:
    """
    Return True for source values that are author names, book titles,
    Medium/URL-style sources, or other compound/virtual sources — not
    real archive filenames.

    If all_sources is provided, archive files are checked first — a PDF
    that exists in the archive is NOT external, even if it has .pdf in the name.
    """
    val_lower = val.lower()

    # Skip obvious URLs and wiki-link paths
    if re.match(r"https?://", val_lower):
        return True
    if val_lower.startswith("//") or val_lower.startswith("/"):
        return True

    # If we have the file list, check whether this source IS a real file.
    # If so, it's not external — it's a valid archive reference.
    if all_sources is not None:
        val_nopunct = val_lower.replace("'", "")
        # Try exact filename match
        if val_lower in all_sources or val_nopunct in all_sources:
            return False
        # Try bare title (strip extension)
        bare = val_lower.rsplit(".", 1)[0] if "." in val_lower else val_lower
        bare_nopunct = bare.replace("'", "")
        if bare in all_sources or bare_nopunct in all_sources:
            return False

    # Author names (1-2 words, likely a person's name)
    name_indicators = [
        "greg dec", "salvatore c", "mirko p", "isabelle b",
        "tom la", "jesse r", "boris c", "anupriya",
        "diepeveen", "bordeg",
    ]
    if any(n in val_lower for n in name_indicators):
        words = val_lower.split()
        if len(words) <= 3 and not any(c in val_lower for c in ["article", "guide", "tutorial", "how to", "using", "with", "pdf"]):
            return True

    # Book / course / known virtual source titles
    book_indicators = [
        "dax for humans", "beginning big data",
        "artificial intelligence with power bi (diepeveen)",
    ]
    if any(b in val_lower for b in book_indicators):
        return True

    return False


def get_registry_sources() -> dict[str, dict]:
    """Return {filename: {status, notes}} from _INGESTED.md."""
    if not REGISTRY.exists():
        return {}
    result = {}
    content = REGISTRY.read_text(encoding="utf-8")
    for line in content.splitlines():
        line_stripped = line.strip()
        if not line_stripped or not line_stripped.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 5:
            continue
        filename = parts[1]
        # Skip header rows and separator rows
        if not filename or filename in ("File", "------") or filename.startswith("-"):
            continue
        # Strip trailing ellipsis/periods from filenames (e.g. "Beyond VLOOKUP…")
        filename = re.sub(r"[\u2026…\"]+$", "", filename).strip()
        result[filename] = {
            "status": parts[4],
            "notes":  parts[6] if len(parts) > 6 else "",
        }
    return result


def scan_all_notes(verbose: bool = False) -> dict[str, dict]:
    """
    Scan all KB Wikis. Return dict:
      {note_path: {"kb", "name", "source", "stem"}}
    """
    notes = {}
    for kb in KB_NAMES:
        wiki_dir = VAULT_DIR / "01.Knowledge" / kb / "Wiki"
        if not wiki_dir.is_dir():
            continue
        for note_path in wiki_dir.glob("*.md"):
            try:
                text = note_path.read_text(encoding="utf-8")
            except Exception:
                continue
            fm = parse_frontmatter(text)
            source_val = fm.get("source", "")
            notes[str(note_path)] = {
                "kb":     kb,
                "name":   note_path.name,
                "stem":   note_path.stem,           # without .md
                "source": source_val,
            }
            if verbose:
                print(f"  [scan] {kb}/{note_path.name}  source={source_val!r}")
    return notes


# ── orphan scanners ───────────────────────────────────────────────────────────

def find_index_orphans(notes: dict[str, dict], verbose: bool = False) -> list[dict]:
    """Notes not linked from their KB's INDEX.md."""
    orphans = []
    # Build indexed set once per KB
    indexed_by_kb: dict[str, set[str]] = {}
    for kb in KB_NAMES:
        indexed_by_kb[kb] = get_indexed_wikilinks(kb)

    for note_path, info in notes.items():
        note_path_obj = Path(note_path)
        if note_path_obj.name in ("INDEX.md", "CHANGELOG.md", "QUESTIONS.md"):
            continue
        indexed = indexed_by_kb[info["kb"]]
        if info["stem"] not in indexed:
            orphans.append({
                "type":    "INDEX orphan",
                "kb":      info["kb"],
                "note":    info["name"],
                "path":    note_path,
            })
            if verbose:
                print(f"  [orphan] INDEX: {info['kb']}/{info['name']} — not in INDEX.md")
    return orphans


def find_source_orphans(notes: dict[str, dict], all_sources: set[str],
                        verbose: bool = False) -> list[dict]:
    """Notes whose source: field matches no file in Inbox or InboxArchive."""
    orphans = []
    for note_path, info in notes.items():
        note_path_obj = Path(note_path)
        # Skip INDEX and QUESTIONS — they are vault system files
        if note_path_obj.name in ("INDEX.md", "CHANGELOG.md", "QUESTIONS.md"):
            continue
        src = info["source"].strip()
        if not src:
            orphans.append({
                "type":  "SOURCE orphan (empty)",
                "kb":    info["kb"],
                "note":  info["name"],
                "path":  note_path,
                "note_source_field": src,
            })
            if verbose:
                print(f"  [orphan] SOURCE (empty): {info['kb']}/{info['name']}")
            continue   # empty source = orphan
        if src.lower() in EXTERNAL_SOURCES or src.lower().startswith("system:"):
            continue   # known external/virtual source — always valid
        if is_external_source_name(src, all_sources):
            continue   # matches a real archive file (e.g. m-code.pdf, dax.pdf)
        if not source_matches_file(src, all_sources):
            orphans.append({
                "type":  "SOURCE orphan (file missing)",
                "kb":    info["kb"],
                "note":  info["name"],
                "path":  note_path,
                "note_source_field": src,
            })
            if verbose:
                print(f"  [orphan] SOURCE: {info['kb']}/{info['name']}  source={src!r}")
    return orphans


def find_registry_orphans(notes: dict[str, dict], registry: dict[str, dict],
                          all_sources: set[str],
                          verbose: bool = False) -> list[dict]:
    """Sources in _INGESTED.md but no KB note has a matching source: field."""
    orphans = []
    # Build set of source values that ARE referenced by notes (normalised)
    referenced = {normalise_source(info["source"]) for info in notes.values() if info["source"]}

    for filename, reg_info in registry.items():
        status = reg_info["status"]
        if status in ("rejected",):
            continue
        # Normalise filename to match note source values
        norm = normalise_source(filename)
        # Also check the raw filename (some sources stored without .md in registry)
        bare = filename.rsplit(".md", 1)[0].lower().rstrip()
        if norm in referenced or bare in referenced:
            continue
        # 2. Substring match: registry filename is a short prefix of a note source value
        #    e.g. registry="Beyond VLOOKUP", note source="Beyond VLOOKUP: Unleashing..."
        #    Both sides are already normalised, so direct string comparison works.
        if any(norm in ref or ref in norm for ref in referenced):
            continue
        # 3. Token-overlap match: ≥4 tokens from registry name appear in any note source
        #    Handles sources where the registry entry is slightly different from the
        #    note's source: field (e.g. "Tejwani (2026)" vs "(Tejwani, 2026-01-19)").
        #    Also handles wikilink slugs: note source might be
        #    "beginning-big-data-with-power-bi-and-excel-2013-dunlop" (no spaces) while
        #    registry tokens are "beginning", "big data", etc. We split on hyphens AND
        #    spaces so both sides use the same vocabulary.
        reg_tokens = set(norm.split())
        if len(reg_tokens) >= 3:
            matched = False
            for ref in referenced:
                ref_lower = ref  # already normalised/lower'd
                # Build ref token set — split on spaces AND hyphens
                # This normalises "power-bi" to {"power", "bi"} and
                # "beginning-big-data" to {"beginning", "big", "data"}
                ref_token_set = {
                    tok
                    for seg in ref_lower.split()
                    for tok in seg.split("-")
                    if tok
                }
                # Word-in-token containment: each registry word is a substring of ref.
                # Count how many of the registry's distinctive tokens appear in ref.
                # This handles hyphen-slug sources where tokens are merged into one word.
                # Stop-words ("and", "with", "the", etc.) don't count toward the threshold.
                stop_words = {"and", "the", "with", "in", "for", "of", "to", "a", "an", "is", "it"}
                content_reg = {t for t in reg_tokens if t not in stop_words}
                content_matches = sum(1 for t in content_reg if t in ref_lower)
                if content_matches >= max(2, len(content_reg) - 2):
                    matched = True
                    break
                # Token overlap (split on spaces and hyphens)
                overlap = len(reg_tokens & ref_token_set)
                if overlap >= max(3, len(reg_tokens) - 2):  # allow up to 1 missing token
                    matched = True
                    break
            if matched:
                continue
            orphans.append({
                "type":   "REGISTRY orphan",
                "source": filename,
                "status": status,
                "hint":   "no note has a source: field matching or overlapping with this registry entry",
            })
            if verbose:
                print(f"  [orphan] REGISTRY: {filename}")
            continue
        orphans.append({
            "type":   "REGISTRY orphan",
            "source": filename,
            "status": status,
            "notes":  reg_info["notes"],
        })
        if verbose:
            print(f"  [orphan] REGISTRY: {filename}  status={status}")
    return orphans


# ── output formatters ─────────────────────────────────────────────────────────

def print_orphans(orphans: list[dict], title: str) -> None:
    if not orphans:
        print(f"  None")
        return
    print(f"\n  {len(orphans)} orphan(s):")
    for o in orphans:
        p = Path(o["path"]) if isinstance(o["path"], str) else o["path"]
        print(f"    • {p.relative_to(VAULT_DIR)}  [{o['type']}]")
        if o.get("note_source_field") == "":
            print(f"      → source: field is empty — add source: to frontmatter")
        elif "file missing" in o.get("type", ""):
            print(f"      → source: \"{o.get('note_source_field','')}\" not in Inbox or InboxArchive")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find orphan notes: INDEX orphans, SOURCE orphans, REGISTRY orphans."
    )
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print every note as it is scanned")
    parser.add_argument("--fix", action="store_true",
                        help="Propose INDEX.md wikilink additions for INDEX orphans")
    parser.add_argument("--source", "-s", metavar="FILENAME",
                        help="Check a specific source instead of full scan")
    args = parser.parse_args()

    print("=== find_orphans.py — Vault Orphan Scan ===\n")

    # ── fast path: single source check ─────────────────────────────────────────
    if args.source:
        src_name = args.source.strip()
        if not src_name.endswith(".md"):
            src_name += ".md"
        all_src = get_all_source_files()
        reg     = get_registry_sources()

        in_inbox    = (INBOX_DIR / src_name).exists()
        in_archive  = any(
            (ARCHIVE_DIR / src_name).exists() or
            (ARCHIVE_DIR / "2026-07" / src_name).exists()
        )
        in_registry = src_name in reg
        notes_having_this_source = [
            str(p) for p, i in scan_all_notes().items()
            if i["source"] == src_name
        ]

        print(f"Source : {src_name}")
        print(f"  In Inbox        : {in_inbox}")
        print(f"  In Archive      : {in_archive}")
        print(f"  In Registry     : {in_registry}  (status={reg.get(src_name, {}).get('status','?')})")
        print(f"  Notes referencing: {len(notes_having_this_source)}")
        for n in notes_having_this_source:
            print(f"    {Path(n).relative_to(VAULT_DIR)}")
        return 0

    # ── full scan ───────────────────────────────────────────────────────────────
    print("Scanning notes...")
    notes        = scan_all_notes(verbose=args.verbose)
    all_sources  = get_all_source_files()
    registry     = get_registry_sources()
    print(f"  {len(notes)} notes scanned across {len(KB_NAMES)} KBs\n")

    # ── full scan ───────────────────────────────────────────────────────────────
    # Index orphans (notes not in their KB's INDEX.md)
    print("─── INDEX orphans (notes not in their KB's INDEX.md) ───")
    idx_orphans = find_index_orphans(notes, verbose=args.verbose)
    print_orphans(idx_orphans, "INDEX")

    # Source orphans
    print("\n─── SOURCE orphans (source: field has no matching file) ───")
    src_orphans = find_source_orphans(notes, all_sources, verbose=args.verbose)
    print_orphans(src_orphans, "SOURCE")

    # Registry orphans
    print("\n─── REGISTRY orphans (source in _INGESTED.md, no note references it) ───")
    reg_orphans = find_registry_orphans(notes, registry, all_sources, verbose=args.verbose)
    total_reg_orphan_files = len(reg_orphans)
    if not reg_orphans:
        print("  None")
    else:
        print(f"\n  {len(reg_orphans)} orphan(s):")
        for o in reg_orphans:
            print(f"    • {o['source']}  [status: {o['status']}]")

    # ── folder-structure check ───────────────────────────────────────────────────
    print("\n─── Folder structure ───")
    unexpected_inbox_dirs = []
    for entry in INBOX_DIR.iterdir():
        if entry.is_dir():
            unexpected_inbox_dirs.append(entry.name)
    if unexpected_inbox_dirs:
        print(f"\n  Unexpected directories in 00.Inbox/ (should be files + _INGESTED.md only):")
        for name in unexpected_inbox_dirs:
            print(f"    • 00.Inbox/{name}/")
        print(f"\n  Fix: merge any archive files into 99.System/InboxArchive/YYYY-MM/, then remove the directory.")
    else:
        print("  00.Inbox/ structure: OK (no unexpected subdirectories)")

    # ── INDEX fix proposals ────────────────────────────────────────────────────
    if args.fix and idx_orphans:
        print("\n─── INDEX fix proposals ───")
        for kb in KB_NAMES:
            kb_orphans = [o for o in idx_orphans if o["kb"] == kb]
            if not kb_orphans:
                continue
            print(f"\n  {kb}/Wiki/INDEX.md — add these wikilinks:")
            for o in kb_orphans:
                stem = Path(o["path"]).stem
                print(f"    [[{stem}]]")

    # ── summary ────────────────────────────────────────────────────────────────
    total = len(idx_orphans) + len(src_orphans) + total_reg_orphan_files
    print(f"\n{'='*50}")
    print(f"INDEX orphans   : {len(idx_orphans)}")
    print(f"SOURCE orphans : {len(src_orphans)}")
    print(f"REGISTRY orphans: {total_reg_orphan_files}")
    print(f"Total orphans  : {total}")
    if total == 0:
        print("No orphans found.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
