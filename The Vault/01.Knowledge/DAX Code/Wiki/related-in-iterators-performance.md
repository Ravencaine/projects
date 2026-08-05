---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: pattern
tags: [dax, performance, related, iterators, pattern]
---

# RELATED in Iterators Performance Pattern

Using `RELATED()` inside an iterator (SUMX, AVERAGEX, etc.) causes one Storage Engine query per row — effectively a cross-join that destroys performance. Found in 19% of slow measures; avg 14.9x speedup after fix.

## Purpose

Avoid `RELATED()` inside iterators. The function triggers context transition for every iterated row, multiplying the number of Storage Engine queries by the row count. Fix by storing the related value at transaction time.

## The Problem

```dax
-- SLOW: 8,204 Storage Engine queries on an 8.2M-row table
Product Revenue =
SUMX(
    Sales,
    Sales[Quantity] * RELATED(Products[Price])
)
```

On an 8.2M-row Sales table:
- Time: 14.2 seconds
- Storage Engine queries: 8,204 (one per row!)

## Why It Happens

`RELATED()` requires an active row context to traverse the relationship. Inside an iterator, it creates context transition for each row — forcing the Storage Engine to look up the related value for every single row.

## The Fix

**Best practice: Store the value at transaction time in the fact table.**

If `Price` (or `UnitPrice`) is already in the Sales table:

```dax
-- FAST: 1 Storage Engine query
Product Revenue =
SUMX(
    Sales,
    Sales[Quantity] * Sales[UnitPrice]
)
```

On the same 8.2M-row table:
- Time: 0.9 seconds
- Storage Engine queries: 1

**15.8x faster.**

## When RELATED() Is Fine

1. **In calculated columns**: evaluated once at refresh, not at query time:
```dax
-- Fine: calculated column
Product Category = RELATED(Products[Category])
```

2. **Outside iterators in measures**: when there's no row iteration:
```dax
-- Acceptable: no iteration
Total Revenue =
SUMX(
    FILTER(Sales, Sales[Quantity] > 10),
    Sales[Revenue] * RELATED(Products[DiscountRate])
)
-- Still slow if Sales is large — prefer storing at transaction time
```

## Special Case: Historical vs. Current Values

The original article notes that `RELATED()` always returns the **current** value of the related column, not the historical value at transaction time. If lead time varies by season or supplier capacity, `RELATED()` gives the wrong answer even if it were fast.

Fix: add an `ActualLeadTime` column to the Orders table at source.

## Related

- [[related]] — RELATED function mechanics
- related-in-iterators-performance — cross-reference (same note, different perspective)
- [[iterator-cost-principle]] — why iterators are expensive
- [[related]] — RELATED reference
