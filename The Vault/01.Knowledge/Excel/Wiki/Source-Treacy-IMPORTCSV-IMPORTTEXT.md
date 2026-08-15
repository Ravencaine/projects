---
created: 2026-08-10
updated: 2026-08-10
source: Excel IMPORTCSV and IMPORTTEXT Functions Explained
source_url: https://www.myonlinetraininghub.com/excel-importcsv-and-importtext-functions-explained
note_type: source
tags: [excel, importcsv, importtext, dynamic-array, groupby, choosecols, let, power-query, file-import]
---

# Source: Treacy — IMPORTCSV and IMPORTTEXT Functions Explained

> **Type:** tutorial / function reference
> **Author:** Mynda Treacy (MyOnlineTrainingHub)
> **Published:** 2026-02-03
> **URL:** https://www.myonlinetraininghub.com/excel-importcsv-and-importtext-functions-explained
> **Routed to:** Excel
> **Category:** Excel, Dynamic Arrays, File Import, IMPORTCSV, IMPORTTEXT, Power Query Alternative

## Summary

Two new Excel Microsoft 365 functions (Beta Channel) that import CSV and text files directly into the worksheet as dynamic arrays — no Power Query required. IMPORTCSV for comma-separated files; IMPORTTEXT for custom-delimiter or fixed-width text files. Full parameter breakdown including locale, encoding, skip_rows, take_rows. Pattern for chaining with LET + CHOOSECOLS + GROUPBY for in-formula summarization. When to use these vs Power Query.

## Key Claims / Components

1. **IMPORTCSV:** `=IMPORTCSV(path, [skip_rows], [take_rows], [locale])` — CSV import; auto-detects comma delimiter
2. **IMPORTTEXT:** `=IMPORTTEXT(path, [delimiter], [skip_rows], [take_rows], [encoding], [locale])` — custom delimiter or fixed-width `{pos1, pos2, ...}` array; UTF-8 default encoding; locale override for regional formatting
3. **Refresh:** treated as external connections; Refresh All via Data tab; no hidden query editor steps
4. **Advantage:** every import decision visible in formula bar; no background steps; fully transparent and auditable
5. **LET + CHOOSECOLS + GROUPBY:** `LET(data, IMPORTTEXT(...), GROUPBY(CHOOSECOLS(data,2), CHOOSECOLS(data,4), SUM, 3, 1))` — in-formula summarization of imported data; no intermediate tables
6. **When to use vs Power Query:** these functions for single clean files needing transparency; Power Query for multiple files, complex transformations, APIs, databases, SharePoint
7. **Mynda Treacy / MyOnlineTrainingHub:** Excel educator; known for Power Query, Excel functions, and dashboard courses

## Extracted Notes

- [[IMPORTCSV-IMPORTTEXT-Reference]] — `reference` — IMPORTCSV and IMPORTTEXT signatures, parameters, delimiter types, refresh behavior, PQ comparison
- [[IMPORTCSV-CHOOSECOLS-GROUPBY-Summarization-Pattern]] — `pattern` — LET + CHOOSECOLS + GROUPBY on imported data; variants with multiple grouping columns and FILTER
- [[Source-Treacy-IMPORTCSV-IMPORTTEXT]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | Excel IMPORTCSV and IMPORTTEXT Functions Explained • My Online Training Hub.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Notes count | 2 (reference ×1, pattern ×1) |
