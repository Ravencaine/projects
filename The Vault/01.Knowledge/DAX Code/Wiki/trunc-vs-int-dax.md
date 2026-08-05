---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: gotcha
tags: [gotcha, rounding, trunc, int, negative-numbers]
---

# TRUNC vs INT: The Negative Number Bug

For positive numbers, `TRUNC` and `INT` behave identically — both return the integer portion. For **negative numbers**, they diverge catastrophically: `INT` rounds toward negative infinity (more negative), while `TRUNC` truncates toward zero.

## The Gotcha

```dax
INT( -2.1 )   -- returns -3  (rounds DOWN toward negative infinity)
TRUNC( -2.1 ) -- returns -2  (truncates TOWARD zero)
```

For negative numbers, `INT` is almost never what you want. If you write `INT()` expecting to drop the decimal portion, you'll get a value one step further from zero than intended.

## When This Matters

Any calculation involving negative numbers where you expect to extract the integer portion — financial data (losses, refunds, negative margins), statistical computations, or any currency/math operation where negative values are possible.

## The Full DAX Rounding Suite

| Function | Behavior | Notes |
|---------|----------|-------|
| `INT(x)` | Rounds to next integer **away from zero** for negatives | **Bug risk with negatives** |
| `TRUNC(x)` | Removes decimal portion, rounds toward zero | Safe for negatives |
| `ROUND(x, d)` | Rounds to d decimals, away from zero if >= 5 | Negative d rounds left of decimal |
| `ROUNDDOWN(x, d)` | Rounds toward zero (closer to zero) | Unlike `TRUNC` for d < 0 |
| `ROUNDUP(x, d)` | Rounds away from zero | |
| `MROUND(x, m)` | Rounds to nearest multiple of m | Error if signs differ |
| `CEILING(x, m)` | Rounds up (away from zero) to nearest multiple | Error if m negative, x positive |
| `ISO.CEILING(x, m)` | Same as CEILING but handles negative multiples | ISO standard behavior |
| `FLOOR(x, m)` | Rounds down (toward zero) to nearest multiple | |
| `EVEN(x)` | Rounds away from zero to nearest even integer | |
| `ODD(x)` | Rounds away from zero to nearest odd integer | |
| `CURRENCY(x)` | Returns currency format, rounds to 4 decimals | |

## Demonstration Table

```dax
Decimals = GENERATESERIES( -15, 15.01, .01 )
```

Then add columns:
```dax
Int = INT( [Value] )
Trunc = TRUNC( [Value] )
```

For 0 and all positive numbers: `INT` = `TRUNC`. For every negative number: `TRUNC = INT + 1` (unless the number is exactly an integer).

## Fix

Always use `TRUNC` when you mean "drop the fractional part." Reserve `INT` only if you explicitly want floor behavior for both positive and negative numbers (rare).

```dax
-- Safe: drop decimals for all numbers (including negatives)
SafeInt = TRUNC( [Value] )

-- Dangerous: for -2.1, returns -3 instead of -2
RiskyInt = INT( [Value] )
```

## Related

- [Better MOD Workaround](/wiki/better-mod-workaround-dax.md) — TRUNC is the fix for MOD's decimal bug
- [Rounding functions overview](/wiki/round-trunc-int.md) — existing KB note
- [ROUND](/wiki/round.md) — the full rounding family
- [CEILING / FLOOR](/wiki/math-and-trig-functions-overview.md) — multiple/rounding functions
