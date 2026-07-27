---
created: 2026-07-26
source: dax.pdf
note_type: gotcha
tags: [dax, gotcha, divide, blank]
---

# DIVIDE Function vs Divide Operator

`DIVIDE()` and the `/` operator both perform division, but they handle division by zero differently.

## Expected Behaviour

Both should return the quotient of numerator and denominator.

## Actual Behaviour

- `/` (divide operator): returns an error if the denominator is zero or BLANK
- `DIVIDE()`: returns BLANK if the denominator is zero or BLANK — unless you provide an alternate result

```dax
-- Returns ERROR if Sales = 0
Profit Margin := [Profit] / [Sales]

-- Returns BLANK if Sales = 0
Profit Margin := DIVIDE([Profit], [Sales])
```

## Why It Happens

The divide operator is strict: division by zero raises an error. `DIVIDE` is designed for DAX measure safety — it handles zero-denominator gracefully by returning BLANK.

## How to Handle It

Use `DIVIDE` when the denominator is an expression that could return zero or BLANK. Use `/` when the denominator is a constant value known to be non-zero.

```dax
-- Good: denominator could be zero
Profit Margin := DIVIDE([Profit], [Sales])

-- Good: constant denominator is never zero
Pi := DIVIDE(22, 7)

-- Never: 3rd arg substitutes BLANK with 0 (anti-pattern)
Profit Margin := DIVIDE([Profit], [Sales], 0)
```

## Related Gotchas

- [[avoid-converting-blanks-to-values]] — explains why the 3rd argument of DIVIDE is an anti-pattern
