---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter-modifier]
---

# ALLSELECTED

> **Extended 2026-07-27** — slicer-awareness teaching from Advanced Power BI DAX Measures (Jesse Ruiz)

## Signature
```
ALLSELECTED([<table> | <column>[, <column>[, …]]])
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `table` or `column(s)` | table or column | The table or column(s) to remove visual filters from |

## Returns

**table** or **column values** — values as they exist after slicer/filter pane selections, but before the visual-level filter

## Examples

```dax
-- All colors including those filtered out by the visual
All Colors in Visual :=
CALCULATE(
    [Sales],
    ALLSELECTED('Product'[Color])
)

-- % of visual total (not grand total)
% of Visual :=
DIVIDE(
    [Sales],
    CALCULATE([Sales], ALLSELECTED('Product'[Color]))
)
```

## Notes

- **`ALL` vs `ALLSELECTED`**:
  - `ALL` removes **all** filters including visual-level filters, slicers, and filter pane selections — returns the grand total.
  - `ALLSELECTED` removes only the **visual-level filter** — preserves slicer and filter pane selections, but ignores which rows the visual has filtered out.
- Use `ALLSELECTED` for calculating **ratios against the full visual context** — e.g., "what % of the visible data does this row represent?"
- A common pitfall: `ALLSELECTED` inside nested `CALCULATE` calls can behave unexpectedly due to its dependency on the visual query context.

## Related

- [[all]] — remove all filters (including visual)
- [[allexcept]] — selective filter preservation
- [[calculate]] — primary consumer of ALLSELECTED
