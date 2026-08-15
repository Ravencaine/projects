---
created: 2026-08-08
updated: 2026-08-08
source: ABC Analysis in Power BI The Chart That Shows Your 8020 Instantly
note_type: atomic
tags: [power-bi, visual-calculations, collapse, sum]
---

# Visual Calculations: COLLAPSESUM / COLLAPSE ALL

`COLLAPSESUM` is a visual calculation function that computes an aggregation (sum by default) collapsing the current visual context — similar to `CALCULATE(..., REMOVEFILTERS())` but scoped to the visual axis.

## Definition

```
COLLAPSESUM( <expression> )
COLLAPSESUM( <expression>, ALL )
```

- **`COLLAPSESUM(expr)`:** collapses the current row context (like the current item on the X-axis) and sums `expr` over the full visual axis
- **`COLLAPSESUM(expr, ALL)`:** additionally removes all external filters — gives grand total across the entire dataset

## Use Case

Calculate each item's percentage of the grand total without writing a model-level measure:

```
% of Total =
  COLLAPSESUM( SUM(Sales[SalesAmount]) )
  / COLLAPSESUM( SUM(Sales[SalesAmount]), ALL )
```

- Numerator: sum of sales for the current item (collapsed row context)
- Denominator: grand total across all items (collapsed + all filters removed)

## Key Properties

- Works **without hard-coding the axis field:** uses `ROWS` implicitly
- Swap the visual's breakdown dimension and the formula still works
- Does not require a model-level measure — lives entirely in the visual

## Related

- [[ABC-Classification-Chart-Visual-Calculations]] — % of total used in the ABC chart
- [[Visual-Calculations-RUNNINGSUM-ORDER-BY]] — RUNNINGSUM often pairs with COLLAPSESUM
