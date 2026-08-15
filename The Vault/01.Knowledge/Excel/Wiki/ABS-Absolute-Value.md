---
created: 2026-08-09
updated: 2026-08-09
source: "5 Boring Excel Functions That Are Secretly Brilliant • My Online Training Hub"
note_type: atomic
tags: [excel, functions, abs, absolute-value, percentage-change, tolerance-check]
---

# ABS: Absolute Value

`ABS(number)` removes the sign from a number, returning always-positive magnitude. Available in all Excel versions.

## Syntax

```
=ABS(number)
```

## Key Use Cases

### 1. Correct % Change When Prior Year Is Negative

Naive formula:
```
=(Current Year - Prior Year) / Prior Year
```
Fails when Prior Year is negative (e.g. expenses/losses): dividing by a negative gives the wrong sign.

Fixed formula:
```
=(Current Year - Prior Year) / ABS(Prior Year)
```
`ABS` forces the denominator positive, so the result correctly reflects whether change is favourable or adverse.

### 2. Invoice Tolerance Check

Use `ABS` to check whether an invoice differs from a purchase order by more than a tolerance — without separate tests for over/under:

```
=IF(ABS(InvoiceAmount - POAmount) <= POAmount * 0.1, "OK", "Check")
```

Convert the difference to magnitude; test once, not twice.

## Why It Matters

Most formulas assume positive inputs. `ABS` lets you write formulas that work correctly even when values go negative — without adding conditional branches.

## Related

- [[Source-5-Boring-Excel-Functions-Mynda-Treacy]] — source
- [[SIGN-Function-OR-Logic-SUMPRODUCT]] — companion logical function for SUMPRODUCT
