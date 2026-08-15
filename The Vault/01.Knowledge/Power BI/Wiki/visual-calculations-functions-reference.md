---
created: 2026-08-11
updated: 2026-08-11
source: "ABC-Analysis-HowToPowerBI-Transcript.md"
note_type: reference
tags: [power-bi, visual-calculations, reference]
---

# Visual Calculations Functions — Quick Reference

Key functions used in ABC/Pareto visual calculations patterns.

## Functions

### COLLAPSEDEALL

```dax
COLLAPSEDEALL(<expression>)
```
Returns `expression` evaluated across all rows on the axis (ignores current row context). Used to compute % of total without needing a REMOVEFILTERS measure.

### RUNNINGSUM

```dax
RUNNINGSUM(<expression>)
```
Cumulative sum of `expression` across rows. Must pair with `ORDER BY` to define sort order.

### ORDER BY

```dax
RUNNINGSUM([% of Total])
  ORDER BY [Running Sum] DESC
```
Defines the sort order for RUNNINGSUM and NEXT. Use the same measure used in RUNNINGSUM for correct Pareto ordering.

### NEXT

```dax
NEXT(<expression>)
  ORDER BY <order_expression> DESC
```
Returns the value of `expression` in the next row. Essential for finding the last item in an ABC bucket to place a label.

## Common Mistakes

- Using hardcoded column names (e.g., `Product[ProductKey]`) instead of `ROWS` — breaks flexibility when swapping dimensions
- Using `ORDER BY TotalSales` instead of `ORDER BY [Running Sum]` in RUNNINGSUM — wrong sort order for Pareto
- Deleting a measure that another visual calculation depends on — visual calculations can only reference measures present in the visual

## Related

- [[abc-classification-visual-calculations]] — full ABC Pareto chart walkthrough
- [[visual-calculations-usage-guide]] — usage guide with more examples
