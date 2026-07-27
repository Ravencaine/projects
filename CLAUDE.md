# 00 Projects — Project Rules

This is the parent project folder. It serves as the workspace root for all sub-projects under `Documents/00 Projects/`.

> **DoubleHelix rules:** This project inherits its knowledge-base protocols from the DoubleHelix vault. See below for active skills and vault paths.

## Active Skills

The following skills are available from anywhere in this project:

| Skill | Purpose |
|-------|---------|
| `/note-ingestion` | Ingest source material into the DoubleHelix knowledge base. Full protocol: see `SKILL_note_ingestion.md`. Triggered by: "ingest this", "add to knowledge base", "create a note from this", etc. |
| `/doublehelix-batch-ingestion` | Process the next 5 queued articles from `batch_queue_next.md`. Triggered by: "ingest the batch", "process the queue". |
| `/llm-wiki` | Query the DoubleHelix vault and produce a written report. Triggered by: "what do I know about X", "search the KB for Z", "find notes about X". |
| `/kb-scaffold` | Scaffold a new knowledge base folder with full structure. Triggered by: "create a new KB", "new knowledge base". |
| `/inbox-maintenance` | Clean the DoubleHelix Inbox — remove duplicates, sanitize filenames. Triggered by: "clean inbox", "tidy inbox", "sanitize filenames". |
| `/wiki-linker` | Build a deterministic link graph over DoubleHelix notes and inject discovered [[wikilinks]] as a "Referenced By" section. Triggered by: "build the link graph", "enrich links", "add missing wikilinks", "wiki-link". |
| `/knowledge-base-health-check` | Audit a DoubleHelix knowledge base, auto-fix drift, flag judgement calls. Triggered by: "run a health check", "audit the [name] KB". |
| `/epub-utility-skill` | Extract text/content from EPUB files. |
| `/pdf-ocr-utility` | OCR scanned PDFs, create searchable PDFs. |
| `/video-transcriber-skill` | Transcribe videos, create Obsidian notes from video sources. |

## DoubleHelix Protocol

The DoubleHelix knowledge base is at `DoubleHelix/`. Its note ingestion protocol is the authoritative reference for creating notes — loaded via `/note-ingestion`.

Key paths (relative to `DoubleHelix/`):
- **Inbox:** `00.Inbox/` — raw source material arrives here
- **Archive:** `99.System/InboxArchive/YYYY-MM/` — ingested sources archived here
- **Registry:** `00.Inbox/_INGESTED.md` — tracks all ingested sources
- **Knowledge bases:** `01.Knowledge/` — organized by topic
- **Templates:** `99.System/Vault Guides/template_*.md`
- **Wiki-linker adapter:** `.tools/wiki-compiler-adapter/` — build link graphs over the vault
- **Ingest skill:** registered as `note-ingestion` (invoke with `/note-ingestion` — Hermes resolves by name, not path)

## MCP Servers

- **obsidian-vault** — points to `DoubleHelix/`; use for vault reads/writes
- **powerbi-modeling-mcp** — Power BI data modeling tools

## Vault-Wide Rules

- **RULE-1:** When `/note-ingestion` is triggered, follow the skill protocol. Do not improvise note structures or skip classification.
- **RULE-2:** Split aggressively. No cap on notes created. Every distinct concept gets its own note.
- **RULE-3:** Before writing, check if a similar note already exists. Extend it rather than duplicate.
- **RULE-4:** Archive source only after ALL notes are written and saved. Never archive a partially-ingested source.