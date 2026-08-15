---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: pattern
tags: [dax, calculation-groups, switch, selectedvalue, filter, granularity, dynamic, pattern]
---

# FilterTableBasedOnMeasure Granularity SWITCH Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

Extended version of `FilterProductsBasedOnMeasure` that accepts the **granularity as a parameter** via a disconnected table selection. Users pick the filter entity (Product, Customer, Store) from a second slicer, and the function dynamically routes the `FILTER` call to the correct table via `SWITCH`.

## Disconnected granularity table

```dax
TableToFilter =
    SELECTCOLUMNS(
       {"Product", "Customer", "Store"},
       "Table to filter", [Value]
    )
```

This calculated table populates a second slicer — users select which entity to filter by.

## Dynamic function

```dax
Local.FilterTableBasedOnMeasure = (
    resultExpression : EXPR,
    filterMeasure : MEASUREREF,
    filterLimit : SCALAR
)=>
    VAR TableToFilter = SELECTEDVALUE(TableToFilter[Table to filter])
    VAR Result =
        SWITCH(
            TableToFilter,
            "Product",
                CALCULATE(
                    resultExpression,
                    FILTER(Product, filterMeasure > filterLimit)
                ),
            "Customer",
                CALCULATE(
                    resultExpression,
                    FILTER(Customer, filterMeasure > filterLimit)
                ),
            "Store",
                CALCULATE(
                    resultExpression,
                    FILTER(Store, filterMeasure > filterLimit)
                )
        )
    RETURN
        Result
```

## How it works

1. `SELECTEDVALUE(TableToFilter[Table to filter])` — reads user's granularity selection from slicer
2. `SWITCH(TableToFilter, "Product", ..., "Customer", ..., "Store", ...)` — routes to the correct branch
3. Each branch uses `FILTER` on the selected table, evaluating `filterMeasure` per row

## Two-slicer UI

| Slicer 1 | Slicer 2 |
|----------|----------|
| Amount threshold (calculation group): 100 / 1,000 / 10,000 / 100,000 / 1,000,000 | Entity to filter: Product / Customer / Store |

## Related

- [[filterproductsbasedonmeasure-local-function]] — fixed-granularity version
- [[slicer-filter-measure-implementation-workflow]] — basic implementation
- [[flexible-slicer-with-granularity-workflow]] — full two-slicer setup workflow
