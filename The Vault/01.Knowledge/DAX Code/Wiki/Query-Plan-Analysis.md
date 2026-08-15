---
created: 2026-08-11
source: How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2.md
note_type: pattern
tags: [dax, performance, dax-studio, query-plan, diagnostics]
---

# Query Plan Analysis

Reading the Query Plan panel in DAX Studio to identify structural problems in a DAX query.

## What the Query Plan Shows

Two versions of the plan the engine builds to answer your query:

| Plan | What it shows |
|------|--------------|
| **Logical Query Plan** | Abstract sequence of operations: filter → aggregate → join etc. |
| **Physical Query Plan** | Actual operators the engine executed to carry out the logical plan |

## How to Read It

You do not need to understand every line. The primary signal to watch for is **repetition** — operations that appear far more times than expected for the shape of the data.

Repetition is the fingerprint of a DAX anti-pattern that is re-scanning the same data over and over instead of computing it once.

## Key Interpretation Rule

> A well-written DAX measure asks SE to do as much heavy lifting as possible — grouping, filtering, summing — and only hands FE a small, already-organised set of results to finish off.

If the Query Plan shows the same operation repeated N times (where N corresponds to a row count in your data), the measure is forcing re-computation per row — an FE-heavy anti-pattern.

## Common Repetition Fingerprints

| Operation repeated | Likely cause |
|-------------------|-------------|
| Same column scan repeated N times | `FILTER(ALL())` inside CALCULATE — SE rescanned per row |
| CrossJoin repeated | Cartesian product in an iterator over a large table |
| CallbackDataGen repeated | FE requesting data from SE for every row — the performance killer |

## Related

- [[DAX-Studio-Debug-Workflow]] — full workflow from query capture to analysis
- [[Storage-Engine-vs-Formula-Engine]] — why repetition matters (SE vs FE)
- [[FILTER-ALL-Inside-CALCULATE-AntiPattern]] — the classic repetition pattern
