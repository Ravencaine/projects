"""
Build INDEX.md files for 5 KBs in The Vault.
Reads frontmatter from each .md file, categorizes them, and generates INDEX.md.
Also updates CHANGELOG.md for each KB.
"""
import os
import re
import frontmatter
from datetime import datetime

VAULT_ROOT = r"C:\Users\krlsa\Documents\00 Projects\The Vault"

# KB configurations
KBS = [
    {
        "name": "Power BI",
        "folder": "Power BI",
        "categories": {
            "Data Modeling": ["data model", "schema", "dimension", "fact", "star", "snowflake", "relationship", "normaliz", "denormaliz"],
            "Visualization & Reports": ["visual", "chart", "report", "dashboard", "page", "tooltip", "slicer", "filter", "bookmark"],
            "DAX & Measures": ["dax", "measure", "calculated", "kpi", "metric", "row-level", "rlsi"],
            "Data Sources & Connectivity": ["data source", "connector", "import", "directquery", "live", "gateway", "odata", "api", "sharepoint", "excel"],
            "Administration & Security": ["admin", "security", "rls", "workspace", "app", "publish", "deployment", "pipeline", "sensitivity"],
            "Power Query & Data Prep": ["power query", "m language", "m code", "transform", "clean", "query editor", "parameter"],
            "Performance & Optimization": ["performance", "optimiz", "refresh", "composite", "aggregat", " VertiPaq", "storage mode"],
        },
    },
    {
        "name": "Power Query",
        "folder": "Power Query",
        "categories": {
            "Core Functions & Operators": ["function", "operator", "builtin", "text.", "number.", "date.", "datetime", "list.", "record."],
            "Transformations & Shaping": ["transform", "pivot", "unpivot", "transpose", "group", "merge", "append", "combine", "split", "extract", "format"],
            "M Code & Advanced": ["m code", "m language", "let", "in ", "custom function", "recursive", "performance", "optimiz"],
            "Data Types & Schema": ["data type", "column type", "schema", "inference", "casting", "null", "blank"],
            "Connectors & Data Sources": ["connector", "source", "database", "api", "web", "folder", "excel", "csv", "sharepoint", "odata", "rest api"],
            "Parameters & Variables": ["parameter", "variable", "function param", "optional", "required"],
        },
    },
    {
        "name": "Excel",
        "folder": "Excel",
        "categories": {
            "Formulas & Functions": ["formula", "function", "vlookup", "xlookup", "index", "match", "sumif", "countif", "if(", "let("],
            "Pivot Tables & Analysis": ["pivot", "power pivot", "slicer", "timeline", "grouping", "calculated field"],
            "Data Visualization": ["chart", "graph", "conditional format", "sparkline", "data bar"],
            "Data Tools & Power Query": ["power query", "get & transform", "data cleaning", "text to column", "remove duplicate"],
            "VBA & Automation": ["vba", "macro", "automation", "scripting", "userform"],
        },
    },
    {
        "name": "Data Modeling",
        "folder": "Data Modeling",
        "categories": {
            "Star Schema & Dimensions": ["star schema", "dimension", "dim_", "slowly changing", "scd", "type 1", "type 2", "hierarchy", "parent-child"],
            "Fact Tables & Metrics": ["fact", "fact_", "measure", "additive", "semi-additive", "non-additive", "grain"],
            "Relationships & Cardinality": ["relationship", "cardinality", "one-to-many", "many-to-many", "cross-filter", "bi-directional"],
            "Time Intelligence": ["date table", "calendar", "time intelligence", "fiscal", "ytd", "mtd", "period", "date dimension"],
            "Best Practices & Patterns": ["best practice", "pattern", "design", "modeling technique", "data vault", "normalize"],
        },
    },
    {
        "name": "VBA",
        "folder": "VBA",
        "categories": {
            "Macros & Procedures": ["sub", "macro", "procedure", "routine", "automation"],
            "Functions & Modules": ["function", "module", "public", "private", "scope"],
            "UserForms & Controls": ["userform", "form", "control", "button", "textbox", "combobox", "listbox"],
            "Objects & Collections": ["object", "collection", "workbook", "worksheet", "range", "cell", "application"],
            "Error Handling & Debugging": ["error", "on error", "debug", "try", "catch", "exception"],
        },
    },
]


def get_frontmatter(filepath):
    """Parse frontmatter from a markdown file."""
    try:
        post = frontmatter.parse(open(filepath, encoding="utf-8").read())
        return post[1], post[0]
    except Exception:
        return "", {}


def extract_title_from_content(content):
    """Extract the first # heading as title fallback."""
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def slugify(text):
    """Convert text to a safe filename slug."""
    text = text.lower().replace(" ", "-")
    return re.sub(r'[^a-z0-9\-]', '', text)


def get_description(content, filename, title):
    """Extract a short description from note content."""
    # Strip frontmatter
    content = re.sub(r'^---[\s\S]*?---\n', '', content)
    # Strip markdown headings
    content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
    # Strip markdown links
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    # Strip code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    # Strip inline code
    content = re.sub(r'`([^`]+)`', r'\1', content)
    # Strip images
    content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', content)
    # Strip blockquotes
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    # Strip horizontal rules
    content = re.sub(r'^[-*_]{3,}\s*$', '', content, flags=re.MULTILINE)
    # Collapse whitespace
    content = re.sub(r'\s+', ' ', content).strip()
    # Take first sentence or 150 chars
    if len(content) > 200:
        desc = content[:200]
        last_period = desc.rfind('.')
        last_newline = desc.rfind(' ')
        cut = max(last_period, last_newline)
        if cut > 50:
            desc = desc[:cut + 1]
        else:
            desc = desc[:150].rstrip() + "..."
    else:
        desc = content
    return desc if desc else title


