---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: workflow
tags: [dax, calculation-groups, slicer, granularity, switch, disconnected-table, workflow]
---

# Flexible Slicer With Granularity Workflow

**Type:** Workflow · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

Build a two-slicer report where users control both the **measure threshold** (via calculation group) and the **filter granularity** (via disconnected table). Allows filtering products, customers, or stores by any measure's value.

## Step 1 — Create the granularity table

Create a disconnected calculated table:

```dax
TableToFilter =
    SELECTCOLUMNS(
       {"Product", "Customer", "Store"},
       "Table to filter", [Value]
    )
```

Add `TableToFilter[Table to filter]` as a slicer on the report canvas.

## Step 2 — Create the dynamic filter function

In Tabular Editor, create:

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
                CALCULATE(resultExpression,
                    FILTER(Product, filterMeasure > filterLimit)),
            "Customer",
                CALCULATE(resultExpression,
                    FILTER(Customer, filterMeasure > filterLimit)),
            "Store",
                CALCULATE(resultExpression,
                    FILTER(Store, filterMeasure > filterLimit))
        )
    RETURN Result
```

## Step 3 — Create the calculation group

Create a calculation group (e.g., `Filter Sales Amount`).

## Step 4 — Add calculation items

```dax
Sales amount more than 100USD =
    Local.FilterTableBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 100)

Sales amount more than 1,000USD =
    Local.FilterTableBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 1000)

Sales amount more than 10,000USD =
    Local.FilterTableBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 10000)

Sales amount more than 100,000USD =
    Local.FilterTableBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 100000)
```

## Step 5 — Report layout

| Visual | Purpose |
|--------|---------|
| Calculation group slicer | Choose amount threshold |
| TableToFilter slicer | Choose entity to filter (Product/Customer/Store) |
| Matrix/Table | Shows filtered results |

## Result

Users can ask: "Show me **stores** with **sales > 100,000**" or "Show me **customers** with **profit > 10,000**" — same two slicers, flexible granularity.

## Related

- [[filtertablebasedonmeasure-granularity-switch]] — the function itself
- [[slicer-filter-measure-implementation-workflow]] — basic single-granularity version
- [[selectedmeasure-local-function-parameter]] — why SELECTEDMEASURE works for any measure
