---
created: 2026-08-05
updated: 2026-08-05
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: atomic
tags: [dax, calculation-groups, precedence, application-order]
---

# CG Precedence = Application Order, Not Evaluation Order

CG precedence defines the **order in which calculation items are applied** to a measure — not the order in which the resulting expressions are evaluated. These are different operations.

## Expected Behaviour

You might assume that setting precedence = 200 (higher) means "this calculation group runs last" — like a stack where higher priority runs later.

## Actual Behaviour

The higher-precedence calculation group **runs first**. Precedence controls the chain of transformations applied to the measure reference, from first to last.

## Why It Happens

DAX applies each calculation item as a transformation to the measure expression:

1. Start with `[Just2]`
2. Highest precedence CG (Multiplier, 200) applies first: `[Just2] * 10`
3. Next precedence CG (Adder, 100) applies second: `([Just2] * 10) + 5`
4. Result: `(2 * 10) + 5 = 25`

## Key Distinction

| Concept | Meaning |
|---------|---------|
| Precedence = 200 (Multiplier) runs first | Higher number = applied first |
| Precedence = 100 (Adder) runs second | Lower number = applied later |

Mathematically this is correct: `(2 * 10) + 5` ≠ `(2 + 5) * 10` — so applying multiplication first produces the mathematically expected result.

## Important

The position of a calculation item argument inside `CALCULATE` has **no effect** on application order. Only CG precedence governs which CG fires first.

## Related

- [[calculation-items-apply-only-to-measure-references]]
- [[nested-calculate-does-not-change-cg-application-order]]
- [[measure-that-applies-cg-overrides-precedence]]


See also [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] — Source: [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] demonstrates the precedence/application distinction through four worked puzzles.

See also [[report-filter-vs-measure-cg-behaviour]] — See [[report-filter-vs-measure-cg-behaviour]] for the complementary case where precedence does NOT govern the outcome.