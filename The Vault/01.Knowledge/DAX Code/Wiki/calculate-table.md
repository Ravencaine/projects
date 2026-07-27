---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter-context]
---

# CALCULATETABLE

## Signature
```
CALCULATETABLE(<expression>[, <filter1> [, <filter2> [, …]]])
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `expression` | table | Must be a **table expression** (not scalar) |
| 2+ | `filter1`, `filter2`, … | filter | Boolean or table filter expressions |

## Returns

**table**

## Examples

```dax
-- Filtered Sales table for red products
CALCULATETABLE('Sales', 'Product'[Color] = "Red")

-- Used inside a measure
Red Sales Total :=
CALCULATE(
    SUMX(CALCULATETABLE('Sales', 'Product'[Color] = "Red"), Sales[Amount]),
    ...
)
```

## Notes

- Shares the same filter logic as `CALCULATE`, but the first argument must be a **table expression** rather than a scalar expression.
- Returns a table, so it is used:
  - As the table argument to other table functions (e.g., `SUMX`, `FILTER`, `ADDCOLUMNS`)
  - Directly in measures that consume a table result
  - As a table variable inside `CALCULATE`
- `CALCULATE` is the scalar-returning counterpart.

## Related

- [[calculate]] — scalar-returning counterpart
- [[filter]] — iterator filter function
- [[all]] — clear filters
