---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: workflow
tags: [dax, calculation-groups, slicer, filter, measure, workflow]
---

# Slicer Filter Measure Implementation Workflow

**Type:** Workflow · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

Implement a slicer that filters a report by a measure threshold (e.g., "show only products with sales > 100k"). Uses a local function + calculation group + calculation items.

## Step 1 — Create the local filter function

In Tabular Editor (external) or the model, create this calculated table/measure with the local function:

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

> Note: This requires Tabular Editor or the newer built-in calculation group editor in Power BI. Use Tabular Editor for full control.

## Step 2 — Create the calculation group

Create a new calculation group in your model (e.g., `Filter Product Sales`).

## Step 3 — Add calculation items

Create one calculation item per threshold:

```dax
-- Item 1
Products selling more than 100USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 100)

-- Item 2
Products selling more than 1,000USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 1000)

-- Item 3
Products selling more than 10,000USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 10000)

-- Item 4
Products selling more than 100,000USD =
    Local.FilterProductsBasedOnMeasure(SELECTEDMEASURE(), [Sales Amount], 100000)
```

## Step 4 — Add to report

1. The calculation group appears as a slicer in the Fields pane
2. Add it to the report canvas as a slicer visual
3. Users select a threshold from the calculation group slicer
4. The report updates to show only products meeting the threshold

## Key requirements

- **Tabular Editor** (or built-in calculation group editor) to create the function and calculation group
- The measure in the report must be the same measure referenced in `filterMeasure`
- See [[selectedmeasure-local-function-parameter]] for why `SELECTEDMEASURE()` is used

## Related

- [[filterproductsbasedonmeasure-local-function]] — the function itself
- [[measure-cannot-be-filtered-granularity-required]] — why this approach is needed
- [[flexible-slicer-with-granularity-workflow]] — two-slicer version with dynamic granularity
