#!/usr/bin/env python3
"""
Persistence script for extract-implicit-knowledge.

Reads analysis-batch-*.json from the extraction cache, deduplicates against
merge-state.json, and writes Obsidian notes into the KB.

Usage:
    python persist-as-notes.py <kb-path>

Output:
    - Notes written to <KB>/Wiki/Implicit/Entities/, Claims/, Edges/<type>/
    - merge-state.json updated
    - <KB>/Wiki/INDEX.md extended under ## Implicit Knowledge
    - <KB>/Outputs/<YYYY-MM-DD>_implicit-extraction-<kb>.md report

Exit codes:
    0  success
    1  usage / no cache found
    2  partial failure (some notes written, some failed)
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

VAULT_ROOT = Path(__file__).parent.parent.parent.parent
SKILL_DIR = Path(__file__).parent.resolve()
CACHE_DIR = VAULT_ROOT / ".extraction_cache"
OUTPUTS_DIR = "Outputs"  # relative to KB root


def resolve_kb(kb_path: str | Path) -> tuple[Path, Path, str]:
    """Resolve KB path to (kb_root, wiki_root, kb_slug)."""
    VAULT_ROOT = Path(__file__).parent.parent.parent.parent
    kb_path_raw = Path(kb_path).expanduser()
    if kb_path_raw.name.lower() == "wiki":
        kb_path_raw = kb_path_raw.parent
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
            kb_path = kb_path_raw.resolve()
    else:
        kb_path = kb_path_raw.resolve()
    if kb_path.name.lower() == "wiki":
        kb_path = kb_path.parent
    if not kb_path.is_absolute():
        candidates = [
            VAULT_ROOT / "01.Knowledge" / kb_path,
            VAULT_ROOT / kb_path,
        ]
        for cand in candidates:
            if cand.exists():
                kb_path = cand
                break
    wiki_root = kb_path / "Wiki"
    kb_slug = kb_path.name.lower().replace(" ", "-")
    return kb_path, wiki_root, kb_slug


# ---------------------------------------------------------------------------
# Slug generation
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Convert a name to a kebab-case slug suitable for filenames."""
    # Remove non-alphanumeric, collapse spaces/dashes
    text = re.sub(r"[^a-zA-Z0-9\s\-]", "", text)
    text = re.sub(r"[\s_]+", "-", text.strip())
    text = re.sub(r"-+", "-", text.lower())
    return text.strip("-")


def entity_slug(name: str) -> str:
    # Strip leading "entity:" or "entity-" prefix
    clean = re.sub(r"^entity[:\-]\s*", "", name, flags=re.IGNORECASE).strip()
    return f"entity-{slugify(clean)}"


def claim_slug(claim_id: str) -> str:
    # claim:<stem>:<slug> -> claim-<stem>-<slug>
    # e.g. claim:auto-date-time-disable:per-column -> claim-auto-date-time-disable-per-column
    parts = claim_id.split(":")
    if len(parts) >= 3:
        stem = slugify(parts[1])
        short = slugify(parts[2])
        return f"claim-{stem}-{short}"
    return slugify(f"claim-{parts[-1]}")


def relationship_slug(edge: dict) -> str:
    # <source>--<type>--<target>
    src = slugify(edge["source"].replace("article:", ""))
    tgt = slugify(edge["target"].replace("article:", "").replace("entity:", "").replace("claim:", ""))
    return f"{src}--{edge['type']}--{tgt}"


# ---------------------------------------------------------------------------
# Template rendering
# ---------------------------------------------------------------------------

def render_entity(node: dict, kb_name: str, today: str) -> str:
    """Render an entity note from template_entity.md."""
    name = node.get("name", "Unknown Entity")
    summary = node.get("summary", "")
    tags = node.get("tags", [])
    category = tags[1] if len(tags) > 1 else kb_name

    # Extract sources from tags or description
    sources_section = ""
    if "sources" in node:
        sources_lines = []
        for s in node["sources"]:
            article = re.sub(r"^(article|entity|claim):", "", str(s.get("article", "")))
            sources_lines.append(f"- [[{article}]] — {s.get('context', '')}")
        if sources_lines:
            sources_section = "\n\n## Sources in the Vault\n\n" + "\n".join(sources_lines)

    related = ""
    if "related" in node:
        related_links = []
        for r in node["related"]:
            r = re.sub(r"^(article|entity|claim):", "", r)
            related_links.append(f"- [[{r}]]")
        related = "\n\n## Related\n\n" + "\n".join(related_links)

    return f"""---
created: {today}
source: implicit-extraction:{kb_name}
note_type: entity
tags: [entity, {category}, {kb_name}]
---

# {name}

<!-- {summary} -->

## Definition

{summary}{sources_section}{related}
"""


