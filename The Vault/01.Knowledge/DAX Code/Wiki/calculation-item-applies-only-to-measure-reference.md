---
created: 2026-08-06
updated: 2026-08-06
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: atomic
tags: [calculation-groups, measure-reference, dax]
---

# Calculation Items Apply Only to Measure References

A calculation item is applied only when it encounters a **measure reference** in the evaluation chain. If CALCULATE contains only a constant value with no measure reference, no calculation item is applied.

## Definition

Calculation items are DAX mechanisms that intercept and transform measure references. They attach to measures — not to arbitrary expressions. When a CALCULATE expression evaluates a measure by name (`[MeasureName]`), the engine applies the active calculation items to that measure reference. When CALCULATE receives only a literal constant or a non-measure expression, the calculation item has no measure to intercept — it is silently skipped.

## Key Points

- A calculation item requires a **measure reference** to be applied.
- `CALCULATE(2, Adder[Addend]="Plus5")` returns **2:** the constant has no measure reference, so no calculation item is applied.
- `CALCULATE([Just2], Adder[Addend]="Plus5")` returns **7:** `[Just2]` is the measure reference that the calculation item intercepts and transforms.
- Any expression that is not a direct measure reference — including nested CALCULATE calls — may have its own measure reference that is independent of the outer one.

## Examples

```dax
-- No measure reference: calculation item not applied
CALCULATE(
    2,                      -- constant, not a measure
    Adder[Addend] = "Plus5"
)
-- Result: 2 (not 7)

-- Measure reference present: calculation item applied
CALCULATE(
    [Just2],                -- measure reference
    Adder[Addend] = "Plus5"
)
-- Result: 2 + 5 = 7
```

## Related

- [[calculation-item-applies-only-to-measure-reference]] — this note
- [[precedence-controls-application-not-evaluation]]
- [[nested-calculate-does-not-change-application-order]]
- [[measure-applied-calculation-item-overrides-precedence]]
- [[measure-calculate-calc-item-breaks-precedence]]
