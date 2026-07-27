# Ingestion Index

Quick routing reference for incoming source material.

## Trigger Phrases

Activate the ingestion skill on any of:
- "ingest this"
- "add to knowledge base"
- "create a note from this"
- "document this"
- "save this as a note"
- "run ingestion on"
- "process this source"

## Inbox Routing

| Keyword pattern | Target KB |
|----------------|-----------|
| `Power BI`, `DAX`, `PowerPivot` | `01.Knowledge/Power BI/` or `DAX Code/` |
| `Power Query`, `M code`, `Get Data` | `01.Knowledge/Power Query/` |
| `Excel`, `VBA`, `xlsx`, `spreadsheet` | `01.Knowledge/Excel/` or `VBA/` |
| PKM, `second brain`, `Zettelkasten` | `01.Knowledge/PKM/` |
| `Data Model`, `star schema`, `dimension` | `01.Knowledge/Data Modeling/` |
| Default (no match) | ask the user |

## Key Paths

| | Path |
|---|---|
| Vault root | `The Vault/` |
| Inbox | `00.Inbox/` |
| Archive | `99.System/InboxArchive/YYYY-MM/` |
| Registry | `00.Inbox/_INGESTED.md` |
| Templates | `99.System/Vault Guides/template_*.md` |
| Ingestion skill | `99.System/Vault Guides/SKILL_note_ingestion.md` |