def render_claim(node: dict, kb_name: str, today: str) -> str:
    """Render a claim note from template_claim.md."""
    name = node.get("name", "Unnamed Claim")
    summary = node.get("summary", "")
    tags = node.get("tags", [])
    category = tags[1] if len(tags) > 1 else kb_name

    evidence_lines = []
    if "evidence" in node:
        for ev in node["evidence"]:
            if isinstance(ev, dict):
                article = ev.get("article", "?")
                # Strip article:/entity:/claim: prefix from LLM output
                article = re.sub(r"^(article|entity|claim):", "", article)
                evidence_lines.append(f"- Stated in [[{article}]] — {ev.get('section', 'article')}")
            else:
                evidence_lines.append(f"- {ev}")
    evidence_section = "\n\n## Evidence\n\n" + "\n".join(evidence_lines) if evidence_lines else ""

    related = ""
    if "related" in node:
        related_links = []
        for r in node["related"]:
            r = re.sub(r"^(article|entity|claim):", "", r)
            related_links.append(f"- [[{r}]]")
        related = "\n\n## Related\n\n" + "\n".join(related_links)

    return f"""---
created: {today}
source: implicit-extraction:{kb_name}
note_type: claim
tags: [claim, {category}, {kb_name}]
---

# {name}

<!-- {summary} -->

## Claim

{summary}{evidence_section}{related}
"""


def render_relationship(edge: dict, kb_name: str, today: str,
                        source_name: str, target_name: str) -> str:
    """Render a relationship note from template_relationship.md."""
    edge_type = edge.get("type", "related")
    source_node = edge.get("source", "")
    target_node = edge.get("target", "")
    weight = edge.get("weight", 0.5)
    description = edge.get("description", "")
    evidence = edge.get("evidence", "")

    src_stem = source_node.replace("article:", "").replace("entity:", "").replace("claim:", "")
    tgt_stem = target_node.replace("article:", "").replace("entity:", "").replace("claim:", "")

    description = strip_node_prefix(description)
    evidence = strip_node_prefix(evidence)

    return f"""---
created: {today}
source: implicit-extraction:{kb_name}
note_type: relationship
edge_type: {edge_type}
tags: [{kb_name}, implicit-edge, {edge_type}]
source_node: "[[{src_stem}]]"
target_node: "[[{tgt_stem}]]"
weight: {weight}
---

# {source_name} {edge_type} {target_name}

<!-- {description} -->

## Edge

`[[{src_stem}]]` -- **{edge_type}** -> `[[{tgt_stem}]]`

## Evidence

{description}
{blockquote(evidence)}

## Related

- [[{src_stem}]]
- [[{tgt_stem}]]
"""


def blockquote(text: str) -> str:
    """Wrap text in an Obsidian blockquote."""
    if not text:
        return ""
    lines = text.strip().split("\n")
    return "\n".join(f"> {line}" for line in lines)


def strip_node_prefix(text: str) -> str:
    """Remove article:/entity:/claim: prefix from a wikilink target."""
    return re.sub(r"\[\[((?:article|entity|claim):)", "[[", text)


# ---------------------------------------------------------------------------
# Merge state management
# ---------------------------------------------------------------------------

