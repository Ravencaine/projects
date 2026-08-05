---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Copy-Pasting DAX The Power of Measure Branching in Power BI.md"
note_type: atomic
tags: [dax, measure-branching, performance, dax-studio, beginner, intermediate]
---

# Measure Branching and Performance

Measure branching can materially improve DAX query performance. The source article reported a ~30% reduction in query time (2.8s → 1.9s) after refactoring copy-paste measures into a branching structure.

## Why Branching Improves Performance

Power BI's formula engine caches the result of each measure expression. When multiple measures share a common sub-expression:

**Without branching (copy-paste):**
```
Profit Margin %      → computes SUM(Revenue) + SUM(Cost) separately
YTD Profit Margin %  → computes SUM(Revenue) + SUM(Cost) separately
YoY Profit Margin %  → computes SUM(Revenue) + SUM(Cost) separately
```
Each measure recalculates the same aggregations independently → redundant CPU work.

**With branching:**
```
Base Sales = SUM ( Sales[Revenue] )
Base Cost  = SUM ( Sales[Cost] )

Gross Profit = [Base Sales] - [Base Cost]

Profit Margin %      → references [Gross Profit] (cached)
YTD Profit Margin %  → references [Gross Profit] (cached)
YoY Profit Margin %  → references [Gross Profit] (cached)
```
`SUM(Sales[Revenue])` and `SUM(Sales[Cost])` are computed **once**, cached, and reused across all measures.

## When to Expect the Performance Benefit

The benefit is most significant when:
- Multiple measures reference the same base aggregations (e.g., Revenue appears in 10+ measures)
- Measures are used together in the same visual (e.g., Profit Margin % alongside YTD Profit and YoY Growth on one chart)
- The fact table is large (millions of rows)

The benefit is negligible when:
- Each measure uses completely different fact table columns
- The model is small (< 100K rows)
- Measures are used in isolation (never on the same visual)

## Measuring the Difference

Use **DAX Studio** to measure query times before and after refactoring:

```dax
-- Run in DAX Studio Query Editor
EVALUATE
SUMMARIZECOLUMNS (
    'Date'[Year],
    "Total Sales", [Total Sales],
    "Profit %", [Profit %]
)
```

Time the query in DAX Studio's Server Timings pane. Compare before (copy-paste) vs after (branching) to quantify the improvement.

## When Branching Can Hurt Performance

Circular dependencies or very deep chains (> 5 layers) can add overhead. Keep chains shallow and check dependency trees in Tabular Editor.

## Related

- [[measure-branching-pattern]] — the full pattern
- [[measure-branching-calculate-composition]] — how CALCULATE interacts with the cache
- [[dax-optimization-best-practices]] — broader DAX performance optimisation
