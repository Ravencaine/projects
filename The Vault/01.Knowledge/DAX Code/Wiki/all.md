---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, filter-modifier]
---

# ALL

## Signature
```
ALL([<table> | <column>[, <column>[, …]]])
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `table` or `column(s)` | table or column | The table or column(s) to clear filters on |

## Returns

**table** or **column values**: all rows / all values with filters removed from the specified arguments

## Examples

```dax
-- Remove all filters on the Date table
CALCULATE([Sales], ALL('Date'))

-- Remove filter on a specific column only
CALCULATE([Sales], ALL('Product'[Color]))

-- Ratio against total (denominator)
% of Total :=
DIVIDE([Sales], CALCULATE([Sales], ALL('Product'[Color])))

-- ALL on multiple columns in a table
CALCULATE([Sales], ALL('Product'[Color], 'Product'[Category]))
```

## Notes

- Removes **all** filters on the specified table or columns, regardless of visual-level, slicer, or filter pane selections.
- When passed a **table**: returns all rows of that table.
- When passed **column(s)**: returns all distinct values of those columns (acts as a filter remover).
- A fundamental building block for **denominator calculations** (ratios, percentages, "as of total" measures).
- Variations:
  - `ALLEXCEPT` — keep selected column filters
  - `ALLSELECTED` — remove only visual-level filters
  - `ALLNOBLANKROW` — remove filters and blank rows
  - `ALLCROSSFILTERED` — clear cross-filter direction

## Related

- [[allexcept]] — selective filter preservation
- [[allselected]] — visual-level filter removal
- [[removefilters]] — functionally equivalent (modern alias)
- [[calculate]] — primary consumer of ALL
