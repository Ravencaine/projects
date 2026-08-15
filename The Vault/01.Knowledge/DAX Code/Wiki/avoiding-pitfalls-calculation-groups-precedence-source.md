---
created: 2026-08-06
updated: 2026-08-06
source: Avoiding Pitfalls in Calculation Groups Precedence.md
source_url: https://www.sqlbi.com/articles/avoiding-pitfalls-in-calculation-groups-precedence/
note_type: source
tags: [calculation-groups, precedence, dax, power-bi, tabular]
---

# Avoiding Pitfalls in Calculation Groups Precedence

SQLBI article by Alberto Ferrari — explains how calculation group precedence interacts with CALCULATE and context transition, and why measures that apply calculation items internally can silently override precedence.

> **Type:** article
> **Author:** Alberto Ferrari
> **Published:** 2020-08-17
> **URL:** https://www.sqlbi.com/articles/avoiding-pitfalls-in-calculation-groups-precedence/
> **Routed to:** DAX Code

## Summary

Calculation group precedence determines the order in which calculation items are **applied** to measure references — not the order in which they are **evaluated**. Precedence only governs which measure reference a calculation item touches. A measure that internally applies a calculation item via CALCULATE overrides group precedence entirely, because the calculation item is applied to a different measure reference inside the CALCULATE.

## Key Claims

- A calculation item is applied only to a **measure reference:** not to a raw constant value inside CALCULATE.
- Precedence controls the order of **application** of calculation items, not evaluation order.
- Nesting CALCULATE functions does not change which calculation items are applied to which measure reference.
- A measure that applies a calculation item internally **overrides group precedence:** the user's measure wins over the model designer's precedence settings.
- Users who create their own measures using CALCULATE + calculation item can silently break well-engineered calculation group designs.

- See also [[dax-context]].
- See also [[context-transition-with-calculate]].
## Notable Details

- The `Adder` and `Multiplier` example: Multiplier precedence 200 (applied first), Adder precedence 100 (applied second).
- `Just2 := 2` — a measure returning a constant, used to demonstrate that no calculation items apply when CALCULATE receives no measure reference.
- `Just2Times10` measure: `CALCULATE([Just2], Multiplier[Factor]="Mul10")` — applies a calculation item directly, which changes the effective precedence.
- Four warm-up puzzles train intuition before the core principle.
- Nine related SQLBI articles in the Calculation Groups series.

## Extracted Notes

Links to notes derived from this source:

- [[calculation-item-applies-only-to-measure-reference]] — `atomic` — calculation items require a measure reference to attach
- [[precedence-controls-application-not-evaluation]] — `atomic` — precedence is about which measure a calculation item touches, not when
- [[nested-calculate-does-not-change-application-order]] — `atomic` — nesting CALCULATE has no effect on calculation item application
- [[measure-applied-calculation-item-overrides-precedence]] — `atomic` — a measure that applies a calc item internally bypasses group precedence
- [[measure-calculate-calc-item-breaks-precedence]] — `gotcha` — user-defined measures using CALCULATE + calc item override precedence silently
- [[just2times10-measure-overrides-precedence]] — `pattern` — the Just2Times10 measure demonstrating precedence override
- [[sqlbi-calculation-groups-article-map]] — `reference` — full SQLBI article series map

## Metadata

| Field | Value |
|-------|-------|
| Source file | Avoiding Pitfalls in Calculation Groups Precedence.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~760 |
