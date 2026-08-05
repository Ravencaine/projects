---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: pattern
tags: [dax, performance, all, removefilters, pattern]
---

# ALL vs REMOVEFILTERS Performance Pattern

Using `ALL()` when only filter removal is needed causes the table to be materialized unnecessarily. `REMOVEFILTERS()` removes filters without returning the table — up to 10.7x faster. Found in 31% of slow measures.

## Purpose

Distinguish between ALL() and REMOVEFILTERS() and use each in the right context. ALL() both removes filters AND returns the full table; REMOVEFILTERS() only removes filters. Use ALL() only when the returned table is needed; otherwise prefer REMOVEFILTERS().

## The Problem Pattern

```dax
-- SLOW: 3.2 seconds
Total Revenue All Regions =
CALCULATE(
    SUM(Sales[Revenue]),
    ALL(Geography)
)
```

On a Geography table with 850 rows, `ALL(Geography)` materializes all 850 rows before the calculation proceeds.

## The Fix

```dax
-- FAST: 0.3 seconds (10.7x faster)
Total Revenue All Regions =
CALCULATE(
    SUM(Sales[Revenue]),
    REMOVEFILTERS(Geography)
)
```

`REMOVEFILTERS(Geography)` removes filters from the Geography columns without materializing the table.

## The Rule

```
Do you need the table returned (for COUNTROWS, as an iterator argument, etc.)?
    YES → ALL()   (you need the table)
    NO  → REMOVEFILTERS()  (you only need to clear filters)
```

## When to Use ALL()

```dax
-- Need the table returned for a count
Number of Products = COUNTROWS(ALL(Products))

-- Need the table as an iterator argument
Product Rank =
RANKX(ALL(Products), [Total Sales])

-- Need the table for SUMMARIZECOLUMNS or similar
```

## When to Use REMOVEFILTERS()

```dax
-- Only removing filters from a column
Total Sales All Regions =
CALCULATE(SUM(Sales[Amount]), REMOVEFILTERS(Geography))

-- Removing all filters from entire model
% of Grand Total =
DIVIDE(
    SUM(Sales[Amount]),
    CALCULATE(SUM(Sales[Amount]), REMOVEFILTERS())
)

-- Removing filters from specific columns only
Total Sales This Year =
CALCULATE(SUM(Sales[Amount]), REMOVEFILTERS(Date[Year]))
```

## Special Case: REMOVEFILTERS() with No Arguments

`REMOVEFILTERS()` with no arguments removes filters from all tables in the model — equivalent to ALL() on every table, but without materializing anything:

```dax
-- SLOW: 28.3 seconds
% of Total Revenue =
DIVIDE(
    SUM(Sales[Revenue]),
    CALCULATE(
        SUM(Sales[Revenue]),
        ALL(Date), ALL(Products), ALL(Geography)
    )
)

-- FAST: 1.7 seconds (16.6x faster)
% of Total Revenue =
DIVIDE(
    SUM(Sales[Revenue]),
    CALCULATE(SUM(Sales[Revenue]), REMOVEFILTERS())
)
```

## Related

- [[all]] — ALL reference
- [[removefilters]] — REMOVEFILTERS reference
- [[5-dax-performance-patterns-reference]] — overview of all 5 patterns
