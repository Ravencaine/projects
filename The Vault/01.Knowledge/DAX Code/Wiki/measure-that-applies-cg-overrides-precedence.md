---
created: 2026-08-05
updated: 2026-08-05
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: gotcha
tags: [dax, calculation-groups, precedence, gotcha, measure]
---

# Measure That Applies a CG Overrides Precedence

Defining a measure that internally calls `CALCULATE` with a calculation item **breaks the precedence mechanism**. The calculation item inside the measure fires at the measure's evaluation time, not at the precedence-governed application time.

## Expected Behaviour

A measure `Just2Times10` that applies `Multiplier` internally should still respect the external `Adder` precedence when `Adder` is applied via a report filter.

## Actual Behaviour

The `Multiplier` calculation item fires **inside** the measure when `Just2Times10` is evaluated — before the external `Adder` calculation item gets a chance to apply to `[Just2]`. The result is `([Just2] * 10) + 5 = 25`, not `((2 + 5) * 10) = 70`.

## Why It Happens

When a measure contains `CALCULATE([Measure], CG[item]="value")`, the calculation item is part of the measure's own expression. When the measure is evaluated, its internal calculation item fires as part of that evaluation. External calculation items from report filters apply to the measure reference — but `Multiplier` has already been applied inside the measure.

## Example

```dax
-- CG precedence: Multiplier (200) > Adder (100)

Just2Times10 :=
CALCULATE (
    [Just2],
    Multiplier[Factor] = "Mul10"
)

-- Query from report with Adder slicer:
-- CALCULATE ( [Just2Times10], Adder[Addend] = "Plus5" )

-- Step 1: Adder applies to [Just2Times10]
-- Step 2: [Just2Times10] evaluates → [Just2] * 10 fires internally
-- Step 3: Multiplier fires inside the measure
-- Final: ([Just2] * 10) + 5 = 25

-- But with both CGs applied via report filter (no internal call):
-- DAX applies by precedence: Multiplier first, Adder second
-- Result: (2 * 10) + 5 = 70
```

## How to Handle It

- If you want precedence to control: apply CGs via report filters only
- If you want to enforce a specific order: use a measure that internally applies CGs — but document this clearly as it overrides user-controlled precedence
- Understand that **users can break well-engineered calculations** by creating their own measures that use CGs with `CALCULATE` — this overrides the report's precedence settings

## Related

- [[report-filter-vs-measure-cg-behaviour]]
- [[cg-precedence-application-not-evaluation]]
- [[nested-calculate-does-not-change-cg-application-order]]


See also [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] — Source: [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] introduces this as the fourth diagnostic puzzle and the core takeaway.

See also [[calculation-items-apply-only-to-measure-references]] — See the override happens because the measure produces a different measure reference for the external CG to target.