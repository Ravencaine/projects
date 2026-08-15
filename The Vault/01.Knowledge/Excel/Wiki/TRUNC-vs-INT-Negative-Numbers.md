---
created: 2026-08-09
updated: 2026-08-09
source: "5 Boring Excel Functions That Are Secretly Brilliant • My Online Training Hub"
note_type: atomic
tags: [excel, functions, trunc, int, negative-numbers, whole-numbers, division]
---

# TRUNC vs INT: Negative Number Behavior

Both `TRUNC` and `INT` remove the decimal portion of a number. For positive numbers they behave identically. For negative numbers they diverge critically: `TRUNC` moves toward zero; `INT` always rounds down.

## Syntax

```
=TRUNC(number, [num_digits])
=INT(number)
```

## Positive Numbers: Identical

```
=TRUNC(19.95) → 19
=INT(19.95)   → 19
```

## Negative Numbers: Different

```
=TRUNC(-150.50) → -150   (moves toward zero)
=INT(-150.50)   → -151   (always rounds down)
```

## TRUNC Use Cases

### Split Dollars and Cents

```
=TRUNC(19.95)      → 19    (dollars)
=19.95 - TRUNC(19.95) → 0.95   (cents)
```

### Whole Items from Division

```
Budget: $500, Cost per licence: $79
=TRUNC(500/79) → 6  (whole licences you can afford)
=500 - TRUNC(500/79)*79 → $26  (remaining budget)
```
Or more elegantly: `=MOD(500, 79)` → `26`

Applicable to: shipment boxes, team formations, full weeks, equipment allocation, resource planning.

## When to Choose TRUNC Over INT

Always use `TRUNC` when:
- Negative numbers are possible in the data
- You need to split a number into integer + fractional parts
- You want truncation behavior (toward zero), not floor behavior (always down)

## Related

- [[Source-5-Boring-Excel-Functions-Mynda-Treacy]] — source
