---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, utility]
---

# COALESCE

## Signature

```dax
COALESCE(<expr1>, <expr2>, ...)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `expr1, expr2, …` | Expressions to evaluate in order, left to right |

## Returns

The **first expression** that does not evaluate to `BLANK()`. Returns `BLANK()` if all arguments are `BLANK()`.

## Examples

```dax
-- Return the first non-blank value among Profit, Revenue, or 0
COALESCE([Profit], [Revenue], 0)

-- Use selected year parameter, or default to current year
COALESCE(SELECTEDVALUE('Param'[Year]), YEAR(TODAY()))
```

## Notes

- Returns `BLANK()` if all arguments evaluate to `BLANK()`.
- Useful for providing fallback values without nested `IF`s.
- Expressions are evaluated left to right.

## Related

- [[if]]
- [[switch]]
- [[blank]]
