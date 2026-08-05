---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# SUM

## Signature

```dax
SUM(<column>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<column>` | The column of numbers to sum. |

## Returns

A decimal number representing the sum of all values in the column.

## Examples

```dax
SUM('Sales'[Amount])
```

## Notes

- Simple column aggregation — the most basic way to total a numeric column.
- **Ignores BLANK rows**: blank values are treated as zero.
- **Does not apply filters**: it operates over the entire column unless wrapped in `CALCULATE`.
- For **conditional summing** (with a filter), use `SUMX` or `CALCULATE(SUM(...), filter)`.
- Not an iterator — does not introduce row context.

## Related

- [[sumx]] — iterator-based sum for row-level calculations
- [[calculate]] — required to apply filters to SUM
- [[countrows]] — counts rows instead of summing values
