---
created: 2026-08-05
updated: 2026-08-05
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: gotcha
tags: [dax, calculation-groups, calculate, gotcha]
---

# Nested CALCULATE Does Not Change CG Application Order

You cannot control the order of calculation item application by nesting `CALCULATE` functions. Precedence always governs — nesting does not override it.

## Expected Behaviour

```dax
-- You might expect: inner CALCULATE fires first (Mul10),
-- outer CALCULATE fires second (Plus5)
-- Expected result: (2 * 10) + 5 = 25
CALCULATE (
    CALCULATE (
        [Just2],
        Multiplier[Factor] = "Mul10"
    ),
    Adder[Addend] = "Plus5"
)
```

## Actual Behaviour

Result is **70**, not 25. The inner `CALCULATE` applies the `Multiplier` calculation item to `[Just2]`, producing `[Just2] * 10`. Then the outer calculation item `Adder` applies to *that expression* — but `Adder`'s calculation item is applied to the `[Just2] * 10` expression, not to `[Just2]` directly.

The chain becomes: `([Just2] * 10) + 5 = (2 * 10) + 5 = 25` only if the inner result is still a measure reference. In the specific example, the result is 70 because the nested `CALCULATE` pattern in this article does not produce a second measure reference for the outer calculation item to target.

## Why It Happens

A calculation item is applied to a **measure reference**. The inner `CALCULATE` produces `[Just2] * 10` — not a new measure reference that can be further targeted by the outer calculation item. The outer `Adder` calculation item targets `[Just2]` inside the inner expression, but the `Multiplier` already fired first by precedence regardless of nesting.

## How to Handle It

- Do not use nested `CALCULATE` as a mechanism to control CG application order
- If you need a specific calculation order, use a measure that applies the calculation items internally — but understand that this overrides precedence entirely (see [[measure-that-applies-cg-overrides-precedence]])
- If you need precedence to govern, use report filters (slicers/rows/columns) to apply CGs — not measures or nested `CALCULATE`

## Related

- [[cg-precedence-application-not-evaluation]]
- [[report-filter-vs-measure-cg-behaviour]]
- [[measure-that-applies-cg-overrides-precedence]]


See also [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] — Source: [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] presents this as the third diagnostic puzzle before the core explanation.

See also [[calculation-items-apply-only-to-measure-references]] — See the nested CALCULATE still requires a measure reference for the outer CG item to fire.