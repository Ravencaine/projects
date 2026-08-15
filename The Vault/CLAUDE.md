# CLAUDE.md — Project-Level Operating Instructions

## Purpose

This workspace is a structured knowledge base for documenting code concepts: functions, patterns, errors, workflows, and more. It contains one or more topic-specific knowledge bases under `01.Knowledge/`, each with its own wiki, outputs, and changelog.

This file covers project-level rules: how knowledge bases are structured, how questions produce reports, how health checks run, and how output is presented. For the note ingestion protocol — classification, split rules, mandatory sections, quality checks, and note-writing behaviour — see the authoritative skill at `99.System/Vault Guides/SKILL_note_ingestion.md`. For a quick routing shortcut, use `99.System/Vault Guides/INGESTION_INDEX.md`. Keep this file thin: do not restate the full ingestion protocol or template rules here unless they are needed as a project-level exception.

---

## Section 1 — Knowledge Base Structure

Each knowledge base is one folder inside `01.Knowledge/`. The folder name matches the user's requested name exactly — preserve casing, spaces, and punctuation as given (e.g., `Power BI`, `DAX Code`).

```
[topic]
├── Wiki/           — compiled, cross-linked notes
│   ├── INDEX.md
│   ├── QUESTIONS.md — open threads, gaps, held tensions
│   └── *.md        — individual notes (function, pattern, etc.)
├── Outputs/        — generated reports from questions
└── CHANGELOG.md    — running log; top entry = current state
```

**Valid KBs:** `Data Modeling` · `DAX Code` · `Excel` · `Power Automate` · `Power BI` · `Power Query` · `VBA`

---

## Section 1b — The Inbox

Raw source material lands in the project-level `00.Inbox/` folder (the Inbox), not in individual KB folders. On ingestion, Claude reads from the Inbox, classifies the material, and routes each note to the correct Wiki based on topic.

The Inbox contains:
- `00.Inbox/`                — unprocessed source material (verbatim, never edited)
- `00.Inbox/_INGESTED.md`    — registry with columns: file, added date, routed to KB, status, location

Valid status values: `pending` | `processing` | `archived` | `converted` | `rejected`

Use `rejected` for source material reviewed and determined out of scope or irrelevant to any existing KB. The health check flags sources pending for more than 90 days as candidates for `rejected`; the user makes the rejection call.

**Archive policy:** Sources stay in Inbox after notes are written. Archiving is optional and done only via `99.System/Scripts/safe_archive.py` — never raw `mv`. The script checks that notes exist in the KB before archiving; if notes are missing it blocks the move and exits non-zero.

### Inbox Routing Rules

Before ingesting any source from the Inbox, auto-route by filename keyword:

| Keyword pattern | Target KB |
|----------------|-----------|
| `Power BI`, `DAX`, `PowerPivot` | `01.Knowledge/Power BI/` or `DAX Code/` |
| `Power Query`, `M code`, `Get Data` | `01.Knowledge/Power Query/` |
| `Excel`, `VBA`, `xlsx`, `spreadsheet` | `01.Knowledge/Excel/` or `VBA/` |
| `Data Model`, `star schema`, `dimension` | `01.Knowledge/Data Modeling/` |
| Default (no match) | ask the user |

**MANDATORY video check:** Before ingesting any source, scan for YouTube/video URLs (`youtube.com`, `youtu.be`, `.mp4`, `.mkv`). If a video is found, run `video-transcriber-skill` first — ingest the full transcript, never captions.

Route rules run BEFORE the Pass 1 inventory. When a source spans multiple domains, list all target KBs and ask the user to confirm the primary routing.

---

## Section 2 — Adding Notes to a Knowledge Base

Two ingestion modes exist. Both follow the two-pass protocol in `99.System/Vault Guides/SKILL_note_ingestion.md`.

**Low-token: drop and file.** Share code, error messages, snippets, or URLs. Claude classifies the material, writes the note, and files it. Best for single focused items.

**High-token: guided ingest.** Paste dense material (a function library, a transcript, a tutorial walkthrough). Claude asks framing questions, classifies each distinct piece, proposes splits if needed, and writes notes one at a time. Best when material contains multiple notes worth separating.

---

## Section 3 — The Ingestion Skill

The authoritative ingestion protocol lives in `99.System/Vault Guides/SKILL_note_ingestion.md`. It uses a **two-pass extraction system** to maximize coverage:

- **Pass 1 (Discovery & Inventory):** Scan the source across all 9 templates BEFORE writing anything. Produce a structured inventory table — type, name, location, status. The inventory is a contract; every item must be written or extended.
- **Pass 2 (Extraction):** Work through the inventory systematically. For each item, perform the merge/extend check against the target KB, then write using the appropriate template.

