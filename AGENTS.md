# 00 Projects — Project Rules

This is the parent project folder. It serves as the workspace root for all sub-projects under `Documents/00 Projects/`.

> **The Vault:** This project uses `The Vault/` as the active Obsidian knowledge base. All skills, MCP servers, and ingestion workflows point to it.

## Active Vault

**`The Vault/`** — `C:\Users\krlsa\Documents\00 Projects\The Vault`

| Path | Purpose |
|------|---------|
| `00.Inbox/` | Raw source material — unedited |
| `01.Knowledge/` | 6 topic knowledge bases (see below) |
| `99.System/Vault Guides/` | Ingestion skill + 9 note templates |
| `00.Inbox/_INGESTED.md` | Ingestion registry |

### Knowledge Bases

`Data Modeling` · `DAX Code` · `Excel` · `Power BI` · `Power Query` · `VBA`

### MCP Server

`obsidian-vault` → `The Vault/` (configured in `~/.hermes/config.yaml`)

## Active Skills (Hermes)

The following skills are registered as Hermes skills (invoke with `/<skill-name>`):

| Skill | Purpose |
|-------|---------|
| `/note-ingestion` | Ingest source material into the active vault. Full protocol: `99.System/Vault Guides/SKILL_note_ingestion.md`. Triggered by: "ingest this", "add to knowledge base", "create a note from this", etc. |
| `/knowledge-base-health-check` | Audit the active vault's knowledge bases, auto-fix drift, flag judgement calls. Triggered by: "run a health check", "audit the [name] KB". |
| `/epub-utility-skill` | Extract text/content from EPUB files. |
| `/pdf-ocr-utility` | OCR scanned PDFs, create searchable PDFs. |
| `/video-transcriber-skill` | Transcribe videos, create Obsidian notes from video sources. |

## Vault-Wide Rules

- **RULE-1:** When `/note-ingestion` is triggered, load the skill and follow the protocol. Do not improvise note structures or skip classification.
- **RULE-2:** Split aggressively. No cap on notes created. Every distinct concept gets its own note.
- **RULE-3:** Before writing, check if a similar note already exists. Extend it rather than duplicate.
- **RULE-4:** No files in the vault root. Every file belongs in a named subfolder — never create loose files at `The Vault/` level.
- **RULE-5:** Never create new folders without explicit permission. If a folder is needed, ask first. Do not infer or assume.
- **RULE-6:** Archive only via `99.System/Scripts/safe_archive.py` — never raw `mv` or shutil.move. The script verifies that notes exist in the KB before archiving. If no notes are found it exits non-zero and the source stays in Inbox. Archive is optional: sources can remain in Inbox indefinitely after notes are written.
- **RULE-7:** Delete temporary one-off scripts when they have completed their task. Never leave throwaway scripts sitting in the workspace.
- **RULE-8:** Permanent reusable code (Python scripts, utilities, tools) goes in `99.System/Scripts/`. Ask before creating new files in that folder. Never put temporary scripts there.
- **RULE-9:** After every ingestion session, run `find_orphans.py` to catch notes that weren't added to INDEX.md or whose `source:` frontmatter is wrong/missing. Run: `python 99.System/Scripts/find_orphans.py`. Exit code 1 means orphans found — fix them before declaring the session done.