def load_merge_state(kb_slug: str) -> dict:
    """Load merge-state.json, returns the full dict."""
    state_file = SKILL_DIR / "merge-state.json"
    if not state_file.is_file():
        return {}
    try:
        return json.loads(state_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_merge_state(state: dict) -> None:
    """Save merge-state.json."""
    state_file = SKILL_DIR / "merge-state.json"
    state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# INDEX.md update
# ---------------------------------------------------------------------------

def update_index(wiki_root: Path, new_notes: list[dict], kb_slug: str) -> None:
    """Append ## Implicit Knowledge section to INDEX.md if not already present."""
    index_path = wiki_root / "INDEX.md"
    if not index_path.is_file():
        return

    text = index_path.read_text(encoding="utf-8", errors="replace")

    # Check if section already exists
    if "## Implicit Knowledge" in text:
        # Append entries to existing section
        # Find the start of the section and the start of the next section
        lines = text.split("\n")
        section_start = -1
        section_end = len(lines)
        for i, line in enumerate(lines):
            if line.strip() == "## Implicit Knowledge":
                section_start = i
            elif section_start >= 0 and line.startswith("## "):
                section_end = i
                break

        if section_start < 0:
            return

        # Find where the table ends (blank line after table rows)
        table_end = section_start + 1
        for i in range(section_start + 1, section_end):
            if lines[i].startswith("| ---") or lines[i].startswith("| Note"):
                table_end = i + 1
                break

        # Find end of table (next non-table row)
        while table_end < section_end and (lines[table_end].startswith("|") or not lines[table_end].strip()):
            table_end += 1

        # Add new entries
        new_rows = []
        for note in new_notes:
            name = note.get("name", note.get("id", ""))
            stem = note.get("stem", "")
            desc = note.get("summary", note.get("description", ""))[:120]
            if note.get("noteType") == "relationship":
                desc = f"**{note.get('edge_type', '')}**: {desc}"
            new_rows.append(f"| [[{stem}]] | {desc} |")

        # Insert before section end
        new_lines = lines[:table_end] + new_rows + [""] + lines[table_end:]

    else:
        # Create new section
        new_section = [
            "",
            "## Implicit Knowledge",
            "",
            "| Note | Description |",
            "|------|-------------|",
        ]
        for note in new_notes:
            name = note.get("name", note.get("id", ""))
            stem = note.get("stem", "")
            desc = note.get("summary", note.get("description", ""))[:120]
            if note.get("noteType") == "relationship":
                desc = f"**{note.get('edge_type', '')}**: {desc}"
            new_section.append(f"| [[{stem}]] | {desc} |")
        new_section.append("")

        new_lines = text.split("\n") + new_section

    index_path.write_text("\n".join(new_lines), encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def persist(kb_path: str) -> None:
    kb_root, wiki_root, kb_slug = resolve_kb(kb_path)
    kb_name = kb_root.name  # "Power BI"
    cache_dir = CACHE_DIR / kb_slug
    today = date.today().isoformat()

    # Find analysis batch files
    batch_files = sorted(cache_dir.glob("analysis-batch-*.json"))
    if not batch_files:
        print(f"[persist] No analysis batches found in {cache_dir}", file=sys.stderr)
        sys.exit(1)

    # Load merge state
    state = load_merge_state(kb_slug)
    kb_state = state.get(kb_slug, {})
    existing_entities = set(kb_state.get("entities", {}).keys())
    existing_claims = set(kb_state.get("claims", {}).keys())
    existing_edges = set(kb_state.get("edges", {}).keys())

    # Create directories
    implicit_dir = wiki_root / "Implicit"
    entities_dir = implicit_dir / "Entities"
    claims_dir = implicit_dir / "Claims"
    edges_dir = implicit_dir / "Edges"
    edges_dir.mkdir(parents=True, exist_ok=True)
    entities_dir.mkdir(parents=True, exist_ok=True)
    claims_dir.mkdir(parents=True, exist_ok=True)

    # Node slug functions
    entity_slugs = {}
    claim_slugs = {}

    written_notes: list[dict] = []
    skipped_duplicates: list[dict] = []
    errors: list[str] = []

    # Collect all nodes and edges
    all_nodes: list[dict] = []
    all_edges: list[dict] = []

    for bf in batch_files:
        try:
            batch = json.loads(bf.read_text(encoding="utf-8"))
            all_nodes.extend(batch.get("nodes", []))
            all_edges.extend(batch.get("edges", []))
        except (json.JSONDecodeError, OSError) as e:
            errors.append(f"Failed to read {bf.name}: {e}")

    # Build source_name lookup from batch data
    node_name_map: dict[str, str] = {}
    for node in all_nodes:
        node_name_map[node["id"]] = node.get("name", node["id"])

    # Process entity nodes
    for node in all_nodes:
        node_type = node.get("type") or ""
        node_id = node.get("id", "")
        # Detect by type field OR by id prefix
        is_entity = node_type == "entity" or node_id.startswith("entity:")
        if not is_entity:
            continue
        name = node.get("name", "")
        slug = entity_slug(name)
        if slug in existing_entities:
            skipped_duplicates.append({"type": "entity", "name": name, "slug": slug})
            continue
        try:
            content = render_entity(node, kb_name, today)
            path = entities_dir / f"{slug}.md"
            path.write_text(content, encoding="utf-8")
            node["stem"] = f"Implicit/Entities/{slug}"
            node["noteType"] = "entity"
            node["summary"] = node.get("summary", "")
            written_notes.append(node)
            existing_entities.add(slug)
            entity_slugs[slug] = node["id"]
            # Update merge state
            kb_state.setdefault("entities", {})[slug] = {
                "first_seen": today,
                "articles": node.get("articles", []),
            }
        except Exception as e:
            errors.append(f"Failed to write entity {slug}: {e}")

    # Process claim nodes
    for node in all_nodes:
        # Detect by type field OR by id prefix (LLM may not set type)
        node_type = node.get("type") or ""
        node_id = node.get("id", "")
        is_claim = node_type == "claim" or node_id.startswith("claim:")
        if not is_claim:
            continue
        claim_id = node.get("id", "")
        slug = claim_slug(claim_id)
        if slug in existing_claims:
            skipped_duplicates.append({"type": "claim", "id": claim_id, "slug": slug})
            continue
        try:
            content = render_claim(node, kb_name, today)
            path = claims_dir / f"{slug}.md"
            path.write_text(content, encoding="utf-8")
            node["stem"] = f"Implicit/Claims/{slug}"
            node["noteType"] = "claim"
            node["summary"] = node.get("summary", "")
            written_notes.append(node)
            existing_claims.add(slug)
            claim_slugs[slug] = node["id"]
            kb_state.setdefault("claims", {})[slug] = {
                "first_seen": today,
                "first_article": node.get("first_article", ""),
                "evidence": node.get("evidence", []),
            }
        except Exception as e:
            errors.append(f"Failed to write claim {slug}: {e}")

    # Process implicit edges (builds_on, exemplifies, cites, contradicts)
    implicit_edge_types = {"builds_on", "exemplifies", "cites", "contradicts", "authored_by"}
    for edge in all_edges:
        edge_type = edge.get("type", "")
        if edge_type not in implicit_edge_types:
            continue
        slug = relationship_slug(edge)
        if slug in existing_edges:
            skipped_duplicates.append({"type": "edge", "slug": slug})
            continue

        source_id = edge.get("source", "")
        target_id = edge.get("target", "")
        source_name = node_name_map.get(source_id, source_id.replace("article:", "").replace("entity:", "").replace("claim:", ""))
        target_name = node_name_map.get(target_id, target_id.replace("article:", "").replace("entity:", "").replace("claim:", ""))

        try:
            content = render_relationship(edge, kb_name, today, source_name, target_name)
            edge_dir = edges_dir / edge_type
            edge_dir.mkdir(exist_ok=True)
            path = edge_dir / f"{slug}.md"
            path.write_text(content, encoding="utf-8")
            edge["stem"] = f"Implicit/Edges/{edge_type}/{slug}"
            edge["noteType"] = "relationship"
            edge["summary"] = edge.get("description", "")
            written_notes.append(edge)
            existing_edges.add(slug)
            kb_state.setdefault("edges", {})[slug] = {
                "first_seen": today,
                "weight": edge.get("weight", 0.5),
                "source_node": source_id,
                "target_node": target_id,
            }
        except Exception as e:
            errors.append(f"Failed to write edge {slug}: {e}")

    # Update merge state
    state[kb_slug] = kb_state
    state[kb_slug]["last_run"] = today
    save_merge_state(state)

    # Update INDEX.md
    update_index(wiki_root, written_notes, kb_slug)

    # Write Outputs report
    outputs_dir = kb_root / "Outputs"
    outputs_dir.mkdir(exist_ok=True)
    report_path = outputs_dir / f"{today}_implicit-extraction-{kb_slug}.md"
    entity_count = sum(1 for n in written_notes if n.get("noteType") == "entity")
    claim_count = sum(1 for n in written_notes if n.get("noteType") == "claim")
    edge_count = sum(1 for n in written_notes if n.get("noteType") == "relationship")

    report = f"""---
created: {today}
source: implicit-extraction:{kb_name}
note_type: reference
tags: [{kb_name}, implicit-extraction, report]
---

# Implicit Extraction Report — {kb_name}

## Summary

| Category | Count |
|----------|-------|
| Entities | {entity_count} |
| Claims | {claim_count} |
| Relationships | {edge_count} |
| Duplicates skipped | {len(skipped_duplicates)} |
| Errors | {len(errors)} |

## Written Notes

"""
    for note in written_notes:
        stem = note.get("stem", "")
        name = note.get("name", note.get("id", ""))
        ntype = note.get("noteType", "")
        report += f"- [[{stem}]] — {ntype}: {name}\n"

    if skipped_duplicates:
        report += "\n## Skipped Duplicates\n\n"
        for d in skipped_duplicates:
            report += f"- {d['type']}: {d.get('name', d.get('slug', ''))}\n"

    if errors:
        report += "\n## Errors\n\n"
        for e in errors:
            report += f"- {e}\n"

    report += f"\n---\n*Generated by extract-implicit-knowledge skill*\n"
    report_path.write_text(report, encoding="utf-8")

    # Report to stderr
    print(f"[persist] KB: {kb_name}", file=sys.stderr)
    print(f"[persist] Written: {entity_count} entities, {claim_count} claims, {edge_count} relationships", file=sys.stderr)
    print(f"[persist] Skipped: {len(skipped_duplicates)} duplicates, {len(errors)} errors", file=sys.stderr)
    print(f"[persist] Report: {report_path}", file=sys.stderr)

    if errors:
        sys.exit(2)


def main():
    if len(sys.argv) < 2:
        print("Usage: persist-as-notes.py <kb-path>", file=sys.stderr)
        sys.exit(1)
    persist(sys.argv[1])


if __name__ == "__main__":
    main()
