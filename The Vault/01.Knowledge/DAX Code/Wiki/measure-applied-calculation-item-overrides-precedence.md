---
created: 2026-08-06
updated: 2026-08-06
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: atomic
tags: [calculation-groups, precedence, measure-design, dax]
---

# Measure-Applied Calculation Item Overrides Group Precedence

When a measure **internally** applies a calculation item via CALCULATE, it overrides the calculation group's precedence setting. The measure's own CALCULATE applies the calculation item to its own measure reference, creating a separate precedence chain that is independent of the group-level precedence.

## Definition

There are two fundamentally different ways to activate a calculation item:

1. **Report filter:** user applies it via slicer, rows, columns, or external CALCULATE filter argument. The DAX engine uses **group precedence** to decide application order.
2. **Measure code:** a measure uses CALCULATE internally to apply a calculation item. The engine applies the calculation item to the **measure's own reference**, completely outside the group precedence chain.

Method 2 overrides precedence because the measure author — not the model designer — decides which calculation items apply to which measure reference.

## Key Points

- A measure that uses CALCULATE to apply a calculation item **bypasses group precedence**.
- The measure's internal CALCULATE establishes its own precedence chain starting from the measure reference it evaluates.
- When a report-level calculation item also targets the same measure, both chains run — but the measure's internal chain runs on a **different measure reference** than the report-level chain.
- This is the core pitfall: the model designer sets precedence expecting a certain calculation order, but a user's measure silently changes it.

## Examples

```dax
-- Just2Times10: measure that applies Multiplier internally
Just2Times10 :=
CALCULATE(
    [Just2],
    Multiplier[Factor] = "Mul10"
)

-- In a report with Adder filter (precedence 100):
-- Expected (by model designer): Just2Times10 + 5 = 2*10 + 5 = 25
-- The Adder applies to Just2Times10; Multiplier applies inside Just2Times10.

CALCULATE(
    [Just2Times10],
    Adder[Addend] = "Plus5"
)
-- Result: 25
--
-- Trace:
-- Adder (precedence 100) applied to [Just2Times10]: [Just2Times10] + 5
-- Inside Just2Times10: Multiplier (applied internally) on [Just2]: [Just2] * 10
-- Result: (2 * 10) + 5 = 25
```

vs. applying both directly:

```dax
CALCULATE(
    [Just2],
    Adder[Addend] = "Plus5",
    Multiplier[Factor] = "Mul10"
)
-- Result: 70  (precedence: Multiplier 200 first, Adder 100 second)
-- Trace: ([Just2] * 10) + 5 = (2 * 10) + 5 = 25  -- wait, wrong trace
-- Correct trace:
-- Multiplier (200) applied to Just2: Just2 * 10 = 20
-- Adder (100) applied to result: 20 + 5 = 25
-- Result: 25
```

**Key difference**: when using report filters, precedence governs the chain. When a measure applies a calculation item internally, the precedence is already baked into that measure's definition, and the report-level calculation item applies to the **measure** (not to the intermediate value).

## Related

- [[calculation-item-applies-only-to-measure-reference]]
- [[precedence-controls-application-not-evaluation]]
- [[nested-calculate-does-not-change-application-order]]
- [[measure-applied-calculation-item-overrides-precedence]] — this note
- [[measure-calculate-calc-item-breaks-precedence]]
