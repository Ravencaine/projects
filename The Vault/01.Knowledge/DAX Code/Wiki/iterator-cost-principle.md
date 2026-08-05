---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
note_type: atomic
tags: [dax, iterators, performance, principle]
---

# Iterator Cost Principle

Iterators (SUMX, AVERAGEX, MAXX, MINX, COUNTX, etc.) are powerful but carry row-by-row evaluation cost. Use them only when computing something that does not already exist in the table.

## Definition

An iterator scans a table row by row, evaluating its expression at each row before accumulating a result. This is expensive compared to a simple column aggregation. Every scalar aggregation (SUM, AVERAGE, COUNT, MIN, MAX) has an X-variant for a reason — the X versions are for when the scalar aggregation is insufficient.

## Key Points

- Iterators evaluate their second argument once per row in the first argument table
- On large tables (millions of rows), this cost compounds significantly
- A simple SUM of a column is 1 Storage Engine query; the equivalent SUMX is a full table scan through the Formula Engine
- The X in SUMX is not optional — it changes the evaluation model fundamentally
- Iterators are correct and necessary when computing a per-row expression that does NOT exist as a column: `Sales[Qty] * Sales[Price]` (two columns multiplied), `Revenue - Cost` (derived value), `AVERAGE(Budget)` where Budget is a table

## Examples

```dax
-- ITERATOR NEEDED: computing something not stored
Gross Profit =
SUMX(
    Sales,
    Sales[Revenue] - Sales[Cost]
)

-- ITERATOR UNNECESSARY: summing a column that already exists
Bad = SUMX(Sales, Sales[Revenue])
Good = SUM(Sales[Revenue])

-- ITERATOR UNNECESSARY: averaging a column
Bad = AVERAGEX(Sales, Sales[DaysToShip])
Good = AVERAGE(Sales[DaysToShip])

-- ITERATOR NEEDED: per-row arithmetic
Weighted Avg =
SUMX(Sales, Sales[Amount] * Sales[Weight]) / SUM(Sales[Weight])
```

## Related

- [[unnecessary-iterator-pattern]] — common anti-pattern and fixes
- [[x-aggregators-sumx-minx-maxx]] — X aggregator mechanics
- [[sumx]] — SUMX reference
- [[average]] — AVERAGE vs AVERAGEX
