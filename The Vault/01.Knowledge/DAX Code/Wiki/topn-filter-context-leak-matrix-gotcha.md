---
created: 2026-08-09
updated: 2026-08-09
source: "Find the products in the top 10 every year with DAX.md"
note_type: gotcha
tags: [dax, gotcha, topn, calculate, filter-context, allselected, keepfilters, matrix]
---

# TOPN/CALCULATE Filter-Context Leak in Matrices

A `TOPN`-based measure that runs in a matrix returns 1 for every row instead of filtering to the top N — because the top-N computation happens in the deeply-filtered per-row context, not in the slicer/user context.

## Expected Behaviour

You write a measure that should return 1 only for the top 10 products in the current context. You expect the matrix to show 1 next to each top-10 product and BLANK for the rest.

```dax
Num Best Prods =
VAR NumOfTop = 10
VAR Years =
    SUMMARIZE ( Sales, 'Date'[Year] )   -- ❌ not ALLSELECTED
VAR YearsAndTop10 =
    GENERATE (
        Years,
        TOPN ( NumOfTop, VALUES ( 'Product'[ProductKey] ), [Sales Amount] )
    )
VAR BestProds =
    -- ... group + filter ...
VAR Result =
    CALCULATE ( COUNTROWS ( 'Product' ), BestProds )   -- ❌ no KEEPFILTERS
RETURN
    Result
```

## Actual Behaviour

The measure returns **1 for every product in the matrix**, not just the top ones.

## Why It Happens

Two independent filter-context leaks, both invisible in the DAX Studio query editor:

1. **`Years` only sees the currently-filtered years.** When the matrix has `Brand` on rows and the user has filtered to year 2020, `SUMMARIZE (Sales, 'Date'[Year])` returns just `{2020}` — not the slicer's selected range. `TOPN` then ranks within that single year. The subsequent `GROUPBY` and `FILTER` produce a list that always contains *every* product (each appears once → count ≥ 1 ≥ minYears).
2. **`TOPN` evaluates `[Sales Amount]` in the current filter context.** Inside a matrix cell, that context is per-cell — so `TOPN` returns "the top 10 products for *this specific cell*", which is at most 1 product, sometimes 0. When `CALCULATE(COUNTROWS('Product'), BestProds)` runs in this context, the per-cell `BestProds` list is essentially empty or a single product, and the result is always 1 (or 0).
3. **`CALCULATE(<expr>, T)` replaces filters on columns in `T`.** Even if the product list is correct, applying it via `CALCULATE` *overwrites* the matrix's row-level filter on any column that overlaps with the table — for example, `Product[ProductKey]` if the matrix uses it. Result: the matrix's row label no longer drives the count; the measure's `BestProds` does.

## How to Handle It

**Two complementary fixes:**

### Fix 1 — decouple the top-N logic from outer filter context

Wrap every `VAR` that produces the period or top-N table in `CALCULATETABLE(... ALLSELECTED())`:

```dax
VAR Years =
    CALCULATETABLE (
        SUMMARIZE ( Sales, 'Date'[Year] ),
        ALLSELECTED ()          -- see the slicer's year range, not the matrix cell's
    )
VAR YearsAndTop10 =
    CALCULATETABLE (
        GENERATE (
            Years,
            TOPN (
                NumOfTop,
                VALUES ( 'Product'[ProductKey] ),
                [Sales Amount]
            )
        ),
        ALLSELECTED ()          -- [Sales Amount] evaluates in slicer context
    )
```

`ALLSELECTED` removes the matrix-row filters but preserves whatever the user explicitly selected (slicers, report filters). The top-N list is now computed *once per slicer selection*, not per matrix cell.

### Fix 2 — intersect instead of replace when applying the product list

Wrap the `BestProds` filter in `KEEPFILTERS`:

```dax
VAR Result =
    CALCULATE (
        COUNTROWS ( 'Product' ),
        KEEPFILTERS ( BestProds )   -- AND, don't replace
    )
```

This way, if the matrix uses `Product[ProductKey]` as a row label, the per-row filter ANDs with the product list rather than replacing it. The measure now correctly counts whether the current row's product is in the evergreen list.

## Diagnostic Checklist

When a `TOPN`-based measure returns 1 everywhere in a matrix:

- [ ] Is every `VAR` producing a period or ranking table wrapped in `CALCULATETABLE(... ALLSELECTED())`?
- [ ] Is the final `CALCULATE(<expr>, T)` using `KEEPFILTERS(T)`?
- [ ] Does the test in DAX Studio (no matrix context) return the expected product list?
- [ ] Does the same `VAR` chain produce different results when run inside the matrix vs. outside? (If yes — filter context leak.)

## Related Gotchas

- [[calculate-nested-keephilters-gotcha]] — nested CALCULATE rules; KEEPFILTERS behaviour at depth
- [[keepfilters]] — intersect-vs-replace semantics
- [[auto-exist-and-all-gotchas]] — auto-exist collapsing in SUMMARIZE
- [[dax-allselected-cardinality-trap]] — ALLSELECTED can inflate result cardinality unexpectedly
- [[avoid-using-filter-as-filter-argument]] — when FILTER vs direct filter inside CALCULATE

## Related

- [[evergreen-top-n-products-pattern]] — pattern that exhibits this gotcha
- [[query-measure-function-workflow]] — stage 2 ("move to measure") catches this
- [[Author-Marco-Russo-Alberto-Ferrari]] — originators of the diagnostic