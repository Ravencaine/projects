---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# POWER, LOG, LOG10, EXP, PI

Exponentials, logarithms, and constants.

## POWER

```dax
POWER(<number>, <power>)
```

Raises a number to a power. Equivalent to `number ^ power`.

```dax
POWER(5, 2)       -- 25
POWER([Value], 3) -- cube
```

## LOG

```dax
LOG(<number>[, <base>])
```

Logarithm of `number` to the specified base. Base defaults to 10.

```dax
LOG(100)          -- 2 (base 10)
LOG(100, 10)      -- 2
LOG(8, 2)         -- 3 (log base 2 of 8)
```

## LOG10

```dax
LOG10(<number>)
```

Common logarithm — base 10 only.

```dax
LOG10(1000)       -- 3
```

## EXP

```dax
EXP(<number>)
```

Returns e raised to the specified power. e ≈ 2.71828.

```dax
EXP(1)            -- ~2.71828
EXP([GrowthRate]) -- e^x for exponential modelling
```

## PI

```dax
PI()
```

Returns the value of π (3.14159...). No arguments.

```dax
Circumference = 2 * PI() * [Radius]
Area = PI() * POWER([Radius], 2)
```

## Notes

- LOG of a non-positive number → error
- EXP(1) ≈ 2.71828 — useful for natural exponential models
- LN is not available in DAX; use LOG with base e: `LOG(x, EXP(1))` = ln(x)
- Related: [[sqrt]], [[power]]

## Related

- [[power]]
- [[sqrt]]
