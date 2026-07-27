---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MAX and MAXX

Returns the largest value in a column or the largest result of an expression evaluated over a table.

## MAX

```dax
MAX(<column>)
MAX(<expression1>, <expression2>)
```

## MAXX

```dax
MAXX(<table>, <expression>[, <variant>])
```

| Term | Definition |
|------|------------|
| `column` | The column to find the maximum in |
| `expression1`, `expression2` | Two scalar expressions |
| `table` | The table to iterate |
| `expression` | Evaluated per row |
| `variant` | (Optional) If TRUE, handles mixed data types |

## Returns

Largest numeric, text, or date value.

## Examples

```dax
-- Latest order date
Last Order := MAX('Sales'[OrderDate])

-- Highest calculated margin per row
Highest Margin := MAXX('Sales', DIVIDE([Profit], [Sales]))
```

## Notes

- MAX treats BLANK as 0 when comparing with numbers
- If both arguments are BLANK, MAX returns BLANK
- If either argument returns an error, MAX returns an error
- MAXX is an iterator; expression is evaluated in row context

## Related

- [[min]]
- [[minx]]
