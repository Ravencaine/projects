---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MIN and MINX

Returns the smallest value in a column or the smallest result of an expression evaluated over a table.

## MIN

```dax
MIN(<column>)
MIN(<expression1>, <expression2>)
```

## MINX

```dax
MINX(<table>, <expression>[, <variant>])
```

| Term | Definition |
|------|------------|
| `column` | The column to find the minimum in |
| `expression1`, `expression2` | Two scalar expressions |
| `table` | The table to iterate |
| `expression` | Evaluated per row |
| `variant` | (Optional) If TRUE, handles mixed data types |

## Returns

Smallest numeric, text, or date value.

## Examples

```dax
-- Minimum order date
First Order := MIN('Sales'[OrderDate])

-- Minimum calculated margin per row
Lowest Margin := MINX('Sales', DIVIDE([Profit], [Sales]))
```

## Notes

- MIN handles text (alphabetical comparison), dates, and numbers
- BLANK values are skipped
- MINX is an iterator; variant=TRUE supports mixed types by ordering ascending
- Two-expression form: MIN(1, [Sales]) — useful for clamping minimums

## Related

- [[max]]
- [[sumx]]
