---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: pattern
tags: [dax, calculation-groups, keeplfilters, filter, product, pattern]
---

# FilterProductsBasedOnMeasure Local Function Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

Encapsulate the "filter rows by measure value" logic in a reusable local function. Uses `KEEPFILTERS` + `FILTER` inside `CALCULATE` to apply a threshold filter to a specified table. Called from calculation items with `SELECTEDMEASURE()` as the result expression.

## Function signature

```dax
Local.FilterProductsBasedOnMeasure =
(
    resultExpression : EXPR,
    filterMeasure: MEASUREREF,
    filterLimit: SCALAR
)=>
    CALCULATE(
        resultExpression,
        KEEPFILTERS(
            FILTER(Product, filterMeasure > filterLimit)
        )
    )
```

## Parameters

| Parameter | Type | Purpose |
|-----------|------|---------|
| `resultExpression` | EXPR | The measure expression to evaluate (pass `SELECTEDMEASURE()`) |
| `filterMeasure` | MEASUREREF | The measure to use as the filter (e.g., `[Sales Amount]`) |
| `filterLimit` | SCALAR | The threshold value (e.g., 100, 1000, 10000) |

## How it works

1. `FILTER(Product, filterMeasure > filterLimit)` — evaluates `filterMeasure` at each Product row and keeps only those exceeding `filterLimit`
2. `KEEPFILTERS()` — preserves existing visual filters instead of overwriting them
3. `CALCULATE(..., KEEPFILTERS(...))` — evaluates `resultExpression` under the filtered context

## Calculation items using this function

```dax
-- In Filter Product Sales calculation group
Products selling more than 100USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 100)

Products selling more than 1,000USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 1000)

Products selling more than 10,000USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 10000)
```

## Granularity note

The table being filtered (`Product`) is hardcoded inside the function. For dynamic granularity, see [[filtertablebasedonmeasure-granularity-switch]].

## Related

- [[selectedmeasure-local-function-parameter]] — how SELECTEDMEASURE is used as parameter
- [[slicer-filter-measure-implementation-workflow]] — step-by-step implementation
- [[filtertablebasedonmeasure-granularity-switch]] — dynamic granularity version
