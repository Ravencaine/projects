---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter-modifier]
---

# REMOVEFILTERS

## Signature
```
REMOVEFILTERS([<table> | <column>[, <column>[, …]]])
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `table` or `column(s)` | table or column | The table or column(s) to remove filters from |

## Returns

**clears filters** — equivalent to `ALL(...)`, returns a filter-emptied table or column

## Examples

```dax
-- Remove all filters on the Date table
REMOVEFILTERS('Date')

-- Remove filter on a specific column
CALCULATE([Sales], REMOVEFILTERS('Product'[Color]))

-- Equivalent to ALL in a ratio denominator
% of Grand Total :=
DIVIDE(
    [Sales],
    CALCULATE([Sales], REMOVEFILTERS('Product'[Color]))
)
```

## Notes

- **Functionally equivalent to `ALL`** — both remove all filters on the specified table or columns.
- `REMOVEFILTERS` is the **preferred modern DAX** form because its intent is clearer: it signals "remove these filters" rather than "return all rows/values."
- Introduced as a more readable alias; `ALL` and `REMOVEFILTERS` are interchangeable in all contexts.

## Related

- [[all]] — functionally equivalent (predecessor form)
- [[calculate]] — primary consumer of REMOVEFILTERS
