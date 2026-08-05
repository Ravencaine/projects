---
created: 2026-07-27
updated: 2026-08-02
source: "Iterators in DAX: SUMX, AVERAGEX, RANKX"
note_type: comparison
tags: [dax, iterators, aggregators, sumx, sum, averagex, average]
---

# Iterator vs Aggregator Comparison

Aggregators (SUM, AVERAGE, COUNT) work directly on a column in the current filter context. Iterators (SUMX, AVERAGEX, RANKX) loop row-by-row over a table and evaluate an expression per row.

## When Aggregators Win

| Scenario | Aggregator | Iterator alternative |
|---------|-----------|---------------------|
| Sum a column | `SUM(Tbl[Col])` | `SUMX(Tbl, Tbl[Col])` — **27x slower** |
| Average a column | `AVERAGE(Tbl[Col])` | `AVERAGEX(Tbl, Tbl[Col])` — **34x slower** |

**Rule:** If the iterator expression is just a single column reference, use the aggregator.

## When Iterators Are Required

| Scenario | Iterator |
|---------|----------|
| Row-by-row multiplication | `SUMX(Sales, Sales[Qty] * Sales[Price])` |
| Conditional per-row logic | `SUMX(Sales, IF(Sales[Qty]>10, Sales[Revenue], 0))` |
| Weighted average | `AVERAGEX(Sales, Sales[Rev] / Sales[Qty])` |
| Ranking | `RANKX(ALL(Customers), [Total Sales])` |

## Performance Rule

> Use aggregators whenever the expression is a single column reference. Use iterators only when row-level computation logic is required.

## Related

- [[sumx]]
- [[averagex]]
- [[rankx]]
- [[sumx-vs-sum-gotcha]]
