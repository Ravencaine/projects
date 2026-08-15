---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: gotcha
tags: [dax, filter-context, keepfilters, top-n, sqlbi]
---

# TopN ProductKey Override Gotcha

When using a top-N-by-period result table as a filter in `CALCULATE`, the table's column filter **replaces** the outer filter context — it does not intersect with it. Without `KEEPFILTERS`, the inner filter silently wins, producing incorrect counts or sums.

## Expected Behaviour

When a user slices the matrix by `Product[Brand]` or `Product[ProductName]`, the measure should respect those filters and show the count/sum only for products matching both the outer selection and the evergreen top-N condition.

## Actual Behaviour

Without `KEEPFILTERS`, the `BestProds` table's `Product[ProductKey]` filter **overwrites** any outer filter on the same column. A matrix row for "Product X" returns blank if "Product X" is not in `BestProds` — even if "Product X" would have qualified as a top-N product in the current filter context.

Additionally, if the user places `Product[ProductKey]` directly on a visual axis, the `BestProds` filter replaces the visual's own filter, making every row return the same number (usually 1 or 0).

## Why It Happens

`CALCULATE`'s filter arguments replace filters by default. The `BestProds` table contains `Product[ProductKey]` as a result of `GROUPBY`. Applying it as a direct filter:

```dax
CALCULATE( COUNTROWS('Product'), BestProds )
```

...removes the outer `Product[ProductKey]` filter (from the matrix row or visual axis) and replaces it with `BestProds`'s product keys.

## How to Handle It

Wrap the table filter in `KEEPFILTERS`:

```dax
CALCULATE( COUNTROWS('Product'), KEEPFILTERS(BestProds) )
```

`KEEPFILTERS` changes the behaviour from **replace** to **intersect:** the outer filter and the inner `BestProds` filter are combined. A row only appears if it is in both the matrix context *and* the evergreen top-N set.

## General Rule

When the table used as a `CALCULATE` filter argument contains columns that also appear in the outer filter context (either from visuals, slicers, or row/column axes), always wrap it in `KEEPFILTERS` unless you explicitly want the replacement behaviour.

## Related Gotchas

- [[filter-functions-allexcept-keepfilters]] — broader treatment of KEEPFILTERS vs direct filters in CALCULATE
- [[auto-exist-and-all-gotchas]] — related context-collision issues with SUMMARIZE
- [[Evergreen-Top-N-Products]] — the pattern this gotcha applies to
- [[Source-SQLBI-Top-10-Every-Year]] — primary source from SQLBI
