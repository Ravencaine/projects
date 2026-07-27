---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# FILTERS and TOPN

Return the active filters on a column, or the top N rows of a table.

## FILTERS

```dax
FILTERS(<columnName>)
```

Returns the values that are **directly applied as filters** to `columnName` in the current context. Returns a column of values — use in a measure context.

```dax
-- Count how many filters are active on Product[Color]
Filter Count = COUNTROWS(FILTERS('Product'[Color]))
```

## TOPN

```dax
TOPN(<N>, <Table>[, <OrderBy_Expression>[, <Order>[, ...]]])
```

Returns the top N rows of `Table`, sorted by `OrderBy_Expression` (default: descending).

| Parameter | Definition |
|-----------|------------|
| `N` | Number of rows to return |
| `Table` | Source table |
| `OrderBy_Expression` | (Optional) Sort key |
| `Order` | (Optional) 0/DESC = descending, 1/ASC = ascending |

```dax
-- Top 10 products by sales
Top 10 Products =
TOPN(
    10,
    'Product',
    [Sales],
    0
)
```

> TOPN may return more than N rows if there are ties in the OrderBy expression.

## Notes

- FILTERS returns a **column of filter values** — typically used with COUNTROWS or in CALCULATE
- FILTERS: not supported in DirectQuery mode for calculated columns or RLS rules
- TOPN can have multiple ORDER BY columns for tie-breaking
- TOPN is often used inside CALCULATETABLE to create a filtered set
- Related: [[rownumber]], [[rankx]]

## Related

- [[rownumber]]
- [[rankx]]
