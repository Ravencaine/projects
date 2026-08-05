---
created: 2026-08-01
updated: 2026-08-02
source: "Multiple-Criteria Lookups in Excel Five Methods to Master.md"
source_url: "https://medium.com/@markchen69/multiple-criteria-lookups-in-excel-five-methods-to-master-a6c22aaa5df0"
note_type: source
tags: [excel, lookup, multi-criteria, xlookup, index-match, filter, let, xmatch]
---

# Five Methods to Master Multi-Criteria Lookups — Mark Chen

> **Type:** tutorial
> **Author:** Mark Chen
> **Published:** 2025-05-28
> **URL:** https://medium.com/@markchen69/multiple-criteria-lookups-in-excel-five-methods-to-master-a6c22aaa5df0
> **Routed to:** Excel
> **KB:** Excel

## Summary

Five methods for multi-criteria lookups in Excel, with pros/cons, version requirements, and decision guidance:

1. Helper Column + XLOOKUP/VLOOKUP — universal, fast, requires extra column
2. INDEX/MATCH with array multiplication — no helper columns, Ctrl+Shift+Enter in older Excel
3. XLOOKUP with array multiplication (365) — same logic, cleaner syntax, built-in not-found
4. FILTER (365) — returns all matching rows or first via INDEX
5. LET + XMATCH + INDEX (365) — named sub-expressions, computed once, max performance

## Extracted Notes

- [[index-match-multi-criteria-array]] — `atomic` — INDEX/MATCH with boolean array multiplication; Ctrl+Shift+Enter in older Excel
- [[let-xmatch-index-lookup]] — `atomic` — LET names sub-expressions; XMATCH finds first match; avoids recalculating arrays; IFNA for not-found

## Metadata

| Field | Value |
|-------|-------|
| Source file | Multiple-Criteria Lookups in Excel Five Methods to Master.md |
| Ingestion date | 2026-08-01 |
| Word count | ~700 |
| Level | Intermediate |
| Category | Lookup |
