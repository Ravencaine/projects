---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/advanced-conditional-formatting-in-excel-using-formulas"
published: 2026-04-28
note_type: source
tags: [excel, conditional-formatting, formulas, automation, formatting, data-validation]
---

# Advanced Conditional Formatting in Excel Using Formulas — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2026-04-28. Author: Mynda Treacy — already in vault (5th source).

## Summary

7 formula-based conditional formatting techniques: format rows based on one cell, compare two columns, flag missing data, detect keywords, create date alerts, find duplicates, and build filter-aware banding. Plus rule priority management.

## The 7 Techniques

| # | Technique | Formula |
|----|-----------|---------|
| 1 | Format entire rows from one cell | `=$H2="Cancelled"` |
| 2 | Compare two columns | `=$H5>$G5` |
| 3 | Flag missing data | `=SUM(--ISBLANK($C5:$H5))` |
| 4 | Highlight keyword rows | `=SEARCH("urgent",$H5)` |
| 5 | Date-based alerts | `=$G7<=TODAY()` / `=$G7<=TODAY()+7` |
| 6 | Detect duplicates (1 column) | `=COUNTIF($E$5:$E5,$E5)>1` |
| 7 | Detect duplicates (multi-column) | `=COUNTIFS($E$5:$E5,$E5,$G$5:$G5,$G5)>1` |
| — | Filter-aware banding | `=MOD(SUBTOTAL(3,$C$5:$C5),2)` |

## Key Insight

Formula-based conditional formatting is constrained to return a single TRUE/FALSE. Array operations (like double unary `--ISBLANK`) must reduce to one value for the row.

## Key Insights Extracted

- [[Mixed-References-for-Row-Formatting]] — `atomic` — `$H2` (column locked, row relative); CF formula evaluates each row with the same column check
- [[ISBLANK-Double-Unary-for-Row-Validation]] — `atomic` — `=SUM(--ISBLANK($C5:$H5))`; double unary converts TRUE/FALSE array to 1/0; SUM reduces to single value
- [[SEARCH-for-Keyword-Detection-in-CF]] — `atomic` — SEARCH returns number (found) or error (not found); CF treats number=TRUE, error=FALSE; case-insensitive
- [[TODAY-for-Dynamic-Date-Alerts]] — `atomic` — TODAY() recalculates each recalc; overdue vs upcoming alert thresholds; priority: overdue over upcoming
- [[COUNTIF-Expanding-Range-for-Duplicates]] — `atomic` — `$E$5:$E5` (top locked, bottom relative); range expands as CF evaluates downward; first occurrence count=1
- [[COUNTIFS-for-Multi-Column-Duplicates]] — `atomic` — COUNTIFS with two expanding ranges; flags exact duplicates; partial matches get lighter format
- [[MOD-SUBTOTAL-for-Filter-Aware-Banding]] — `atomic` — SUBTOTAL(3,range) counts only visible rows; MOD alternates 0/1; banding respects filters
- [[Rule-Priority-in-CF-Manager]] — `workflow` — strict rules above general rules; use Manage Rules to order; stricter overrides gentler

## Author

- [[Author-Mynda-Treacy]] — extended (5th source)
