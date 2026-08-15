---
created: 2026-08-08
updated: 2026-08-08
source: "Analyzing the performance impact of visual calculations"
source_url: https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
author:
  - Marco Russo
  - Alberto Ferrari
published: 2026-07-28
note_type: source
tags: [dax, visual-calculations, performance, sqlbi, densification, summarizecolumns, previous, distinctcount]
---

# Analyzing the Performance Impact of Visual Calculations (SQLBI)

> **Type:** article
> **Author:** Marco Russo & Alberto Ferrari
> **Published:** 2026-07-28
> **URL:** https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
> **Routed to:** DAX Code

## Summary

Visual calculations can improve or degrade report performance depending on the size of the virtual table. With small virtual tables they are faster than measure-based reports; with large ones they are significantly slower due to densification overhead. The article uses DAX Studio server timings on the Contoso model (23M rows in Sales) to demonstrate both cases.

## Key Claims

1. **VCs improve performance when the virtual table is small:** the engine precomputes all values once, then subsequent calculations (e.g., PREVIOUS) run in the formula engine on the virtual table with no further storage engine queries. Example: YoY% with DISTINCTCOUNT — VC: 6s vs Measure: 13s.
2. **VCs degrade performance when the virtual table is large:** densification rebuilds all combinations of row/column values (including BLANK rows eliminated by SUMMARIZECOLUMNS), and the full densified table must be materialized at leaf level regardless of whether matrix rows are expanded. Example: 67 stores × 2,517 products × 10 years (1,686,390 rows) — VC: 62s vs Measure: 15.6s (4× slower).
3. **SUMMARIZECOLUMNS blank elimination conflicts with VC densification:** SUMMARIZECOLUMNS skips rows where all measures are BLANK; VC densification recreates those rows to support cross-joins needed by visual calculation expressions.
4. **Measure-based reports are optimised to compute only visible cells:** collapsed matrix rows are not computed. VCs must always materialize the full densified virtual table at leaf level.
5. **Small-database timings are misleading:** the storage engine overhead is negligible on small datasets, making the VC densification cost appear disproportionately large relative to the measure-based alternative.

## Server Timings Summary

| Scenario | Virtual table size | Measure-based | Visual calc | Winner |
|---|---|---|---|---|
| YoY% DISTINCTCOUNT (# Customers, 11 brands × 10 years) | ~110 rows | 13s | 6s | VC (2× faster) |
| YoY% Sales Amount (67 stores × 2,517 products × 10 years) | 1,686,390 rows | 15.6s | 62s | Measure (4× faster) |

### Small table server timings (C0298-2 — measure-based, 13s total)

- SE CPU: 12,614 ms (96.7%) | FE CPU: 426 ms (3.3%)
- Multiple SE scans, one per year/cell — many storage engine queries
- Rows scanned: ~4,021 per scan

### Small table server timings (C0298-6 — VC, 6s total)

- SE CPU: 457 ms (0.7%) | FE CPU: 67,914 ms (99.3%)
- 1 SE scan only (reads base measure); all subsequent calculations in formula engine
- Rows in SE scan: 1,318,524 | Rows in FE: ~1.3M

### Large table server timings (C0298-5 — measure-based, 15.6s)

- SE CPU: 17,453 ms | FE CPU: 62.8% / 37.2% split
- Multiple SE scans across many value combinations
- Rows scanned: 1,318,524 in main scan; 16,488,828 in SAMEPERIODLASTYEAR FE step

### Large table server timings (C0298-6 — VC, 62s total)

- SE CPU: 1,953 ms (0.7%) | FE CPU: 67,914 ms (99.3%)
- Almost all time in formula engine due to densification
- Rows in SE scan: 1,318,524

## Key Code Examples

### Measure-based YoY%

```dax
YOY % =
VAR CY = [# Customers]
VAR PY = CALCULATE([# Customers], SAMEPERIODLASTYEAR('Date'[Date]))
VAR Result = DIVIDE(CY - PY, PY)
RETURN Result
```

### VC-based YoY% (uses PREVIOUS)

```dax
YOY % =
VAR CY = [# Customers]
VAR PY = PREVIOUS([# Customers], COLUMNS)
VAR Result = DIVIDE(CY - PY, PY)
RETURN Result
```

## Screenshots

Charts and server timing screenshots saved to: `[[Attachments/Visual-Calculations-Performance/C0298-1.png]]`

## Extracted Notes

Links to notes derived from this source:

- [[Source-Analyzing-Visual-Calculations-Performance]] — this source note
- [[previous-next-period]] — extended — added PREVIOUS(COLUMNS) for VC-based YoY% and server timing context
- [[VC-vs-Measure-Performance-Decision]] — `pattern` — decision framework for when to use VCs vs measures
- [[VC-Densification-Performance-Overhead]] — `atomic` — densification cost explanation and numbers
- [[PREVIOUS-YoY-VC-Pattern]] — `snippet` — ready-to-use PREVIOUS-based YoY% visual calculation
- [[SUMMARIZECOLUMNS-Blank-Elimination-VC-Densification]] — `pattern` — blank elimination and densification interaction
- [[VC-vs-Measure-Benchmark-Snippet]] — `snippet` — benchmark numbers from Contoso 23M-row model

## Metadata

| Field | Value |
|-------|-------|
| Source file | Analyzing the performance impact of visual calculations.md |
| Archived at | pending |
| Ingestion date | 2026-08-08 |
| Attachments | 5 PNGs (server timing charts × 5, stored in Attachments/Visual-Calculations-Performance/) |
| Word count | ~1,200 |
| SQLBI+ resources | Whitepaper + video course (gated — captured metadata only) |
