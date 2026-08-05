---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MAX / MAXA / MAXX and MIN / MINA / MINX

Find the largest or smallest value — column-based or iterator-based.

## MAX / MIN (Column)

```dax
MAX(<column>)
MIN(<column>)
```

Returns the largest/smallest value in a column (numbers, dates, or text alphabetically).

## MAXA / MINA (Column with logicals)

```dax
MAXA(<column>)
MINA(<column>)
```

Same as MAX/MIN but also considers **logical values**: TRUE = 1, FALSE = 0. Empty cells are ignored; returns 0 if the column has no usable values.

## MAXX / MINX (Iterator)

```dax
MAXX(<table>, <expression>[, <variant>])
MINX(<table>, <expression>[, <variant>])
```

Iterates over `table`, evaluates `expression` per row, returns the max/min result.

| Term | Definition |
|------|------------|
| `variant` | (Optional) If TRUE, returns the highest/lowest value when mixed types are compared |

## Examples

```dax
-- Max/Min from a column
Max Price = MAX('Product'[Price])
Min Date = MIN('Sales'[OrderDate])

-- Max including TRUE/FALSE column
Max Flag = MAXA('Status'[IsActive])

-- Max revenue per row
Max Revenue Any Product = MAXX(
    'Sales',
    RELATED('Product'[Price]) * 'Sales'[Quantity]
)

-- Min margin per product
Min Margin = MINX('Product', [Price] - [Cost])
```

## Notes

- MAX/MIN work with text (alphabetical comparison), numbers, and dates
- MAXA/MINA handle logical values — use when your column contains booleans
- MAXX/MINX are iterators — can compute per-row expressions before aggregating
- The `variant` parameter handles mixed-type comparisons (rarely needed)
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[sumx]], [[average]]

## Related

- [[sumx]]
- [[average]]
