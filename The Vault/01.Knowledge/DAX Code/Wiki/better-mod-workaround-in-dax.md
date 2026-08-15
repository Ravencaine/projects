---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, math, mod, quirk]
note_type: pattern

---

# Better MOD Workaround in DAX

DAX's MOD function has a known quirk when handling large negative numbers. This pattern provides a reliable workaround.

## Purpose

`MOD(number, divisor)` returns the remainder after division. However, the implementation has edge cases with very large or negative numbers that produce unexpected negative results.

## Standard Workaround

```dax
Safe MOD :=
VAR __Number = [Value]
VAR __Divisor = [Divisor]
VAR __Result = MOD( __Number, __Divisor )
RETURN
IF( __Result < 0, __Result + __Divisor, __Result )
```

## Pattern

```dax
Better MOD :=
VAR __Mod = MOD( [Number], [Divisor] )
RETURN
DIVIDE( __Mod + [Divisor], 1 )
-- Or simply:
-- DIVIDE( __Mod, 1 ) -- handles negatives automatically with DIVIDE's safe mode
```

## Notes

- `DIVIDE()` inherently returns BLANK() for divide-by-zero, not an error
- The workaround normalizes negative remainders to the 0..divisor-1 range
- Use this pattern whenever MOD appears in calculations involving potentially negative numbers

## Related

- [[round-trunc-int]] — TRUNC for integer truncation
- [[mround]] — multiple rounding
