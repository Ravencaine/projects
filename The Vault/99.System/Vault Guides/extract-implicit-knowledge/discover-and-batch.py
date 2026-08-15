#!/usr/bin/env python3
"""
Deterministic discovery and batching script for extract-implicit-knowledge.

Scans a KB's Wiki folder, resolves wikilinks, derives categories from INDEX.md,
respects merge-state.json for already-extracted articles, groups into batches,
and writes batch JSON files for LLM analysis.

Usage:
    python discover-and-batch.py <kb-path> [scope-glob]

<kb-path> can be:
    - A KB name:           "Power BI"
    - A relative path:     "01.Knowledge/Power BI"
    - A full path:         "The Vault/01.Knowledge/Power BI"
    - A Wiki path:         "Power BI/Wiki" or "01.Knowledge/Power BI/Wiki"

The script normalises all forms to the KB root (e.g. Power BI/Wiki -> Power BI).

[scope-glob] is optional: a glob pattern to restrict which notes are scanned
(e.g. "Wiki/Calculation-*.md"). Default: all *.md under Wiki/.

Output written to: <VAULT>/.extraction_cache/<slug>/

Exit codes:
    0  success
    1  usage / KB not found
    2  no articles found
"""

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

VAULT_ROOT = Path(__file__).parent.parent.parent.parent  # Vault root
SKILL_DIR = Path(__file__).parent.resolve()             # extract-implicit-knowledge/
CACHE_DIR = VAULT_ROOT / ".extraction_cache"


