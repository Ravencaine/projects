---
created: 2026-07-30
updated: 2026-08-02
source: Dynamic Ranking in DAX How I Built a Top 5 Dashboard That Actually Worked.md
note_type: pattern
tags: [dax, ranking, performance, rankx, var, pattern]
---

# RANKX with VAR Performance Pattern

Cache intermediate results in RANKX using VAR to avoid repeated evaluation of the ranking expression across all rows.

## Purpose

RANKX evaluates its second argument (the expression being ranked) once per row in the ranking set. When that expression is expensive — involving complex filters or aggregations — this causes severe performance degradation. VAR captures the result once and reuses it, yielding significant speedups (reported ~30% in production).

## Problem

Naive RANKX re-evaluates the ranked expression for every comparison row:

```dax
-- SLOW: [Total Sales] evaluated once per customer row × once per comparison row
Customer Rank Slow =
RANKX (
    ALL ( Customers[CustomerName] ),
    [Total Sales],        -- complex measure evaluated repeatedly
    ,
    DESC
)
```

## Solution

```dax
Customer Rank Optimized =
VAR RankSet = ALL ( Customers[CustomerName] )
VAR SalesValue = [Total Sales]    -- evaluated ONCE
RETURN
    RANKX (
        RankSet,
        SalesValue,               -- reuses cached value
        ,
        DESC
    )
```

The `SalesValue` VAR captures the current-row measure result once. RANKX then uses it for all internal comparisons without re-evaluating.

## When This Matters Most

- Measure includes `CALCULATE` with multiple filter arguments
- Cross-fact navigation (filtering across multiple fact tables)
- Large dimension tables (100k+ rows in the ranking set)
- RANKX inside a visual that shows many rows simultaneously

## Structural Variation

For multi-column ranking sets:

```dax
Rank By Multiple Columns =
VAR RankSet = ALL ( Customers[CustomerName], Customers[Region] )
VAR Score = [Total Sales] + [Total Profit]
RETURN
    RANKX (
        RankSet,
        Score,
        ,
        DESC
    )
```

## Related

- [[dynamic-top-n-ranking-pattern]] — context for the ranking pattern
- [[dax-var]] — VAR and RETURN mechanics
- [[dax-performance-optimization-techniques]] — broader DAX performance guide
