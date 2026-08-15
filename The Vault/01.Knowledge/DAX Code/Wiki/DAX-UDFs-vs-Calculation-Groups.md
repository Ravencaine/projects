---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: atomic
tags: [dax, udf, calculation-groups, power-bi]
---

# DAX UDFs vs Calculation Groups

UDFs and calculation groups solve **different problems:** they are complementary, not interchangeable.

## The Distinction

| | UDF | Calculation Group |
|--|-----|-----------------|
| **What it changes** | *How* logic is computed | *Which* measure is selected |
| **Trigger** | Called explicitly at the call site | Slicer selection |
| **Scope** | Per-expression | Per-visual or per-page |
| **Parameters** | Typed, explicit, developer-controlled | Implicit via selected item |

## Calculation Group Mental Model

A calculation group has N items (e.g., "Actual", "Budget", "Forecast"). Selecting one item in a slicer swaps the active measure — the entire visual recalculates with the selected calculation item applied as a filter.

## UDF Mental Model

A UDF defines a piece of logic once with typed parameters. Every call site passes concrete values or expressions. The UDF body runs with the caller's context.

## When to Use Which

- **Use a calculation group** when you want users to toggle between alternative definitions of the same KPI via a slicer (e.g., switch between MTD/YTD/PTD)
- **Use a UDF** when you have repeated logic that should be computed the same way everywhere (e.g., safe division, ABC banding, currency conversion)

## They Compose

A mature semantic model uses both: calculation groups for user-facing measure selection, UDFs inside those measures for reusable computation logic.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source note
- [[dwp.SafeDivide]] — example UDF
