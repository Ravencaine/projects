---
created: 2026-08-06
updated: 2026-08-06
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: atomic
tags: [calculation-groups, precedence, application-order, evaluation-order, dax]
---

# Precedence Controls Application Order, Not Evaluation Order

Calculation group **precedence** determines which calculation item is applied **first** when multiple calculation groups are active. This is the order of **application:** the DAX engine transforming the measure expression — not the order of **evaluation** of the surrounding CALCULATE expressions.

## Definition

When two calculation groups are both active (e.g., Adder with precedence 100 and Multiplier with precedence 200), the DAX engine applies their calculation items in **ascending precedence order**: lower precedence first, higher precedence second. The result is a transformed expression, not a nested evaluation.

This is analogous to operator precedence in mathematics: `2 + 3 * 10` evaluates as `2 + (3 * 10)` because `*` has higher operator precedence — the `*` operation is applied first, even though it appears second in the text.

## Key Points

- Precedence governs **which measure reference** each calculation item touches — lower precedence is applied to the original measure reference; higher precedence is applied to the already-transformed result.
- The order of CALCULATE arguments has **no effect** on precedence.
- Higher precedence calculation items receive the **output** of lower precedence calculation items as their input — the chain is one expression transformation, not nested function calls.
- The visual filter/slicer application in a report uses group precedence. A CALCULATE with multiple calculation item filters uses precedence to decide application order.

## Examples

```dax
-- Adder precedence = 100, Multiplier precedence = 200
-- Expected: 2 * 10 + 5 = 25  (maths: multiply first)
-- Actual evaluation trace:

CALCULATE(
    [Just2],                -- initial expression: Just2 = 2
    Adder[Addend]="Plus5",
    Multiplier[Factor]="Mul10"
)

-- Step 1: Multiplier (precedence 200) applied first to [Just2]
-- Result: [Just2] * 10

-- Step 2: Adder (precedence 100) applied to the result of Step 1
-- Result: ([Just2] * 10) + 5

-- Final: (2 * 10) + 5 = 25
```

But if the user's CALCULATE wraps the **already-transformed** measure:

```dax
CALCULATE(
    [Just2Times10],         -- Just2Times10 already applies Mul10
    Adder[Addend]="Plus5"
)
-- Result: (2 * 10) + 5 = 25  (same formula, different trace)
```

## Related

- [[calculation-item-applies-only-to-measure-reference]]
- [[precedence-controls-application-not-evaluation]] — this note
- [[nested-calculate-does-not-change-application-order]]
- [[measure-applied-calculation-item-overrides-precedence]]
- [[measure-calculate-calc-item-breaks-precedence]]
