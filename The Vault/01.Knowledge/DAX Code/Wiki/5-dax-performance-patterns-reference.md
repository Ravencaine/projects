---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: reference
tags: [dax, performance, reference, benchmarks]
---

# The 5 DAX Performance Patterns — Quick Reference

Five anti-patterns responsible for 78% of slow DAX measures, found in a study of 5,247 measures across 89 production reports. Based on Gulab Chand Tejwani's empirical analysis (2026).

## The 5 Patterns at a Glance

| # | Pattern | Prevalence | Avg Speedup | Fix |
|---|---------|-----------|------------|-----|
| 1 | Unnecessary iterators | 41% of slow | 19.5x | Replace `SUMX(T, T[Col])` with `SUM(T[Col])` |
| 2 | Calculated columns everywhere | 28% of slow | 67% less refresh time | Move aggregations to measures |
| 3 | RELATED() in iterators | 19% of slow | 14.9x | Store related value at transaction time |
| 4 | Nested CALCULATE + FILTER(ALL()) | 23% of slow | 12.1x | Direct filters; or time intelligence functions |
| 5 | ALL() when REMOVEFILTERS() works | 31% of slow | 11.6x | Replace `ALL(Tbl)` with `REMOVEFILTERS(Tbl)` |

**Aggregate impact:** 78% of slow measures share these 5 patterns. Average: 14.2x faster after fixing. Worst case: 18.3s → 0.3s (61x).

## Pattern 1: Unnecessary Iterators

```dax
-- SLOW: SUMX wrapping a column reference
Bad = SUMX(Sales, Sales[Revenue])

-- FAST: use the scalar aggregator
Good = SUM(Sales[Revenue])
```

Also: `AVERAGEX`, `COUNTX`, `MINX`, `MAXX` when used on a single column.

## Pattern 2: Calculated Columns for Aggregation

```
Decision: Will this be used as a FILTER/SLICER/AXIS?
  YES → calculated column OK
  NO  → use a measure
```

12 calculated columns in an 8.2M-row table: 890 MB memory, 22 extra minutes of refresh.

## Pattern 3: RELATED() in Iterators

```dax
-- SLOW: 8,204 SE queries on 8.2M rows
Bad = SUMX(Sales, Sales[Qty] * RELATED(Products[Price]))

-- FAST: use a stored column
Good = SUMX(Sales, Sales[Qty] * Sales[UnitPrice])
```

## Pattern 4: CALCULATE + FILTER(ALL())

```dax
-- SLOW: materializes entire table before filtering
Bad = CALCULATE(SUM(Amt), FILTER(ALL(Date), Date[Year] = 2024))

-- FASTER: direct filter
Better = CALCULATE(SUM(Amt), Date[Year] = 2024)

-- FASTEST: time intelligence function
Best = CALCULATE(SUM(Amt), SAMEPERIODLASTYEAR(Date[Date]))
```

## Pattern 5: ALL() vs REMOVEFILTERS()

```dax
-- SLOW: ALL materializes the table
Slow = CALCULATE(SUM(Amt), ALL(Geography))

-- FAST: REMOVEFILTERS only removes filters
Fast = CALCULATE(SUM(Amt), REMOVEFILTERS(Geography))

-- SLOWEST: multiple ALL() calls
Slowest = CALCULATE(SUM(Amt), ALL(Date), ALL(Products), ALL(Geography))

-- FAST: REMOVEFILTERS with no args removes all filters
Fastest = CALCULATE(SUM(Amt), REMOVEFILTERS())
```

## Audit Framework (Quick)

1. Performance Analyzer → find measures >2s
2. Check each for the 5 patterns above
3. Rewrite → test in DAX Studio → deploy

## Related

- [[dax-measure-audit-workflow]] — full 3-step audit workflow
- [[unnecessary-iterator-pattern]] — Pattern 1 deep dive
- [[calculated-columns-vs-measures-performance]] — Pattern 2 deep dive
- [[related-in-iterators-performance]] — Pattern 3 deep dive
- [[nested-calculate-direct-filters-pattern]] — Pattern 4 deep dive
- [[all-vs-removefilters-performance]] — Pattern 5 deep dive
- [[tejwani-5000-dax-measures-performance-source]] — source note
