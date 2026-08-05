---
created: 2026-08-01
updated: 2026-08-02
source: "Power Query or DAX Make the Right Choice Every Time.md"
note_type: atomic
tags: [power-bi, power-query, dax, performance, model-size, beginner]
---

# Power Query vs DAX: Model Size and Performance Impact

Both tools affect model size and performance — but in opposite ways.

## Power Query: Reduces Bloat Before It Hits the Model

Power Query transformations happen **before** data is loaded. Every column removed, every aggregation pre-computed, every unnecessary row filtered — all of that never enters the model.

**Result:** Smaller model → less memory → faster queries.

Power Query does the heavy lifting once, at refresh time. The result is a lean model that DAX can work with efficiently.

## DAX: Computes on Demand, in Memory

DAX measures run **every time a visual renders**, scanning whatever data is in the model. Every unnecessary column, every raw detail left un-aggregated — all of that adds to the scan.

**Result:** Larger model → more RAM → slower measures, especially on large fact tables.

DAX on a bloated model = expensive per-visual recalculation across millions of rows.

## The Performance Gradient

```
Closer to source (Power Query)  =  Faster at query time, smaller model
Further from source (DAX)       =  More flexible, higher CPU/RAM cost
```

## Practical Rule

The more you push toward the source — clean in Power Query, pre-aggregate known totals — the faster every DAX measure will run.

**The trade-off:** Power Query makes changes harder once deployed (you modify the query chain). DAX makes changes easier post-deployment (you write a new measure). But DAX's flexibility has a performance cost.

## The Extreme Case

A model with:
- Raw transaction-level detail (no pre-aggregation)
- 12M rows with every column imported
- DAX measures doing all aggregation on the fly

This model works but is slow — because every measure scan is expensive, and every visual re-triggers the same expensive scans.

The fix: use Power Query to pre-aggregate to monthly level, remove unused columns, then let DAX handle the dynamic filtering on top.

## Related

- [[power-query-vs-dax-core-difference]] — when each tool runs
- [[static-vs-dynamic-aggregations]] — what to pre-aggregate in Power Query
- [[power-query-dax-combined-usage-patterns]] — the 6 rules for combining both tools
