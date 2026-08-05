---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# Rounding: ROUND, ROUNDDOWN, ROUNDUP, TRUNC, INT

Control decimal precision and truncation.

## ROUND

```dax
ROUND(<number>, <num_digits>)
```

Rounds to specified decimal places. Ties round **half away from zero** (commercial rounding).

| `num_digits` | Effect |
|---|---|
| > 0 | Right of decimal |
| 0 | Nearest integer |
| < 0 | Left of decimal (e.g., -1 = nearest 10) |

## ROUNDDOWN / ROUNDUP

```dax
ROUNDDOWN(<number>, <num_digits>)   -- toward zero
ROUNDUP(<number>, <num_digits>)     -- away from zero
```

## TRUNC

```dax
TRUNC(<number>[, <num_digits>])
```

Truncates — removes the fractional part without rounding.

> TRUNC(-4.3) = -4 | INT(-4.3) = -5

## INT

```dax
INT(<number>)
```

Rounds down to the nearest integer (toward negative infinity for negatives).

> INT(-4.3) = -5 (lower number) | TRUNC(-4.3) = -4 (drop fraction)

## CEILING / FLOOR

```dax
CEILING(<number>, <significance>)  -- round up to nearest multiple
FLOOR(<number>, <significance>)    -- round down to nearest multiple
```

```dax
-- Round to nearest 0.05
Price = CEILING([RawPrice], 0.05)

-- Round down to nearest $100
Bucket = FLOOR([Revenue], 100)
```

## MOD

```dax
MOD(<number>, <divisor>)
```

Returns the remainder after division. Always has the same sign as the divisor. Division by zero → error.

```dax
MOD(ROW_NUMBER, 2)    -- even/odd classification
MOD([Year], 5)         -- grouping into 5-year blocks
```

## QUOTIENT

```dax
QUOTIENT(<number>, <divisor>)
```

Returns the integer portion of division (truncates toward zero).

```dax
QUOTIENT([Days], 7)   -- number of full weeks
```

## Notes

- INT vs TRUNC: same for positive numbers; different for negatives
- CEILING/FLOOR: both arguments must have the same sign, or an error is returned
- MOD(n, d) = n - d*INT(n/d)
- Related: [[divide]]

## Related

- [[divide]]
