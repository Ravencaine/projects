---
created: 2026-07-27
updated: 2026-08-02
source: "I Analyzed 5,000 DAX Measures: The 5 Patterns That Kill Performance"
note_type: pattern
tags: [dax, performance, iterators, sumx, fact-table, pre-filter]
---

# Iterator Performance Pattern

Iterators (SUMX, AVERAGEX, etc.) process one row at a time, so their cost grows linearly with the number of rows they touch. On large fact tables (millions of rows), an unfiltered iterator can become the dominant performance bottleneck.

## The Problem

```dax
-- Slow on large fact tables: iterates all rows unconditionally
Total Shipping Cost =
SUMX (
    Sales,                              -- millions of rows, no pre-filter
    Sales[Quantity] * Sales[ShippingRate]
)
```

## The Fix: Pre-Filter the Table

```dax
-- Fast: iterate only the filtered subset
Total Shipping Cost =
SUMX (
    FILTER ( Sales, Sales[Quantity] > 0 ),  -- pre-filter reduces row count
    Sales[Quantity] * Sales[ShippingRate]
)
```

## Better Fix: Aggregate First

```dax
-- Best: avoid the iterator entirely where possible
Total Shipping Cost =
SUMX (
    SUMMARIZE (
        FILTER ( Sales, Sales[Quantity] > 0 ),
        Sales[ProductKey],
        "ShippingCost", SUMX ( RELATEDTABLE ( Products ), Products[ShippingRate] ) * Sales[Quantity]
    ),
    [ShippingCost]
)
```

## When Iterators Are Appropriate

| Scenario | Approach |
|---------|----------|
| Row-level calculation required (multiplication, conditional) | SUMX with pre-filter |
| Large fact table with no row-level logic needed | SUM (aggregate at source) |
| Nested row context | Consider CALCULATE-based alternatives |
| Millions of rows, no pre-filter possible | Reduce table granularity first with SUMMARIZE |

## Performance Rule

> Never iterate an unfiltered fact table with SUMX. Always pre-filter the table expression to the minimum required row set before iterating.

## Related

- [[sumx]]
- [[filter]]
- [[sum]] — SUMMARIZE for pre-aggregation
- [[dax-performance-5000-measures-source]]
- [[calculate]] — pre-filtering the fact table with CALCULATE before SUMX reduces iteration scope significantly
