---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: pattern
tags: [dax, performance, calculate, filter, time-intelligence, pattern]
---

# Nested CALCULATE → Direct Filters Pattern

Using nested CALCULATE + ALL() + FILTER() to remove all filters and reapply one — when a simple direct filter expression or time intelligence function would be faster. Found in 23% of slow measures; avg 12.1x speedup after direct filters; 56.5x when using SAMEPERIODLASTYEAR.

## Purpose

Replace the anti-pattern `CALCULATE(agg, FILTER(ALL(table), condition))` with direct filter expressions. The FILTER(ALL()) materializes the entire table before filtering it — far slower than a direct column comparison.

## The Problem Pattern

```dax
-- SLOW: 22.6 seconds
Sales Growth vs PY =
VAR CurrentSales =
    CALCULATE(
        SUM(Sales[Amount]),
        FILTER(
            ALL(Date),
            Date[Year] = YEAR(TODAY())
        )
    )
VAR PriorYearSales =
    CALCULATE(
        SUM(Sales[Amount]),
        FILTER(
            ALL(Date),
            Date[Year] = YEAR(TODAY()) - 1
        )
    )
VAR Growth = DIVIDE(CurrentSales - PriorYearSales, PriorYearSales)
RETURN Growth
```

`FILTER(ALL(Date), ...)` removes all filters from Date, materializes every row of the Date table, then filters to the matching year. Every nested CALCULATE repeats this expensive operation.

## The Fix — Direct Filters

```dax
-- FASTER: 1.8 seconds (12.6x faster)
Sales Growth vs PY =
VAR CurrentYear = YEAR(TODAY())
VAR CurrentSales =
    CALCULATE(SUM(Sales[Amount]), Date[Year] = CurrentYear)
VAR PriorYearSales =
    CALCULATE(SUM(Sales[Amount]), Date[Year] = CurrentYear - 1)
RETURN DIVIDE(CurrentSales - PriorYearSales, PriorYearSales)
```

Changes:
1. Removed `ALL()` — no need to remove filters when setting a specific value
2. Removed `FILTER()` — direct column comparison is faster
3. Cached `YEAR(TODAY())` in a VAR — computed once instead of twice

## The Fix — Time Intelligence Functions

```dax
-- FASTEST: 0.4 seconds (56.5x faster than original)
Sales Growth vs PY =
VAR CurrentSales = SUM(Sales[Amount])
VAR PriorYearSales =
    CALCULATE(
        SUM(Sales[Amount]),
        SAMEPERIODLASTYEAR(Date[Date])
    )
RETURN DIVIDE(CurrentSales - PriorYearSales, PriorYearSales)
```

Time intelligence functions handle the period navigation internally with far less overhead.

## The Decision Tree

```
Is this a time intelligence calculation?
    YES → Use a time intelligence function: DATESYTD, SAMEPERIODLASTYEAR, DATEADD, PARALLELPERIOD
    NO
    Is the CALCULATE filter using FILTER(ALL(...))?
        YES → Replace with direct filter: CALCULATE(agg, Table[Col] = value)
        NO → CALCULATE is likely appropriate as written
```

## Pattern Equivalents

| Slow Pattern | Fast Replacement |
|-------------|----------------|
| `CALCULATE(agg, FILTER(ALL(Date), Date[Year] = N))` | `CALCULATE(agg, Date[Year] = N)` |
| `CALCULATE(agg, FILTER(ALL(Date), Date[Month] = N))` | `CALCULATE(agg, Date[Month] = N)` |
| `CALCULATE(agg, FILTER(ALL(Tbl), Tbl[Col] = X))` | `CALCULATE(agg, Tbl[Col] = X)` |

## Related

- [[calculate]] — CALCULATE reference
- [[calculate]] — CALCULATE deep dive (Dunlop)
- [[dax-totalytd]] — DATESYTD for YTD calculations
- [[sameperiodlastyear]] — SAMEPERIODLASTYEAR for period comparisons
- [[no-calculate-dax-pattern]] — No CALCULATE alternative approach
- [[direct-filter-pattern]] — direct filter arguments in CALCULATE
