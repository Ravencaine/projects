---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Repeating Yourself in DAX - The Power of Variables (VAR).md"
note_type: atomic
tags: [dax, var, performance, optimization, beginner, intermediate]
---

# VAR Performance Benefit

Every time DAX evaluates an expression, it runs the full calculation. When the same expression appears multiple times in a measure, each occurrence is evaluated separately — unless `VAR` stores and reuses the result.

## The Problem: Repeated Expression Evaluation

Without VAR, repeated logic is evaluated each time it appears:

```dax
YoY Growth % =
DIVIDE (
    SUM ( Sales[Revenue] ) -                                        -- evaluated once
    CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) ),  -- evaluated once
    CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )    -- evaluated AGAIN
)
```

`CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR (...) )` is computed **twice**: once for the numerator and once for the denominator.

## The Solution: VAR Evaluates Once

```dax
YoY Growth % =
VAR Revenue = SUM ( Sales[Revenue] )
VAR LY = CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
RETURN
DIVIDE ( Revenue - LY, LY )
```

Both `SUM(Sales[Revenue])` and the `CALCULATE(...SAMEPERIODLASTYEAR...)` expression are now evaluated **once each** and stored in their respective variables.

## Performance Impact

The more complex the repeated expression, the greater the benefit:

| Repeated Expression | Relative Cost |
|---------------------|---------------|
| `SUM ( FactTable[Column] )` | Low–Medium |
| `CALCULATE ( SUM(...), FILTER(...) )` | Medium–High |
| `SAMEPERIODLASTYEAR / PARALLELPERIOD` | Medium |
| Nested `CALCULATE` with multiple filters | High |

The source article reported ~30% query speedup (2.8s → 1.9s) when refactoring copy-paste logic to VAR-based measures in a 10M-row model.

## When Performance Benefit Is Largest

- Large fact tables (millions of rows)
- Repeated `CALCULATE` calls with `SAMEPERIODLASTYEAR`, `FILTER`, or `ALL` arguments
- Multiple measures on the same visual all using the same base calculations
- Time intelligence functions (evaluated per-row in the filter context)

## When Performance Benefit Is Negligible

- Very small fact tables (< 100K rows)
- Simple aggregations with no filter context (e.g., plain `SUM`)
- Single-use expressions (no repetition within the measure)

## DAX Studio to Measure

Use DAX Studio's **Server Timings** pane to compare query times before and after refactoring to VAR.

## Related

- [[var-syntax-and-pattern]] — VAR syntax and basic usage
- [[dax-optimization-best-practices]] — broader DAX performance optimisation
- [[measure-branching-performance]] — similar caching benefit from measure branching
