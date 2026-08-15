---
created: 2026-08-09
updated: 2026-08-09
source: "5 Boring Excel Functions That Are Secretly Brilliant • My Online Training Hub"
note_type: atomic
tags: [excel, functions, sign, sumproduct, or-logic, double-counting, logical-test]
---

# SIGN: Three-Way Output for OR Logic in SUMPRODUCT

`SIGN(number)` returns the sign of a number as a compact three-value output: `1` (positive), `0` (zero), `-1` (negative). The key application is preventing double-counting in SUMPRODUCT OR logic.

## Syntax

```
=SIGN(number)
```

## The Problem: Double-Counting in OR Logic

When combining two conditions with OR in SUMPRODUCT:
```
=(Units>100) + (Price>20)
```
Excel treats TRUE=1, FALSE=0. When **both** conditions are TRUE:
```
1 + 1 = 2
```
→ that row is counted twice. Every overlapping row inflates the result.

## The Fix: SIGN()

```
=SIGN((Units>100) + (Price>20))
```

SIGN collapses the OR result:
| Condition sum | SIGN result |
|---------------|-------------|
| 0 | 0 (neither met) |
| 1 | 1 (one met) |
| 2 | 1 (both met — collapses to 1) |

Every qualifying row is included **once and only once**.

## Why It Works

`SIGN((A)+(B))` is a boolean OR in arithmetic form:
- 0 → 0 (neither true)
- 1 → 1 (one true)
- 2 → 1 (both true — SUM's double-count collapses to 1)

This is the cleanest way to do OR logic inside SUMPRODUCT without helper columns or IF statements.

## Related

- [[Source-5-Boring-Excel-Functions-Mynda-Treacy]] — source
- [[ABS-Absolute-Value]] — another logical function pair; ABS handles magnitude, SIGN handles OR collapse
