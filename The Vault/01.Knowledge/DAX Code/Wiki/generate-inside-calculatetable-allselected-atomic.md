---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: atomic
tags: [dax, atomic, generate, calculatetable, allselected, filter-context, table]
---

# GENERATE Inside CALCULATETABLE with ALLSELECTED

`GENERATE` computes its second table expression in the *current row context* of the first table — but "current" is whatever filter context surrounds the whole expression. Wrapping `GENERATE` in `CALCULATETABLE(... ALLSELECTED())` decouples the inner ranking from the outer (matrix/per-cell) filter context.

## Definition

When you want to rank items within a slicer's selected range — independent of the report's per-row or per-cell filter context — use this triple composition:

```dax
VAR ResultTable =
    CALCULATETABLE (
        GENERATE (
            PeriodTable,                          -- e.g. SUMMARIZE(Sales, 'Date'[Year])
            TOPN ( N, VALUES ( Entity[Key] ), [Measure] )
        ),
        ALLSELECTED ()
    )
```

`ALLSELECTED` removes the row/column filters from the visual while preserving the user's slicer and report-level filter selections. The inner `GENERATE` then evaluates its `TOPN` in that slicer-only context.

## Key Points

- **`GENERATE` does not change filter context by itself.** It iterates over rows in `table1` and for each row evaluates `table2` *in the row context that `table1` brought*. The outer (query/measure/cell) filter context still flows in.
- **`CALCULATETABLE` is the only way to reset filter context inside a table expression.** The table-form of `CALCULATE` accepts the same modifiers (`ALL`, `ALLSELECTED`, `REMOVEFILTERS`, `KEEPFILTERS`, etc.).
- **`ALLSELECTED` keeps user selection, drops visual context.** Slicers, report-level filters, drillthrough filters, URL filters — all preserved. Row labels, column labels, matrix cell coordinates — all dropped.
- **The pattern applies any time you compute a "global" ranking inside a measure.** Top N per category, top N per year, RANKX over the user's selection — all benefit from this wrapping.
- **Often needed twice in one measure.** Once for the period dimension (`SUMMARIZE`), once for the `GENERATE+TOPN` step — each can leak filter context independently.

## Examples

### Top-N-per-year, slicer-aware

```dax
YearsAndTop10 =
CALCULATETABLE (
    GENERATE (
        SUMMARIZE ( Sales, 'Date'[Year] ),
        TOPN ( 10, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )
    ),
    ALLSELECTED ()
)
```

Inside a matrix with `[Brand]` on rows, this still computes "top 10 products per year, considering only the user's year-range slicer selection" — not "top 10 products in this brand × this cell × this year".

### Without the wrapping (broken)

```dax
-- ❌ WRONG
YearsAndTop10 =
GENERATE (
    SUMMARIZE ( Sales, 'Date'[Year] ),         -- sees only the matrix's year filter
    TOPN ( 10, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )   -- ranks within that cell
)
```

Result: every product appears exactly once in the (year, product) table for the current cell, and downstream `GROUPBY`/`FILTER` produce a list containing all products — measure returns 1 everywhere.

### With ALL instead of ALLSELECTED (different intent)

```dax
YearsAndTop10 =
CALCULATETABLE (
    GENERATE ( ... ),
    ALL ( 'Date' )                             -- ignores slicer entirely
)
```

Use this when the business question is "globally across all years, regardless of user selection". `ALLSELECTED` vs `ALL` is the central slicer-aware-vs-fully-global distinction — see [[REMOVEFILTERS-vs-ALLSELECTED-for-Per-Level-Rules]] for a deeper comparison.

## Why It Matters

Without this technique, table-manipulating measures silently produce per-cell results. The matrix looks plausible but the numbers are wrong. The classic symptom: a "Top 10" measure that returns 1 in every cell.

## Related

- [[generate]] — GENERATE function semantics
- [[topn]] — TOPN function and idioms
- [[allselected]] — function reference
- [[calculatetable]] — CALCULATETABLE filter-context reset
- [[REMOVEFILTERS-vs-ALLSELECTED-for-Per-Level-Rules]] — choosing between the two
- [[topn-filter-context-leak-matrix-gotcha]] — the gotcha this prevents
- [[evergreen-top-n-products-pattern]] — pattern that uses this composition
- [[Author-Marco-Russo-Alberto-Ferrari]] — originators of the technique