def resolve_kb_root(kb_path: str | Path) -> tuple[Path, Path, str]:
    """Resolve a KB path to (kb_root, wiki_root, kb_slug).

    kb_root: e.g. The Vault/01.Knowledge/Power BI
    wiki_root: e.g. The Vault/01.Knowledge/Power BI/Wiki
    kb_slug: e.g. power-bi
    """
    kb_path_raw = Path(kb_path).expanduser()
    kb_path_str = str(kb_path_raw)

    # If the path ends in /Wiki, strip it
    if kb_path_raw.name.lower() == "wiki":
        kb_path_raw = kb_path_raw.parent

    # Resolve relative paths against the vault root, not the cwd
    if not kb_path_raw.is_absolute():
        candidates = [
            VAULT_ROOT / "01.Knowledge" / kb_path_raw,
            VAULT_ROOT / kb_path_raw,
        ]
        for cand in candidates:
            if cand.exists():
                kb_path = cand.resolve()
                break
        else:
            # No candidate found — treat as absolute path (might be full Windows path)
            kb_path = kb_path_raw.resolve()
    else:
        kb_path = kb_path_raw.resolve()

    wiki_path = kb_path / "Wiki"

    if not wiki_path.exists():
        print(f"Error: Wiki folder not found at {wiki_path}", file=sys.stderr)
        sys.exit(1)

    # KB slug for cache dir
    kb_slug = kb_path.name.lower().replace(" ", "-")
    kb_root = wiki_path.parent

    return kb_root, wiki_path, kb_slug


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
INFRA_FILES = {"index", "changelog", "questions", "log", "soul", "readme", "agents", "claude"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_markdown_case_insensitive(parent: Path, name: str) -> Path:
    """Resolve a markdown filename case-insensitively within one directory."""
    wanted_lower = name.lower()
    for child in sorted(parent.iterdir()):
        if child.is_file() and child.stem.lower() == wanted_lower:
            return child
    return parent / name


def extract_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter as a simple key-value dict."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def extract_h1(text: str) -> str:
    """Extract the first H1 heading."""
    for m in HEADING_RE.finditer(text):
        if len(m.group(1)) == 1:
            return m.group(2).strip()
    return ""


def extract_wikilinks(text: str) -> list[str]:
    """Extract all [[target]] wikilink targets."""
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


def extract_first_paragraph(text: str) -> str:
    """Extract first non-empty paragraph after frontmatter and H1."""
    stripped = FRONTMATTER_RE.sub("", text).strip()
    if not stripped:
        return ""
    lines = stripped.split("\n")
    para: list[str] = []
    for s_raw in lines:
        s = s_raw.strip()
        if not s and not para:
            continue
        if not s and para:
            break
        if s.startswith(">"):
            continue
        if re.match(r"^[-*_]{3,}\s*$", s):
            continue
        if s.startswith("#"):
            if para:
                break
            continue
        para.append(s)
    result = " ".join(para)
    return result[:200] + "..." if len(result) > 200 else result


def build_name_to_stem_map(wiki_root: Path) -> dict[str, str]:
    """Build a case-insensitive map from filename stem to relative stem path.

    Full relative paths map uniquely. Bare basenames map only when unambiguous.
    """
    name_map: dict[str, str] = {}
    basename_counts: dict[str, int] = {}

    for md_file in wiki_root.rglob("*.md"):
        rel = md_file.relative_to(wiki_root)
        stem = rel.with_suffix("").as_posix()
        basename = md_file.stem

        name_map[stem.lower()] = stem
        key = basename.lower()
        basename_counts[key] = basename_counts.get(key, 0) + 1
        name_map[key] = stem

    # Remove ambiguous basename entries
    for key, count in basename_counts.items():
        if count > 1 and key in name_map:
            del name_map[key]

    return name_map


def resolve_wikilink(target: str, name_map: dict[str, str],
                     article_ids: set[str] | None = None) -> str | None:
    """Resolve a wikilink target to an article node ID."""
    key = target.lower().strip()
    if key.startswith("-"):
        return None

    for k in [key, key.split("/")[-1]]:
        stem = name_map.get(k)
        if stem:
            node_id = f"article:{stem}"
            if article_ids is None or node_id in article_ids:
                return node_id
    return None


def parse_index(index_path: Path, name_map: dict[str, str]) -> tuple[list[dict], dict[str, str]]:
    """Parse INDEX.md to extract category→article mapping and category list.

    Returns (categories, article_to_category).
    """
    if not index_path.is_file():
        return [], {}

    text = index_path.read_text(encoding="utf-8", errors="replace")
    categories: list[dict] = []
    current_category: dict | None = None
    article_to_category: dict[str, str] = {}

    for line in text.split("\n"):
        # ## heading = category
        sec_match = re.match(r"^##\s+(.+)$", line)
        if sec_match:
            current_category = {"name": sec_match.group(1).strip(), "articles": []}
            categories.append(current_category)
            continue

        # Collect wikilinks under current section
        if current_category:
            for wl_match in WIKILINK_RE.finditer(line):
                t = wl_match.group(1).strip()
                stem = name_map.get(t.lower())
                if stem:
                    article_to_category[stem.lower()] = current_category["name"]
                current_category["articles"].append(t)

    return categories, article_to_category


def load_merge_state(skill_dir: Path, kb_slug: str) -> dict:
    """Load merge-state.json for the given KB, or return empty dict."""
    state_file = skill_dir / "merge-state.json"
    if not state_file.is_file():
        return {}
    try:
        return json.loads(state_file.read_text(encoding="utf-8")).get(kb_slug, {})
    except (json.JSONDecodeError, OSError):
        return {}


def get_already_extracted_articles(state: dict) -> set[str]:
    """Return the set of article IDs already extracted for this KB."""
    extracted = set()
    for key, val in state.get("entities", {}).items():
        if "articles" in val:
            for a in val["articles"]:
                extracted.add(a.lower())
    for key, val in state.get("claims", {}).items():
        for a in val.get("evidence", []):
            extracted.add(a.lower())
    return extracted


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def discover_and_batch(kb_path: str, scope_glob: str | None = None) -> None:
    kb_root, wiki_root, kb_slug = resolve_kb_root(kb_path)
    index_path = wiki_root / "INDEX.md"
    cache_dir = CACHE_DIR / kb_slug
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Load merge-state to skip already-extracted articles
    state = load_merge_state(SKILL_DIR, kb_slug)
    already_extracted = get_already_extracted_articles(state)

    # Build name resolution map
    name_map = build_name_to_stem_map(wiki_root)
    article_ids: set[str] = set()

    for md_file in wiki_root.rglob("*.md"):
        rel = md_file.relative_to(wiki_root)
        stem = rel.with_suffix("").as_posix()
        # Skip infra files at wiki root level
        if rel.parent == Path(".") and md_file.stem.lower() in INFRA_FILES:
            continue
        article_ids.add(f"article:{stem}")

    # Parse INDEX.md for category mapping
    categories, article_to_category = parse_index(index_path, name_map)

    # Collect articles
    articles: list[dict] = []
    warnings: list[str] = []

    glob_pattern = scope_glob or "*.md"

    for md_file in wiki_root.glob(glob_pattern):
        rel = md_file.relative_to(wiki_root)
        stem = rel.with_suffix("").as_posix()

        # Skip infra files
        if rel.parent == Path(".") and md_file.stem.lower() in INFRA_FILES:
            continue

        # Skip already-extracted articles
        node_id = f"article:{stem}"
        if node_id.lower() in already_extracted:
            continue

        try:
            text = md_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        h1 = extract_h1(text)
        frontmatter = extract_frontmatter(text)
        wikilinks = extract_wikilinks(text)
        summary = extract_first_paragraph(text)

        # Resolve wikilinks
        resolved_wikilinks: list[str] = []
        for wl in wikilinks:
            resolved = resolve_wikilink(wl, name_map, article_ids)
            if resolved:
                resolved_wikilinks.append(resolved)
            else:
                warnings.append(f"Unresolved wikilink: [[{wl}]] in {rel}")

        # Derive category from INDEX lookup
        category = article_to_category.get(stem.lower(), "")

        articles.append({
            "id": node_id,
            "name": h1 or md_file.stem,
            "summary": summary or f"Wiki article: {h1 or md_file.stem}",
            "wikilinks": resolved_wikilinks,
            "wikilink_targets": wikilinks,
            "category": category,
            "filePath": str(rel),
            "tags": frontmatter.get("tags", ""),
            "noteType": frontmatter.get("note_type", ""),
            "source": frontmatter.get("source", ""),
            "content": text[:3000],
        })

    if not articles:
        print(f"[discover] No articles found (kb={kb_slug}, glob={scope_glob})", file=sys.stderr)
        print(f"[discover] Already extracted: {len(already_extracted)} articles", file=sys.stderr)
        sys.exit(2)

    # Group into batches of 10-15, same-category co-location
    BATCH_SIZE = 12

    def category_order(a: dict) -> tuple[int, int]:
        cat_idx = {c["name"]: i for i, c in enumerate(categories)}
        return (cat_idx.get(a["category"], 9999), a["id"])

    articles.sort(key=category_order)

    batches: list[list[dict]] = []
    current_batch: list[dict] = []

    for article in articles:
        if len(current_batch) >= BATCH_SIZE:
            batches.append(current_batch)
            current_batch = []
        current_batch.append(article)

    if current_batch:
        batches.append(current_batch)

    # Write scan.json
    scan = {
        "kb_slug": kb_slug,
        "kb_root": str(kb_root),
        "wiki_root": str(wiki_root),
        "scope_glob": scope_glob,
        "stats": {
            "total_articles": len(articles),
            "already_extracted": len(already_extracted),
            "batches": len(batches),
        },
        "categories": [{"name": c["name"], "count": len(c["articles"])} for c in categories],
        "warnings": warnings[:50],
        "all_node_ids": list(article_ids),
    }

    scan_path = cache_dir / "scan.json"
    scan_path.write_text(json.dumps(scan, indent=2), encoding="utf-8")

    # Write batch files
    for i, batch in enumerate(batches):
        batch_path = cache_dir / f"batch-{i}.json"
        batch_data = {
            "batch": i,
            "kb_slug": kb_slug,
            "articles": batch,
            "all_node_ids": list(article_ids),
            "already_extracted": list(already_extracted),
        }
        batch_path.write_text(json.dumps(batch_data, indent=2), encoding="utf-8")

    # Report
    print(f"[discover] KB: {kb_root.name}", file=sys.stderr)
    print(f"[discover] Articles: {len(articles)}, Batches: {len(batches)}, "
          f"Already extracted: {len(already_extracted)}", file=sys.stderr)
    print(f"[discover] Output: {cache_dir}", file=sys.stderr)
    print(f"[discover] Warnings: {len(warnings)} unresolved wikilinks", file=sys.stderr)


def main():
    if len(sys.argv) < 2:
        print("Usage: discover-and-batch.py <kb-path> [scope-glob]", file=sys.stderr)
        sys.exit(1)

    kb_path = sys.argv[1]
    scope_glob = sys.argv[2] if len(sys.argv) > 2 else None
    discover_and_batch(kb_path, scope_glob)


if __name__ == "__main__":
    main()
