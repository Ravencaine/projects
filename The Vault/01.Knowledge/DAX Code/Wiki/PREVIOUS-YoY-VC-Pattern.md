---
created: 2026-08-08
updated: 2026-08-08
source: "Analyzing the performance impact of visual calculations"
source_url: https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
note_type: snippet
tags: [visual-calculations, yoy, previous, dax, pattern]
---

# PREVIOUS-based YoY% Visual Calculation Pattern

Ready-to-use visual calculation for Year-over-Year percentage change using `PREVIOUS()` on the COLUMNS axis. Use when the matrix has years on columns and you want a YoY% column calculated in the visual layer rather than as a model measure.

<!-- one-line description: YoY% calculation using PREVIOUS() on COLUMNS in a visual calculation — avoids SAMEPERIODLASTYEAR and multiple SE queries -->

## Code

```dax
YOY % =
VAR CY = [# Customers]
VAR PY = PREVIOUS([# Customers], COLUMNS)
VAR Result = DIVIDE(CY - PY, PY)
RETURN Result
```

## When to Use

- **Small virtual tables** (≤ few thousand rows) — PREVIOUS reads from the precomputed virtual table, avoiding repeated storage engine queries for each cell
- **Multi-column comparisons** where the prior period is on a sibling column (e.g., same row, previous column)
- **DISTINCTCOUNT or non-additive measures:** PREVIOUS circumvents the need for SAMEPERIODLASTYEAR which forces a new SE query per cell
- **Visual has years on COLUMNS axis:** PREVIOUS(COLUMNS) navigates to the previous column within the same row

## Performance Impact

| Measure | VC with PREVIOUS | Measure with SAMEPERIODLASTYEAR |
|---|---|---|
| DISTINCTCOUNT (11 brands × 10 years) | 6s | 13s |
| Sales Amount (large table) | 62s | 15.6s |

The pattern is faster than the measure-based equivalent only when the virtual table is small. With large matrices (>10K rows), the densification overhead outweighs the benefit.

## Variations

### PREVIOUS with ROWS axis

```dax
-- When prior period is in a previous row (e.g., cumulative total)
VAR Current = [Sales Amount]
VAR PriorRow = PREVIOUS([Sales Amount], ROWS)
RETURN DIVIDE(Current - PriorRow, PriorRow)
```

### PREVIOUS with explicit Steps

```dax
-- Skip one period (e.g., YoY from 2 years ago)
VAR CY = [Sales Amount]
VAR PY = PREVIOUS([Sales Amount], COLUMNS, 2)
RETURN DIVIDE(CY - PY, PY)
```

### Guard against first column (no previous)

```dax
VAR CY = [Sales Amount]
VAR PY = PREVIOUS([Sales Amount], COLUMNS)
RETURN
    IF(
        ISBLANK(PY),
        BLANK(),
        DIVIDE(CY - PY, PY)
    )
```

## Related

- [[previous-next-period]] — PREVIOUS() function reference
- [[VC-vs-Measure-Performance-Decision]] — when to use this vs the measure-based equivalent
- [[VC-Densification-Performance-Overhead]] — why it can be slower with large virtual tables
- [[SUMMARIZECOLUMNS-Blank-Elimination-VC-Densification]] — blank elimination interaction with VC densification
- [[Source-Analyzing-Visual-Calculations-Performance]] — source article with full benchmark numbers
