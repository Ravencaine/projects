---
created: 2026-08-05
updated: 2026-08-05
source: 4 Tips Work Efficiently Power BI (Isabelle Bittar)
source_url: https://medium.com/the-bi-corner/4-tips-to-work-efficiently-in-power-bi-5a691a460d5f
note_type: source
tags: [power-bi, workflow, measure-folder, selection-panel, bookmarks, parameter-file, git]
---

# 4 Tips Work Efficiently Power BI (Isabelle Bittar)

Four productivity tips from Isabelle Bittar's FP20 Analytics Challenge submission: measure display folders, Selection/Bookmarks panel organization, parameter files to avoid hard-coding, and reusable project assets.

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2024-02-18
> **URL:** https://medium.com/the-bi-corner/4-tips-to-work-efficiently-in-power-bi-5a691a460d5f
> **Routed to:** Power BI

## Summary

Isabelle Bittar (KI Data Science) shares four practices that make Power BI development faster and reports cleaner: (1) centralizing measures in a display folder structure, (2) renaming and grouping elements in the Selection and Bookmarks panels, (3) storing hard-coded values in Excel parameter files or DAX measures instead of inline in formulas, and (4) maintaining reusable asset libraries (DAX, M, templates) instead of rebuilding from scratch each project.

## Key Claims

- A `\_Measures` empty table becomes a measures group for folder-based organization
- Display folders support subfolders via `FolderName\SubFolderName` naming convention
- Renaming elements in the Selection panel accelerates development and eases bookmark management
- Bookmarks should also be grouped — critical when managing many navigation states
- Excel parameter files let business users update thresholds without touching the PBIX
- Color measures (`Color Green = "#2C6D6A"`) ensure palette consistency and enable single-point theme updates
- Reusable asset repos (DAX, M, GitHub) are more maintainable than master PBIX files

## Notable Details

- Display folder assignment happens in Model view → Properties panel → Display folder
- The `CALCULATE(MAX(...), FILTER(...))` pattern retrieves parameter values from disconnected Excel tables
- GitHub recommended as a better alternative to master PBIX files for asset storage
- Isabelle notes: function over perfection — B- changes the world, submit rather than wait for polish

## Extracted Notes

Links to notes derived from this source:

- [[Organizing-Measures-Display-Folders]] — `atomic` — creating a \_Measures table, display folder assignment, subfolder naming
- [[Selection-Bookmarks-Panel-Organization]] — `atomic` — renaming elements, grouping, bookmark group management
- [[Parameter-File-No-Hard-Coding]] — `atomic` — Excel parameter files for business-user-updatable values
- [[Color-Measures-Consistent-Theme]] — `atomic` — storing hex colors in DAX measures for consistency
- [[Reusable-Project-Assets]] — `atomic` — maintaining DAX, M, and template libraries instead of starting from scratch
- [[Author-Isabelle-Bittar]] — `author` — Isabelle Bittar, KI Data Science (3 sources)

## Metadata

| Field | Value |
|-------|-------|
| Source file | 4 Tips to Work Efficiently in Power BI 🛠️.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~1,100 |
| PBIX attachment | [4_Tips_Work_Efficiently_Power_BI.pbix](file:///C:/Users/krlsa/Documents/00%20Projects/The%20Vault/99.System/Attachments/4_Tips_Work_Efficiently_Power_BI.pbix) |
