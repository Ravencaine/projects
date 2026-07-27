---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter-modifier]
---

# ALLEXCEPT

## Signature
```
ALLEXCEPT(<table>, <column>[, <column>[, …]])
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `table` | table | The base table (must be a direct table reference) |
| 2+ | `column(s)` | column | Columns to **keep** filters on |

## Returns

**table** — all rows of the base table, with filters removed except on the specified columns

## Examples

```dax
-- Keep Year filter, remove all others on Sales
Sales by Year :=
CALCULATE(
    [Sales],
    ALLEXCEPT('Sales', 'Date'[Year])
)

-- Keep both Year and Month, clear the rest
Sales YTD :=
CALCULATE(
    [Sales],
    ALLEXCEPT('Sales', 'Date'[Year], 'Date'[Month])
)
```

## Notes

- The **first argument must be a base table reference** — not a calculated table or sub-expression.
- Subsequent arguments must be **columns of that base table** — not arbitrary columns.
- Removes all context filters **except** those on the specified columns. Useful when you want to "slice by" specific dimensions (e.g., always keep Year context) while clearing everything else.
- Contrast with `ALL`, which removes all filters entirely, and `ALLSELECTED`, which removes only visual-level filters.

## Related

- [[all]] — remove all filters
- [[allselected]] — remove visual-level filters only
- [[calculate]] — primary consumer of ALLEXCEPT
