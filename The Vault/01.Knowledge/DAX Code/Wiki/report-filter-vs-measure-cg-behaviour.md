---
created: 2026-08-05
updated: 2026-08-05
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: atomic
tags: [dax, calculation-groups, precedence, report-filter, measure]
---

# Report Filter vs Measure: Different CG Application Behaviour

The same calculation group produces **different results** depending on whether it is applied via a report filter (slicer/rows/columns) or via a measure that internally calls a calculation item. This is a critical distinction.

## Expected Behaviour

You might assume both approaches apply calculation items using the same precedence rules.

## Actual Behaviour

| Invocation method | How CG application order is determined |
|-----------------|---------------------------------------|
| Report filter (slicer, rows, columns) | CG precedence governs — the DAX engine chooses the application order |
| Measure that applies a CG internally | The measure **overrides precedence:** it enforces its own application order |

## Why It Happens

When a report filter applies a CG, DAX evaluates the measure and applies all relevant calculation items following precedence.

When a measure internally calls `CALCULATE` with a calculation item, that calculation item is **part of the measure's own expression:** it fires when the measure is evaluated, regardless of external precedence settings.

## Example

```dax
-- CG precedence: Multiplier (200) > Adder (100)

-- Report filter path: Adder and Multiplier both applied via slicers
-- DAX uses precedence → (2 * 10) + 5 = 70

-- Measure path:
Just2Times10 :=
CALCULATE ( [Just2], Multiplier[Factor] = "Mul10" )

-- Query: CALCULATE ( [Just2Times10], Adder[Addend] = "Plus5" )
-- The measure already applied Multiplier internally
-- Adder then applies to [Just2Times10] — not [Just2]
-- Result: (2 * 10) + 5 = 25
```

The measure path yields 25 because the multiplier fires inside the measure before Adder's external application.

## How to Handle It

Be explicit about intent: if you want precedence to govern, use report filters. If you want to enforce a specific order, use a measure that applies the calculation items internally — but document this clearly.

## Related

- [[cg-precedence-application-not-evaluation]]
- [[measure-that-applies-cg-overrides-precedence]]
- [[nested-calculate-does-not-change-cg-application-order]]


See also [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] — Source: [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source]] walks through the two-EVALUATE example that exposes this difference.

See also [[calculation-items-apply-only-to-measure-references]] — See both paths require a measure reference for CG items to activate.