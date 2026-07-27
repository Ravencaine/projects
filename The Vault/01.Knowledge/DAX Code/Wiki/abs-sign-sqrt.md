---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# ABS, SIGN, SQRT

Basic numeric operations: absolute value, sign, and square root.

## ABS

```dax
ABS(<number>)
```

Returns the absolute value (removes the sign).

```dax
ABS([Cost] - [Price])        -- always positive
ABS('Sales'[Quantity] * -1)   -- handle negatives gracefully
```

## SIGN

```dax
SIGN(<number>)
```

Returns: 1 (positive), 0 (zero), -1 (negative).

```dax
SIGN([Profit])                -- direction of profit
SIGN([Forecast] - [Actual])   -- over/under performance
```

## SQRT

```dax
SQRT(<number>)
```

Returns the square root. Returns an error if the number is negative.

```dax
SQRT([Variance])              -- standard deviation from variance
SQRT(ABS([Value]))            -- safe sqrt (handle negatives)
```

## Notes

- SQRT of a negative number → error; wrap in ABS if needed
- SIGN is useful for conditional logic based on direction rather than magnitude
- Related: [[power]]

## Related

- [[power]]
