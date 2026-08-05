---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [mod, rounding, floating-point, workaround, math]
---

# Better MOD Workaround

A corrected implementation of the modulo operation in DAX that handles floating-point/decimal divisors correctly, where the native `MOD()` function produces incorrect alternating results.

## The Bug

`MOD(value, divisor)` in DAX has a floating-point precision bug when the divisor is a decimal number. For example:

```dax
MOD( [Value], .02 )
```

Returns values alternating between `.01` and `.02` — clearly incorrect. The root cause: the modulo function is mathematically defined only for integers, and DAX's implementation breaks down with decimal divisors due to floating-point representation.

## The Fix: TRUNC-based Floating-Point MOD

```dax
Better MOD =
VAR __Value = [Value]
VAR __Divisor = .02
VAR __Divide =
    ROUND(
        DIVIDE( __Value, __Divisor, 0 ),
        LEN( __Divisor & "" )
    )
VAR __FMod = ( __Divide - TRUNC( __Divide ) ) * __Divisor
VAR __Result =
    IF(
        TRUNC( __Divisor ) = __Divisor
        && TRUNC( __Value ) = __Value,
        MOD( __Value, __Divisor ),
        __FMod
    )
RETURN
    __Result
```

**How it works:**

1. **`__Divide`**: divides the value by the divisor, rounds to a precision based on the divisor's decimal places (using `LEN(__Divisor & "")` to detect how many decimal places the divisor has)
2. **`__FMod`**: the floating-point modulo: subtracts the integer portion (`TRUNC`) from the rounded quotient and multiplies back by the divisor
3. **`__Result`**: if both value and divisor are integers, use the native `MOD` (it's correct for integers); otherwise use the `__FMod` calculation

The key insight is that `ROUND` with dynamically detected precision cleans up the floating-point representation before the subtraction, and `TRUNC` cleanly extracts the integer part.

## When to Use This

- When dividing by decimal numbers (e.g., `.02`, `0.5`, `3.14`)
- When `MOD()` produces visibly wrong alternating patterns
- In financial calculations involving fractional units

For integer divisors, the native `MOD()` works correctly and should be used directly.

## Related

- [TRUNC vs INT](/wiki/trunc-vs-int-dax.md) — why `TRUNC` is used instead of `INT` in this formula
- [DIVIDE](/wiki/divide-function-vs-divide-operator.md) — safe division used here
- [ROUND](/wiki/round.md) — the rounding function that cleans up floating-point representation
- [MOD](/wiki/mod.md) — the native (buggy for decimals) modulo function
- [Better MEDIAN](/wiki/better-median-workaround-dax.md) — another DAX function with a workaround
