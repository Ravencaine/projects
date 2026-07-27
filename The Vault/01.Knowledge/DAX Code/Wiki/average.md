---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# AVERAGE and AVERAGEX

Returns the arithmetic mean of values in a column or of an expression evaluated over a table.

## AVERAGE

```dax
AVERAGE(<column>)
```

| Term | Definition |
|------|------------|
| `column` | The column containing the numbers to average |

## AVERAGEX

```dax
AVERAGEX(<table>, <expression>)
```

| Term | Definition |
|------|------------|
| `table` | The table over which to iterate |
| `expression` | Evaluated per row; the value to average |

## Returns

Decimal number.

## Examples

```dax
-- Average rating
Avg Rating := AVERAGE('Reviews'[Rating])

-- Average margin per row
Avg Margin := AVERAGEX('Sales', DIVIDE([Profit], [Sales]))
```

## Notes

- Ignores BLANK values, text, and logical values
- Includes 0 (zero) in the average
- Returns BLANK when no rows qualify
- AVERAGEX is an iterator — expression is evaluated in row context
- No DIVIDE equivalent for averaging — use AVERAGEX or CALCULATE to apply filters

## Related

- [[sumx]]
- [[average]]
- [[calculate]]
