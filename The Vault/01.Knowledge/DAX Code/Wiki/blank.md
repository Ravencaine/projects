---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, scalar]
---

# BLANK

Returns a blank value.

## Signature

```dax
BLANK()
```

## Returns

A BLANK value (empty cell in Excel/Power BI).

## Examples

```dax
-- Return blank instead of zero
Profit Margin :=
IF([Sales] = 0, BLANK(), DIVIDE([Profit], [Sales]))

-- Use BLANK as the alternate result in IF
IF([Amount] < 0, [Amount], BLANK())
```

## Notes

- BLANK is **not the same as zero** (0) or an empty string (""):
  - Numeric 0 evaluates to FALSE in Boolean expressions
  - BLANK evaluates to FALSE in numeric contexts but propagates BLANK in aggregations
- BLANK + number = number; BLANK - number = number; BLANK * number = BLANK
- `BLANK() = BLANK()` returns TRUE
- `BLANK() = 0` returns FALSE
- In measures, BLANK propagates through expressions and visual filters hide BLANK rows by default
- Never convert BLANK to zero — let BLANK propagate through your measures for correct filtering behaviour
- Related: [[avoid-converting-blanks-to-values]], [[divide-function-vs-divide-operator]]

## Related

- [[avoid-converting-blanks-to-values]]
- [[divide-function-vs-divide-operator]]
- [[coalesce]]