**Why two-pass?** Discovery and writing are different cognitive modes. When mixed together, models tend to "close early" — declare done before exhausting the source. Separating them with a mandatory inventory phase forces complete coverage.

The full protocol defines:
- Eleven supported note types (atomic, author, function, pattern, error, snippet, gotcha, comparison, workflow, reference, source)
- The two-pass protocol with mandatory inventory phase
- A classification decision tree
- Split rules for multi-note source material
- Merge protocol for extending existing notes
- Mandatory frontmatter and body sections per note type
- Twelve quality checks to run before delivering any note
- User interaction rules including the INGESTION COMPLETE summary block
- Sixteen behaviours the skill must never do
- Trigger phrases that activate the skill

The canonical note templates live alongside the skill in `99.System/Vault Guides/`:

| Template file | note_type |
|---------------|-----------|
| `template_atomic.md` | atomic |
| `template_comparison.md` | comparison |
| `template_error.md` | error |
| `template_function.md` | function |
| `template_gotcha.md` | gotcha |
| `template_pattern.md` | pattern |
| `template_reference.md` | reference |
| `template_snippet.md` | snippet |
| `template_workflow.md` | workflow |

---

## Section 4 — Asking Questions

Pose questions against the corpus. Every question becomes a written report in `Outputs/`. No exceptions — the point is to compound insight over time, not just answer in chat.

When you ask a question:

1. Read `Wiki/INDEX.md` for the relevant KB. Then grep the KB's Wiki notes with `search_files` for topic keywords — this is the correct retrieval path.
2. Write a report to `Outputs/` covering:
   - The question, restated cleanly
   - The answer, structured for re-reading
   - Citations to specific Wiki articles (and inbox source files where they were the primary source)
   - Tensions or contradictions surfaced across the corpus
   - Open questions or next-move suggestions
3. End the chat summary with a link to the report file.
4. Reports follow the same writing standards as notes.

**Report naming:** `YYYY-MM-DD_query-slug.md`, kebab-case slug, lowercase. If two reports share a date, append `-v2`, `-v3`, etc.

**Skip the report** only when the user explicitly says "don't file this" or "just answer in chat."

---

## Section 5 — Health Check Skill

The `knowledge-base-health-check-skill` audits each knowledge base. It runs on demand when asked ("run a health check", "audit the [name] KB", "check the wiki").

Each run audits one knowledge base at a time. It auto-fixes routine drift (writing-rules violations, broken backlinks, em-dash bullet patterns, missing frontmatter, contradiction cross-references), auto-drafts up to three suggested new articles where there is enough evidence, and flags only judgement calls (out-of-scope source material, output promotion candidates, stale rewrites) in the knowledge base's CHANGELOG.

---

## Section 6 — Output Presentation Rule

Always present notes with their file paths as clickable links (`computer://` or `file://` URI). Markdown file links are the standard delivery format. Do not paste the full note body into chat unless the user explicitly asks.

---

## Section 7 — Project-Level Behaviour Rules

These rules apply project-wide, above and beyond the ingestion-specific rules in the skill file.

**RULE-1:** When `/note-ingestion` is triggered, load and follow `99.System/Vault Guides/SKILL_note_ingestion.md`. Do not re-derive the protocol from memory.

**RULE-2:** When writing a note, use the canonical template from `99.System/Vault Guides/template_<note_type>.md`. Do not improvise the section structure.

**RULE-3:** Never write a note without first confirming which knowledge base it belongs to. If only one KB exists, state the assumption.

**RULE-4:** Split aggressively. No cap on notes created. Every distinct concept gets its own note.

**RULE-5:** Before writing a new note, check whether a similar note already exists in the target knowledge base's Wiki. If one does, extend the existing note with the new information rather than creating a duplicate. Merge overlapping content; don't leave two notes saying nearly the same thing. See `SKILL_note_ingestion.md` Section 4b for the full merge protocol.

**RULE-6:** Archive source only after ALL notes are written and saved. Never archive a partially-ingested source.

**RULE-7:** Writing rules (bullet style, em-dash patterns, prose conventions) are defined in the health check skill. Run the skill to auto-fix drift; do not manually enforce rules that the skill handles automatically.

**RULE-9:** Delete temporary one-off scripts when they have completed their task. Never leave throwaway scripts sitting in the workspace.

**RULE-10:** Permanent reusable code (Python scripts, utilities, tools) goes in `99.System/Scripts/`. Ask before creating new files there. Temporary scripts must never be placed in that folder.

**RULE-11:** No files in the vault root. Every file belongs in a named subfolder — never create loose files at `The Vault/` level.

**RULE-12:** Never create new folders without explicit permission. If a folder is needed, ask first. Do not infer or assume.
