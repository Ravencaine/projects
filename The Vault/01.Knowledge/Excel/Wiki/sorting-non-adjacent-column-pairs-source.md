---
created: 2026-07-31
updated: 2026-08-02
source: "Sorting Non - Adjacent Column Pairs in Excel.md"
source_url: "https://medium.com/@markchen69/sorting-non-adjacent-column-pairs-in-excel-c8ac3473fee2"
note_type: source
tags: [excel, arrays, dynamic-arrays, sorting, deduplication]
---

# Sorting Non-Adjacent Column Pairs in Excel

Deduplicating and alphabetically sorting pairs of non-adjacent columns using CHOOSE() + UNIQUE() + SORT() without helper columns.

> **Type:** article
> **Author:** Mark Chen
> **Published:** 2025-06-24
> **URL:** https://medium.com/@markchen69/sorting-non-adjacent-column-pairs-in-excel-c8ac3473fee2
> **Routed to:** Excel

## Summary

Excel's UNIQUE() cannot be applied directly to non-adjacent columns. The solution is to wrap the non-adjacent ranges in CHOOSE({1,2}, range1, range2), which merges them into a virtual 2D array that UNIQUE() and SORT() can process together — all without moving or duplicating the source columns.

## Key Claims

1. UNIQUE() rejects non-adjacent column references directly.
2. CHOOSE({1,2}, A2:A100, C2:C100) merges two non-adjacent columns into a virtual array.
3. UNIQUE(CHOOSE({1,2}, A2:A100, C2:C100)) returns all distinct row pairs.
4. SORT(..., {1,2}, {TRUE,TRUE}) sorts by column 1 ascending, then column 2 ascending.
5. No helper columns, no data movement — one formula cell produces the result.

## Notable Details

- {1,2} in SORT() specifies which columns to sort by and in what priority order.
- {TRUE,TRUE} in SORT() sets ascending order for both sort columns.
- The author notes LET() can wrap the formula for performance optimization on large ranges.
- The pattern is portable to Power BI (same function names).

## Extracted Notes

- [[sort-unique-choose-non-adjacent-columns]] — `pattern` — Deduplicate and sort non-adjacent column pairs in one formula
- [[choose-merges-non-adjacent-columns]] — `atomic` — CHOOSE({1,2}, range1, range2) creates a virtual 2D array from non-adjacent columns

## Metadata

| Field | Value |
|-------|-------|
| Source file | 🔄 Sorting Non-Adjacent Column Pairs in Excel.md |
| Ingestion date | 2026-07-31 |
| Word count | ~700 |
