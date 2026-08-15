---
created: 2026-07-26
updated: 2026-08-09
source: dax.pdf
note_type: function
tags: [dax, function, table, top-n, ranking, generate, allselected]
---

# TOPN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the top N rows of the specified table.

## Syntax

```dax
TOPN(<N_Value>, <Table>, <OrderBy_Expression>, [<Order>[,<OrderBy_Expression>, [<Order>]]…])
```

## TOPN-per-group idiom (inside GENERATE)

When you want the top N within each group of a second table — e.g., the top 10 products per year — pass `GENERATE(Years, TOPN(N, VALUES(...), [Measure]))`. `GENERATE` evaluates the second table in the row context of the first; `TOPN` then ranks within that context.

```dax
YearsAndTop10 =
GENERATE (
    SUMMARIZE ( Sales, 'Date'[Year] ),
    TOPN ( 10, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )
)
```

Returns a `(Year, ProductKey)` table with ~10 rows per year.

**Slicer-aware ranking:** wrap the whole expression in `CALCULATETABLE(... ALLSELECTED())` so `TOPN` evaluates in the user's slicer context, not the matrix cell's per-row context:

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

Without this, the top-N list is computed per-cell and downstream filters produce a list containing every product — the classic "measure returns 1 everywhere" symptom. See [[topn-filter-context-leak-matrix-gotcha]] for the full diagnostic.

**UDF-callable sort expression:** when `TOPN`'s sort expression is a UDF parameter, wrap with `CALCULATE(sortExpr)` to ensure evaluation regardless of argument form:

```dax
TOPN ( 10, VALUES ( 'Product'[ProductKey] ), CALCULATE ( sortExpr ) )
```

## Related

- [[generate]] — pairs with TOPN for top-N-per-group
- [[allselected]] — decouples the ranking from matrix context
- [[evergreen-top-n-products-pattern]] — pattern that uses GENERATE+TOPN + GROUPBY + coverage filter
- [[dynamic-top-n-ranking-pattern]] — alternative top-N approach using RANKX
- [[top-n-others-union-pattern]] — combine Top N with an "Others" row
- [[topn-filter-context-leak-matrix-gotcha]] — gotcha when TOPN runs inside a matrix
- [[Source-Find-Top-10-Products-Every-Year-DAX]] — source for the per-group idiom
