---
created: 2026-08-08
updated: 2026-08-08
source: "Analyzing the performance impact of visual calculations"
source_url: https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
note_type: pattern
tags: [visual-calculations, performance, dax, measure, decision]
---

# Measure vs Visual Calc Performance Decision Pattern

Use this decision framework to choose between a model measure and a visual calculation for a given report, based on the expected size of the virtual table.

<!-- one-line description: decision tree — choose visual calculation for small virtual tables (≤10K rows), choose model measure for large tables (>10K rows) -->

## Decision Tree

```
Is the virtual table small?
│
├── YES (< ~10,000 rows) — use VISUAL CALCULATION
│   └── Precomputed values already in memory; PREVIOUS/NEXT run in FE on virtual table
│   └── No repeated SE queries per cell
│   └── Example: ~110 cells (11 brands × 10 years)
│
└── NO (> ~10,000 rows) — use MODEL MEASURE
    └── SUMMARIZECOLUMNS blank elimination + collapsed-row optimisation keeps measure fast
    └── Repeated SE queries per cell are cheaper than densification + FE materialisation
    └── Example: 1,686,390 cells (67 stores × 2,517 products × 10 years)
```

## Why the Cutoff Is ~10K Rows

| Table size | VC densification cost | Measure repeated-SE cost | Winner |
|---|---|---|---|
| ~100 rows | Negligible | High (many SE queries) | VC |
| ~1,000 rows | Low | High | VC |
| ~10,000 rows | Moderate | High | VC (marginal) |
| ~100,000 rows | High | Moderate | Measure |
| ~1,000,000+ rows | Very high | Moderate | Measure |

The exact cutoff depends on your model, hardware, and DAX complexity. Test both approaches when the virtual table is in the 5,000–20,000 row range.

## Estimating Virtual Table Size

```
Virtual table rows = (distinct ROWS-axis values) × (distinct COLUMNS-axis values)
```

Measure expansion state: collapsed rows are **not** computed in measure-based reports. In VC reports, all rows are materialized at the leaf level regardless of expansion.

## Decision Factors Beyond Size

| Factor | Favours VC | Favours Measure |
|---|---|---|
| **Non-additive measures** (DISTINCTCOUNT, DISTINCTCOUNTNOBLANK) | ✅ VC | |
| **Additive measures** (SUM, AVERAGE) | | ✅ Measure |
| **Many columns on COLUMNS axis** | | ✅ Measure |
| **Deep drillthrough (many expanded levels)** | | ✅ Measure |
| **Simple prior/next cell reference** | ✅ VC | |
| **Time intelligence with SAMEPERIODLASTYEAR** | | ✅ Measure (for small tables, VC with PREVIOUS is simpler) |
| **DAX requiring cross-join of ROWS × COLUMNS** | ✅ VC | |
| **Compressed/sparse data (many blanks)** | | ✅ Measure |

## The Bottom Line (SQLBI)

> "Do not assume visual calculations are always faster than measure-based reports, as they compute values only once. With small virtual tables, visual calculations are great. As soon as the virtual table grows, performance can be at serious risk."
> — Marco Russo & Alberto Ferrari, SQLBI

## Related

- [[VC-Densification-Performance-Overhead]] — detailed mechanism behind the performance difference
- [[PREVIOUS-YoY-VC-Pattern]] — VC pattern for the small-table case
- [[SUMMARIZECOLUMNS-Blank-Elimination-VC-Densification]] — why the two approaches handle blanks differently
- [[Source-Analyzing-Visual-Calculations-Performance]] — source article
- [[VC-vs-Measure-Benchmark-Snippet]] — specific benchmark numbers from the Contoso model
