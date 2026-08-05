---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: pattern
tags: [dax, performance, iterators, sumx, pattern]
---

# Unnecessary Iterator Pattern

Using SUMX/AVERAGEX/COUNTX/MAXX/MINX to aggregate a single column that already exists — when a simple scalar aggregator (SUM, AVERAGE, COUNT, MIN, MAX) would be faster by orders of magnitude.

## Purpose

Identify and replace iterators that are wrapping a single column reference. These measures work correctly but are orders of magnitude slower than the equivalent scalar aggregator.

## The Problem

```dax
-- SLOW: iterates entire table, evaluates expression per row
Total Revenue =
SUMX(
    Sales,
    Sales[SalesAmount]
)

-- EQUIVALENT but 27x faster:
Total Revenue =
SUM(Sales[SalesAmount])
```

On an 8.2M-row Sales table:
- SUMX version: 8.2 seconds
- SUM version: 0.3 seconds

## When Iterators ARE Needed

Use iterators when the expression computes something that does NOT exist as a stored column:

```dax
-- NEEDED: arithmetic across multiple columns
Gross Profit =
SUMX(Sales, Sales[Revenue] - Sales[Cost])

-- NEEDED: arithmetic requiring division
Weighted Avg =
SUMX(Sales, Sales[Amount] * Sales[Weight]) / SUM(Sales[Weight])

-- NEEDED: referencing another table's column
Product Revenue =
SUMX(Sales, Sales[Quantity] * RELATED(Products[Price]))
```

Note: Pattern 3 (see [[related-in-iterators-performance]]) shows that `RELATED()` in iterators is also slow — best practice is to store the price at transaction time instead.

## Detection

Look for iterator patterns where the iterator body is just a single column reference:

```dax
SUMX(Table, Table[Column])      -- replace with SUM
AVERAGEX(Table, Table[Column])  -- replace with AVERAGE
COUNTX(Table, Table[Column])    -- replace with COUNT
MINX(Table, Table[Column])       -- replace with MIN
MAXX(Table, Table[Column])      -- replace with MAX
```

## Quick Fix Reference

| Slow Pattern | Fast Replacement |
|-------------|-----------------|
| `SUMX(Tbl, Tbl[Col])` | `SUM(Tbl[Col])` |
| `AVERAGEX(Tbl, Tbl[Col])` | `AVERAGE(Tbl[Col])` |
| `COUNTX(Tbl, Tbl[Col])` | `COUNT(Tbl[Col])` |
| `MINX(Tbl, Tbl[Col])` | `MIN(Tbl[Col])` |
| `MAXX(Tbl, Tbl[Col])` | `MAX(Tbl[Col])` |

## Related

- [[iterator-cost-principle]] — why iterators are expensive
- [[x-aggregators-sumx-minx-maxx]] — X aggregator mechanics
- [[sum]] — SUM reference
- [[average]] — AVERAGE vs AVERAGEX
