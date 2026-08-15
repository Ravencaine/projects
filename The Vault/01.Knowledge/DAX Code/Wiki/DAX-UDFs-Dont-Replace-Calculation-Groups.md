---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: gotcha
tags: [dax, udf, calculation-groups, power-bi]
---

# DAX UDFs Don't Replace Calculation Groups

UDFs and calculation groups are **complementary:** they solve different problems. Reaching for one when you need the other creates awkward, over-engineered solutions.

## What Calculation Groups Do

A calculation group lets users switch which measure is active via a slicer. Selecting "YTD" vs "MTD" in a slicer filters the visual to run the YTD measure instead of the MTD measure. The calculation item acts as a filter on which measure is evaluated — it changes *which* measure, not *how* any single measure is computed.

## What UDFs Do

A UDF packages a piece of logic with typed parameters. Calling `dwp.SafeDivide([Sales], [Cost])` runs the same division logic everywhere. The function changes *how* the result is computed — it doesn't change which measure is active.

## The Trap: Trying to Make a UDF Do Calculation Group Work

If you find yourself writing a UDF that takes a "measure selector" parameter and wraps it in SWITCH/CALCULATE to emulate a calculation group — stop. You need a calculation group, not a UDF.

## The Trap: Trying to Make a Calculation Group Do UDF Work

If you find yourself creating 15 calculation items that each contain slightly different arithmetic — stop. Extract the arithmetic into UDFs and use the calculation group for what it was designed for: measure selection.

## The Right Architecture

Mature models use both:
- **Calculation groups** for user-facing measure toggling (MTD/YTD/PTD, Actual/Budget/Forecast)
- **UDFs** inside those measures for reusable computation logic (safe division, ABC banding, currency conversion)

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[DAX-UDFs-vs-Calculation-Groups]] — atomic: full distinction table
