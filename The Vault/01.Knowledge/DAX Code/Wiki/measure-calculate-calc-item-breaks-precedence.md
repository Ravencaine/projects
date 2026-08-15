---
created: 2026-08-06
updated: 2026-08-06
source: Avoiding Pitfalls in Calculation Groups Precedence.md
note_type: gotcha
tags: [calculation-groups, precedence, gotcha, measure-design, dax]
---

# Measure + CALCULATE + Calculation Group Breaks Your Precedence

You carefully set calculation group precedence in your model, but a user creates a custom measure using CALCULATE with a calculation item — and your precedence is silently overridden. The result is wrong, and there is no error or warning.

## Expected Behaviour

With Adder (precedence 100) and Multiplier (precedence 200), applying both via report filters produces a consistent result following group precedence: multiplication first, then addition.

## Actual Behaviour

If a user writes a measure that uses CALCULATE to apply a calculation item internally, the engine applies that calculation item to the **measure reference inside CALCULATE:** not to the user's CALCULATE. This changes which measure reference each calculation item touches, and the precedence chain runs on the wrong reference.

## Why It Happens

Calculation items apply to the **measure reference they encounter**. When a measure code contains `CALCULATE([SomeMeasure], CalcGroup[Item]="Value")`, the calculation item is applied to `SomeMeasure` — inside the CALCULATE — not to the measure that the user is evaluating in the report. The group precedence for the outer measure reference is bypassed for that calculation item.

The result is two independent precedence chains:
- The report-level calculation items apply to the **user's measure reference** (the one they are evaluating in the visual).
- The measure's internal calculation items apply to the **internal measure reference** (the one inside its CALCULATE).

The two chains run on different measure references and are not merged by precedence.

## How to Handle It

- **Design defensively**: avoid using CALCULATE + calculation item inside measures when you have multiple calculation groups with precedence dependencies. If a measure needs to apply a calculation item, apply all of them at the same level — don't rely on group precedence inside a measure.
- **Document the risk**: warn users that creating measures using CALCULATE + calculation group overrides the model's precedence design.
- **Use format strings and scoped assignments** instead of nested precedence chains where possible.
- **Test with both patterns**: compare report-level calculation item filters vs. measure-internal application to verify which precedence chain is actually running.

## Related Gotchas

- [[nested-calculate-does-not-change-application-order]]
- [[measure-applied-calculation-item-overrides-precedence]]
- [[auto-exist-and-all-gotchas]]

- See also [[calculation-item-applies-only-to-measure-reference]].