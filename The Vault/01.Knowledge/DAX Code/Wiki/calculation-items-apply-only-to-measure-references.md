---
created: 2026-08-05
updated: 2026-08-05
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: atomic
tags: [dax, calculation-groups, calculation-items, measure-reference]
---

# Calculation Items Apply Only to Measure References

A calculation item only activates when the expression contains a **direct measure reference**. If there is no measure to target, the calculation item is silently skipped — it has nowhere to apply.

## Expected Behaviour

You might expect a calculation item defined as `SELECTEDMEASURE() + 5` to add 5 to any numeric result, regardless of where that number comes from.

## Actual Behaviour

If the enclosing expression is a constant (no measure reference), the calculation item does nothing. The result is unchanged.

## Why It Happens

`SELECTEDMEASURE()` represents "the measure currently being evaluated." If no measure is being evaluated — only a literal value — there is nothing for `SELECTEDMEASURE()` to resolve to, and DAX skips the application.

## Example

```dax
-- Calculation item: Plus5 = SELECTEDMEASURE() + 5
-- Calculation item: Mul10 = SELECTEDMEASURE() * 10

-- Result: 2 — calculation items silently ignored
-- because [Just2] is a measure returning 2,
-- but the CALCULATE argument is the constant 2, not [Just2]
EVALUATE
CALCULATETABLE (
    ROW ( "Result", 2 ),
    Adder[Addend] = "Plus5",
    Multiplier[Factor] = "Mul10"
)
```

The `CALCULATE` argument is `2` (a constant), not `[Just2]` (a measure reference). No measure → no application.

## How to Handle It

Always ensure the expression being wrapped by a calculation item contains a measure reference — either a direct measure call like `[Sales]` or a measure that itself evaluates to a measure reference.

## Related

- [[calculation-items-apply-only-to-measure-references]]
- [[cg-precedence-application-not-evaluation]]
- [[nested-calculate-does-not-change-cg-application-order]]


See also [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] — See [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] for the full source article with the four diagnostic puzzles.

See also [[report-filter-vs-measure-cg-behaviour]] — See [[report-filter-vs-measure-cg-behaviour]] for the distinction between report filter and measure invocation paths.

See also [[measure-that-applies-cg-overrides-precedence]] — See [[measure-that-applies-cg-overrides-precedence]] for how a measure with a CG argument overrides precedence entirely.