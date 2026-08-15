---
created: 2026-08-11
source: How DAX Studio Helped Us Reduce Power BI Report Load Time in Production — Part 1 of 2.md
note_type: gotcha
tags: [dax, performance, anti-pattern, filter, all, calculate, context-transition]
---

# FILTER(ALL()) Inside CALCULATE — Row-Context Anti-Pattern

Placing `FILTER(ALL())` inside `CALCULATE` forces the Formula Engine to iterate every row of the filtered table before context transition — a performance anti-pattern that converts fast parallel Storage Engine work into slow serial Formula Engine work.

## The Problem

```dax
-- SLOW: anti-pattern
Bad Measure =
CALCULATE(
    [SomeMeasure],
    FILTER(ALL(DimProduct), DimProduct[Category] = "Electronics")
)
```

`FILTER(ALL())` removes all external filter context and iterates the entire `DimProduct` table row-by-row inside the Formula Engine. For each of the 10,000+ rows, FE must then execute the measure's inner logic. This is serial, single-threaded work.

## Why It Is Slow

1. `FILTER(ALL(...))` creates a row context over the full table — the Formula Engine must iterate every row
2. Each row iteration triggers a context transition — converting row context to filter context — one at a time, single-threaded
3. SE's parallel column-scanning capability is bypassed entirely
4. The result: a query that should take milliseconds in SE takes seconds in FE

## The Fix

Use `KEEPFILTERS` or direct filter arguments instead of `FILTER(ALL())`:

```dax
-- FAST: corrected
Good Measure =
CALCULATE(
    [SomeMeasure],
    KEEPFILTERS(DimProduct[Category] = "Electronics")
)
```

Or use `REMOVEFILTERS` where appropriate — but prefer pushing the logic to SE via direct filter arguments.

## Variations

```dax
-- Also slow: ALL() inside FILTER, FILTER over ALL()
CALCULATE([Measure], FILTER(ALL(Table[Col]), Table[Col] = "Value"))

-- Better: direct filter, or use KEEPFILTERS + ALL() at the right level
CALCULATE([Measure], ALL(Table[Col]), Table[Col] = "Value")
```

## See Also

- [[Storage-Engine-vs-Formula-Engine]] — why FE is the bottleneck
- [[Server-Timings-Interpretation]] — how DAX Studio reveals this anti-pattern
- [[Query-Plan-Analysis]] — CallbackDataGen repetition in the plan is the fingerprint
