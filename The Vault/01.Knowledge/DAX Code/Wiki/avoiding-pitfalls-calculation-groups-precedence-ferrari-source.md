---
created: 2026-08-05
updated: 2026-08-05
source: Avoiding Pitfalls in Calculation Groups Precedence.md
source_url: https://www.sqlbi.com/articles/avoiding-pitfalls-in-calculation-groups-precedence/
note_type: source
tags: [dax, calculation-groups, sqlbi, alberto-ferrari, precedence]
---

# Avoiding Pitfalls in Calculation Groups Precedence (Ferrari)

> **Type:** article
> **Author:** Alberto Ferrari (SQLBI)
> **Published:** 2020-08-17
> **URL:** https://www.sqlbi.com/articles/avoiding-pitfalls-in-calculation-groups-precedence/
> **Routed to:** DAX Code

## Summary

Explains why calculation group (CG) precedence does not control evaluation order — it controls *application* order. Demonstrates through four diagnostic puzzles that a calculation item only activates on a measure reference, and that defining a measure which applies a CG overrides the precedence mechanism entirely.

## Key Claims

- CG precedence defines the order of *application* of calculation items, not their order of *evaluation*
- A calculation item applies only to a **measure reference:** if the expression contains no measure, the item has no target and is silently skipped
- Nesting `CALCULATE` does not change application order; CG precedence always governs
- A measure that applies a CG internally **overrides precedence:** it enforces its own application order
- Using a report filter (slicer/rows/columns) with a CG lets the engine choose application order by precedence; using a measure enforces order explicitly
- Multiple CGs in a model compound complexity significantly — understand precedence deeply before deploying

## Notable Details

- Example CG setup: `Adder` (precedence 100, `SELECTEDMEASURE()+5`) and `Multiplier` (precedence 200, `SELECTEDMEASURE()*10`) — precedence 200 runs first
- Puzzle results: no measure → no application (result unchanged); precedence governs application chain → `(2*10)+5=25` vs `((2+5)*10)=70` depending on where the reference lands; measure that calls CG → CG inside measure fires first regardless of precedence
- Four warm-up puzzles before the core explanation; each walks through a different code shape

## Extracted Notes

Links to notes derived from this source:

- [[calculation-items-apply-only-to-measure-references]] — atomic — CG items only activate on measure references
- [[cg-precedence-application-not-evaluation]] — atomic — precedence = application order, not evaluation order
- [[report-filter-vs-measure-cg-behaviour]] — atomic — different CG application behaviour depending on how it's invoked
- [[nested-calculate-does-not-change-cg-application-order]] — gotcha — nested CALCULATE does not change CG application order
- [[measure-that-applies-cg-overrides-precedence]] — gotcha — defining a measure that applies a CG overrides the precedence mechanism

## Metadata

| Field | Value |
|-------|-------|
| Source file | Avoiding Pitfalls in Calculation Groups Precedence.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~161 |
