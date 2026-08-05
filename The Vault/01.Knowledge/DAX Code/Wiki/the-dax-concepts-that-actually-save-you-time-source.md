---
created: 2026-07-27
updated: 2026-08-02
source: "The DAX Concepts that Actually Save You Time in Power BI"
source_url: "https://medium.com/@jjr8888/the-dax-concepts-that-actually-save-you-time-in-power-bi-f193466f5b8f"
note_type: source
tags: [dax, power-bi, fundamentals, context, calculate]
---

# The DAX Concepts that Actually Save You Time in Power BI

A Medium article by Daniel Olatunji targeting analysts who have learned DAX syntax but don't yet "think in DAX" — the shift from memorising functions to understanding what filters are active and when.

> **Type:** article
> **Author:** Daniel Olatunji
> **Published:** 2026-07-27
> **URL:** https://medium.com/@jjr8888/the-dax-concepts-that-actually-save-you-time-in-power-bi-f193466f5b8f
> **Routed to:** DAX Code

## Summary

The article argues that DAX confusion stems from not understanding context — filter context and row context — rather than from syntax difficulty. Once a developer grasps that CALCULATE modifies filter context and that variables (VAR) make formulas readable and performant, the language starts to feel like a small toolkit of composable patterns rather than an overwhelming list of 250+ functions. The core eight functions the author reaches for on every project: CALCULATE, DIVIDE, SUMX/AVERAGEX, ALL/ALLSELECTED, RELATED, SWITCH, SAMEPERIODLASTYEAR/DATESYTD, and RANKX.

## Key Claims

- DAX is a formula language built for one job: pulling numbers out of a data model based on filters
- Every "weird" DAX behaviour comes back to filter context
- CALCULATE is the one function that runs the whole show — context transition is its key superpower
- VAR makes formulas readable and avoids repeated evaluation
- BLANK() and 0 are not equivalent in aggregations
- Time intelligence functions require a marked, continuous date table — skip this and nothing downstream behaves correctly
- Eight functions cover most real Power BI work

## Notable Details

- The 400MB → 60MB file anecdote: swapping calculated columns for measures dropped model size and refresh time dramatically
- Practical DAX priorities: understand what is filtered and when, then pick the right function

## Extracted Notes

Links to notes derived from this source:

- [[filter-context-vs-row-context]] — `atomic` — core DAX evaluation contexts
- [[context-transition-with-calculate]] — `atomic` — CALCULATE inside iterators
- [[calculate]] — extended with context transition detail
- [[blank-vs-zero-in-averages]] — `gotcha` — BLANK() vs 0 in aggregations
- [[divide-function-vs-divide-operator]] — `gotcha` — extended with BLANK handling
- [[use-variables-in-dax-formulas]] — `pattern` — VAR pattern (already in KB)

## Metadata

| Field | Value |
|-------|-------|
| Source file | The DAX concepts that actually save you time in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,050 |
