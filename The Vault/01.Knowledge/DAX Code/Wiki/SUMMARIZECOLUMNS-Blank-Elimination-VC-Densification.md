---
created: 2026-08-08
updated: 2026-08-08
source: "Analyzing the performance impact of visual calculations"
source_url: https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
note_type: pattern
tags: [visual-calculations, summarizecolumns, blank, dax, performance, densification]
---

# SUMMARIZECOLUMNS Blank Elimination + VC Densification Interaction

`SUMMARIZECOLUMNS` and visual calculations have opposing strategies for handling BLANK cells: SUMMARIZECOLUMNS eliminates blank rows (optimisation), while VC densification recreates them (requirement). This interaction is the root cause of VC performance degradation on large virtual tables.

<!-- one-line description: SUMMARIZECOLUMNS skips rows where all measures are BLANK; VC densification must recreate those rows so PREVIOUS/NEXT can navigate the full cross-product -->

## The Conflict

### SUMMARIZECOLUMNS blank elimination

```dax
-- SUMMARIZECOLUMNS does NOT return rows where all measures are BLANK
EVALUATE
SUMMARIZECOLUMNS(
    'Brand'[Brand],
    'Date'[Year],
    "Sales", [Sales Amount]
)
-- Result: 100 rows if 10 of 110 brand×year combinations are blank
```

This is an optimisation — the engine avoids materialising rows with no useful data.

### Visual calculation densification

Visual calculations (e.g., PREVIOUS) need to navigate the full matrix structure — every combination of rows and columns — regardless of whether the base measures are blank. When a YoY% is computed in a cell where the base measure was blank, the VC needs that row to know there was a previous period to compare against.

```dax
-- This VC expression needs the full cross-product
VAR CY = [Sales Amount]           -- BLANK for some cells
VAR PY = PREVIOUS([Sales Amount], COLUMNS)
RETURN DIVIDE(CY - PY, PY)         -- Can return -10% even when CY is BLANK
```

The densification step rebuilds the eliminated rows so that `PREVIOUS` can find a valid previous column.

## Practical Example

Matrix: 11 brands × 10 years = 110 maximum cells

**Without VC:** SUMMARIZECOLUMNS returns ~100 rows (10 blank combinations eliminated)

**With VC:** Densification rebuilds all 110 rows — including the 10 blanks — so PREVIOUS can navigate across all columns

## Performance Impact

The more blank combinations there are (sparse data), the more rows densification must recreate, and the slower the VC becomes relative to the measure-based equivalent.

| Scenario | Blank density | Densified rows | VC vs Measure |
|---|---|---|---|
| Dense data (few blanks) | Low | Close to SUMMARIZECOLUMNS output | Comparable |
| Sparse data (many blanks) | High | Many more than SUMMARIZECOLUMNS output | VC significantly slower |

## Why Densification Cannot Be Skipped

Skipping densification would break VCs that produce non-blank results in cells where base measures are blank — for example:

- A YoY% that shows `-100%` for a new product (no prior year) instead of blank
- A Running Total that starts from a non-zero initial value
- Any VC that computes a derived metric that is meaningful even when the base measure is blank

Densification is required to guarantee that the full visual structure exists in the virtual table.

## Related

- [[VC-Densification-Performance-Overhead]] — densification as the primary VC performance overhead
- [[VC-vs-Measure-Performance-Decision]] — when to prefer VCs despite densification cost
- [[PREVIOUS-YoY-VC-Pattern]] — pattern that must use densification
- [[Source-Analyzing-Visual-Calculations-Performance]] — source article
