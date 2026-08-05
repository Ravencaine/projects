---
created: 2026-07-27
updated: 2026-08-02
source: "I Analyzed 5,000 DAX Measures: The 5 Patterns That Kill Performance"
note_type: gotcha
tags: [dax, performance, sumx, sum, anti-pattern, iterator]
---

# SUMX on a Single Column: The 27x Performance Anti-Pattern

**Pattern:** Using SUMX to iterate over a table and sum a single column when SUM would work.

**Performance impact:** 27x slower than SUM on the same data.

## The Problem

```dax
-- Anti-pattern: SUMX wrapping a single column reference
Total Sales =
SUMX (
    Sales,
    Sales[Revenue]
)
```

```dax
-- Correct: SUM aggregates directly in the current filter context
Total Sales =
SUM ( Sales[Revenue] )
```

## Why It Happens

- DAX beginners see SUMX as the "advanced" version of SUM and use it everywhere
- The engine must create row context and iterate over every row for SUMX
- SUM does a direct column aggregation with no row iteration needed

## How to Identify

Find measures where the SUMX body is just a single column:

```dax
SUMX ( Table, Table[Column] )   -- THIS = replace with SUM
SUMX ( Table, Table[ColA] )      -- THIS = replace with SUM
SUMX ( FactTable, FactTable[Amount] )  -- THIS = SUM (FactTable[Amount])
```

## The Fix

```dax
-- Always:
SUM ( Table[Column] )

-- Only use SUMX when you need row-level logic:
SUMX ( Sales, Sales[Quantity] * Sales[Price] )   -- OK: row-level multiplication
SUMX ( Sales, IF ( Sales[Discount] > 0, ... ) ) -- OK: conditional per-row
```

## Rule

> If the SUMX expression is just a single column reference — replace with SUM immediately.

## Related

- [[sumx]]
- [[iterator-vs-aggregator-comparison]]
- [[dax-performance-5000-measures-source]]
- [[sum]] — the aggregator that SUMX wraps; prefer SUM over SUMX when the column is already in the filter context
