---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: atomic
tags: [dax, selectedmeasure, calculation-groups, local-function, atomic]
---

# SELECTEDMEASURE Local Function Parameter Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

`SELECTEDMEASURE()` returns the DAX expression of the measure currently being evaluated. It is used as a parameter inside calculation item functions to make the function work with any measure selected in the report, without hardcoding the measure name.

## What it returns

`SELECTEDMEASURE()` returns the currently evaluated measure's expression as an expression object — not the measure's name, not its result value, but the expression itself.

## Why it matters in this pattern

```dax
Local.FilterProductsBasedOnMeasure = (
    resultExpression : EXPR,
    filterMeasure: MEASUREREF,
    filterLimit: SCALAR
) =>
    CALCULATE(
        resultExpression,
        KEEPFILTERS(
            FILTER(Product, filterMeasure > filterLimit)
        )
    )
```

Inside the local function:
- `resultExpression` = the caller's expression (typically `SELECTEDMEASURE()`)
- `filterMeasure` = passed as `MEASUREREF` from the calculation item
- `filterLimit` = the numeric threshold

The calculation item calls:
```dax
Products selling more than 100USD =
Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 100)
```

`SELECTEDMEASURE()` passes whatever measure the user has on the canvas into the function — the same calculation item works for Sales, Quantity, Profit, or any other measure.

## Related

- [[filterproductsbasedonmeasure-local-function]] — full function implementation
- [[filtertablebasedonmeasure-granularity-switch]] — extended version with SWITCH