def match_category(note_title, note_tags, note_type, content, kb_config):
    """Match a note to a category based on keywords."""
    combined = f"{note_title} {' '.join(note_tags)} {note_type} {content[:2000]}".lower()
    best_cat = "General"
    best_score = 0
    for cat_name, keywords in kb_config["categories"].items():
        score = sum(1 for kw in keywords if kw.lower() in combined)
        if score > best_score:
            best_score = score
            best_cat = cat_name
    return best_cat


def build_index(kb_config):
    """Build INDEX.md for a single KB."""
    kb_name = kb_config["name"]
    kb_folder = kb_config["folder"]
    wiki_path = os.path.join(VAULT_ROOT, "01.Knowledge", kb_folder, "Wiki")

    if not os.path.exists(wiki_path):
        print(f"  [SKIP] Wiki folder not found: {wiki_path}")
        return 0

    # Collect all .md files (excluding INDEX.md)
    md_files = [f for f in os.listdir(wiki_path)
                if f.endswith(".md") and f.lower() != "index.md"
                and f.lower() != "questions.md"]

    print(f"  Scanning {len(md_files)} notes in {kb_name}...")

    # Process each file
    notes = []
    for fname in md_files:
        fpath = os.path.join(wiki_path, fname)
        content, metadata = get_frontmatter(fpath)

        title = metadata.get("title", "")
        if not title:
            title = extract_title_from_content(content)
        if not title:
            title = fname.replace(".md", "").replace("-", " ").replace("_", " ").title()

        tags = metadata.get("tags", []) or []
        if isinstance(tags, str):
            tags = [tags]
        note_type = metadata.get("note_type") or ""

        desc = get_description(content, fname, title)

        category = match_category(title, tags, note_type, content, kb_config)

        notes.append({
            "filename": fname,
            "title": title,
            "description": desc,
            "category": category,
        })

    # Group by category
    categories_order = list(kb_config["categories"].keys())
    grouped = {cat: [] for cat in categories_order}
    grouped["General"] = []

    for note in notes:
        cat = note["category"]
        if cat not in grouped:
            grouped["General"] = []
        grouped[cat].append(note)

    # Remove empty categories, put General last
    used_cats = [cat for cat in categories_order if grouped.get(cat)] + \
                (["General"] if grouped.get("General") else [])

    # Build INDEX.md content
    lines = []
    lines.append("---")
    lines.append("created: 2026-08-02")
    lines.append("updated: 2026-08-02")
    lines.append("note_type: index")
    lines.append(f"tags: [{kb_name.lower().replace(' ', '-')}, index]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {kb_name} - Knowledge Base Index")
    lines.append("")
    lines.append(f"This is the index for the {kb_name} knowledge base. {len(notes)} notes grouped by type.")
    lines.append("")

    for cat in used_cats:
        cat_notes = grouped[cat]
        lines.append(f"## {cat}  ({len(cat_notes)} notes)")
        lines.append("")
        lines.append("| Note | Description |")
        lines.append("|------|-------------|")
        for note in cat_notes:
            desc_lines = note["description"].split("\n")
            first_desc = desc_lines[0].strip()
            # Escape pipes in description
            first_desc = first_desc.replace("|", "\\|")
            lines.append(f"| [[{note['filename']}]] | {first_desc} |")
        lines.append("")

    index_content = "\n".join(lines)

    # Write INDEX.md
    index_path = os.path.join(wiki_path, "INDEX.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"  Wrote INDEX.md: {index_path} ({len(notes)} notes, {len(used_cats)} categories)")

    # Update CHANGELOG.md
    changelog_path = os.path.join(VAULT_ROOT, "01.Knowledge", kb_folder, "CHANGELOG.md")
    new_entry = (
        "## 2026-08-02 — INDEX.md created\n"
        f"\nINDEX.md created covering {len(notes)} notes across {len(used_cats)} categories.\n"
    )

    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as f:
            changelog_content = f.read()

        # Check if entry already exists
        if "INDEX.md created" in changelog_content and "2026-08-02" in changelog_content:
            print(f"  CHANGELOG already has 2026-08-02 entry, skipping update")
        else:
            # Find the first ## heading after the frontmatter
            header_end = changelog_content.find("\n# CHANGELOG")
            if header_end == -1:
                changelog_content = new_entry + "\n" + changelog_content
            else:
                hash_pos = changelog_content.find("## ", header_end)
                if hash_pos == -1:
                    changelog_content = new_entry + "\n" + changelog_content
                else:
                    changelog_content = changelog_content[:hash_pos] + new_entry + "\n" + changelog_content[hash_pos:]

            with open(changelog_path, "w", encoding="utf-8") as f:
                f.write(changelog_content)
            print(f"  Updated CHANGELOG.md")
    else:
        # Create changelog
        changelog_content = "---\ncreated: 2026-08-02\n---\n\n# CHANGELOG\n\n" + new_entry
        with open(changelog_path, "w", encoding="utf-8") as f:
            f.write(changelog_content)
        print(f"  Created CHANGELOG.md")

    return len(notes)


def main():
    print("Building INDEX.md files for The Vault KBs...\n")

    # Install frontmatter if needed
    try:
        import frontmatter
    except ImportError:
        print("Installing python-frontmatter...")
        import subprocess
        subprocess.run(["python", "-m", "pip", "install", "python-frontmatter"], check=True)
        import frontmatter

    for kb in KBS:
        print(f"Processing: {kb['name']}")
        count = build_index(kb)
        print(f"  Done: {count} notes\n")

    print("All INDEX.md files built successfully!")


if __name__ == "__main__":
    main()
