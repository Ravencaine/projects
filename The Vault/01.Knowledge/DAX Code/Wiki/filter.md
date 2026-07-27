---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, iterator]
---

# FILTER

## Signature
```
FILTER(<table>, <filter>)
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `table` | table | The table to filter (can be a table expression) |
| 2 | `filter` | Boolean | A Boolean expression evaluated per row |

## Returns

**table** — a filtered table containing only rows where `<filter>` is `TRUE`

## Examples

```dax
-- Basic filter on amount
FILTER('Sales', 'Sales'[Amount] > 1000)

-- Used inside CALCULATE for complex conditions
CALCULATE(
    [Sales],
    FILTER('Product', 'Product'[Color] = "Red")
)

-- Nested filter
FILTER(
    FILTER('Sales', 'Sales'[Year] = 2024),
    'Sales'[Amount] > 500
)
```

## Notes

- **Iterator function** — loops over every row in `<table>`, evaluating `<filter>` in the current row context. Can be expensive on large tables; prefer Boolean filter arguments in `CALCULATE` when possible.
- FILTER is needed when the filter condition **cannot** be expressed as a simple `Column = value` or `Column > value` (e.g., multi-column conditions, conditions referencing measures, or band/range filters).
- Returns a table, so it must be used:
  - As a filter argument inside `CALCULATE` / `CALCULATETABLE`
  - As the first argument of another table function
- **Performance tip**: `CALCULATE([Measure], Table[Column] = "Value")` is generally faster than `CALCULATE([Measure], FILTER(Table, Table[Column] = "Value"))` because the engine can use column filters directly instead of iterating.

## Related

- [[calculate]] — scalar context modifier (preferred for simple filters)
- [[all]] — remove filters
- [[avoid-using-filter-as-filter-argument]] — performance anti-pattern
