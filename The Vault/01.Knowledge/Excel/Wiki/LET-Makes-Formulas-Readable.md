---
created: 2026-08-09
updated: 2026-08-09
source: "5 Hidden Excel Formula Rules Every Pro Follows • My Online Training Hub"
note_type: atomic
tags: [excel, formulas, let, variables, readability, let-function]
---

# LET Makes Formulas Readable

`LET` assigns named variables inside a formula. Replace repeated expressions with named variables — formulas read like sentences and Excel evaluates each named expression only once (performance benefit for complex formulas).

## Syntax

```
=LET(
  name1, expression1,
  name2, expression2,
  ...final_expression
)
```

## Example: Commission Formula

```
=LET(
  eligible, AND(C5<>"", E5="Active"),
  rate, XLOOKUP(D5, CommTbl[Sales Band], CommTbl[Rate],, -1),
  D5 * rate * eligible
)
```

Steps:
1. `eligible` — checks name exists and status is Active
2. `rate` — looks up the commission band for the sales amount
3. Final expression — multiplies sales × rate × eligible

Same output as nested IF + helper column approach, but self-contained in one cell with named variables.

## When to Use LET

- Any formula where the same expression appears more than once
- Complex formulas that are hard to follow step-by-step
- Intermediate concepts that deserve a name (eligibility, band, margin, etc.)

## LET vs Helper Columns

| | LET | Helper Columns |
|--|-----|---------------|
| Location | Inside formula | Separate column |
| Reuse | Not reusable elsewhere | Referenced by other formulas |
| Readability | Named variables | Separate labeled column |
| Best for | One-off complex formulas | Multi-formula shared logic |

## Related

- [[Source-5-Hidden-Excel-Formula-Rules-Mynda-Treacy]] — source
- [[Helper-Columns-Build-for-Humans]] — LET is the in-cell alternative to helper columns
- [[LAMBDA-Custom-Functions-via-Name-Manager]] — LAMBDA wraps LET for reuse via Name Manager
