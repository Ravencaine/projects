---
created: 2026-07-26
updated: 2026-08-09
source: dax.pdf
note_type: function
tags: [dax, function, table, generate, crossjoin, topn, allselected]
---

# GENERATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table with the Cartesian product between each row in table1 and the table

## Syntax

```dax
GENERATE(<table1>, <table2>)
```

## Remarks

If the evaluation of table2 for the current row in table1 returns an empty table, then the result table will not contain the current row from table1. This is different than GENERATEALL() where the current row from table1 will be included in the results and columns corresponding to table2 will have null values for that row. All column names from table1 and table2 must be different or an error is returned.

## Generative semantics (the "for each row, compute" pattern)

`GENERATE` is best understood as a **per-row computation**: for each row in `table1`, evaluate `table2` in that row's filter context, and append the result to the output. The result is a `table1 × table2(row)` crossjoin.

This makes `GENERATE` the standard composition for "for each X, find the top/bottom N by some metric":

```dax
GENERATE (
    SUMMARIZE ( Sales, 'Date'[Year] ),
    TOPN ( 10, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )
)
```

→ returns one row per (Year, ProductKey) where ProductKey is in the top 10 of that year.

## Slicer-aware variant: wrap in CALCULATETABLE + ALLSELECTED

When the inner `table2` should see the *slicer's* filter context rather than the report's per-cell context, wrap `GENERATE` in `CALCULATETABLE(... ALLSELECTED())`:

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

Without this wrapping, `TOPN` ranks within the matrix cell's deeply-filtered context (per-row), and the result is a per-cell top-N that doesn't compose into a meaningful "evergreen" list downstream. See [[generate-inside-calculatetable-allselected-atomic]] for the full rationale.

## Related

- [[topn]] — pairs with GENERATE for top-N-per-group
- [[generateall]] — keeps `table1` rows even when `table2` is empty
- [[allselected]] — required for slicer-aware GENERATE inside a measure
- [[evergreen-top-n-products-pattern]] — pattern using GENERATE + TOPN + GROUPBY + coverage filter
- [[generate-inside-calculatetable-allselected-atomic]] — atomic on the slicer-aware composition
- [[Source-Find-Top-10-Products-Every-Year-DAX]] — source for the slicer-aware variant
