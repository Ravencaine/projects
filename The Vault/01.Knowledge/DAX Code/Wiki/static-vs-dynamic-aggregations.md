---
created: 2026-08-01
updated: 2026-08-02
source: "Power Query or DAX Make the Right Choice Every Time.md"
note_type: atomic
tags: [power-bi, dax, power-query, aggregation, beginner, performance]
---

# Static vs Dynamic Aggregations: When to Use Each

The decision between Power Query and DAX often comes down to one question: do you know the aggregation in advance, or does the user need to decide?

## Power Query: Known, Static Aggregations

When the aggregation is predictable and fixed, Power Query is the better choice.

**Examples of known aggregations:**
- Monthly sales totals
- Quarterly revenue per region
- Yearly customer acquisition count
- Pre-calculated daily averages

Power Query computes these once — during refresh — and stores the result in the model.

**Benefits:**
- No per-visual re-calculation
- Slicers respond instantly (the data is already aggregated)
- Smaller model (pre-aggregated rows < raw rows)
- DAX runs faster on pre-aggregated data

**Rule:** If you know the aggregation logic upfront and it won't change per user interaction, do it in Power Query.

## DAX: Dynamic, User-Driven Aggregations

When users need to slice, dice, and explore on their own terms, DAX is the right tool.

**Examples requiring dynamic aggregation:**
- Revenue by any region the user selects
- Profit margin across any product category
- Drill-down from annual → quarterly → monthly → daily
- Custom hierarchies the user defines

DAX measures calculate on the fly based on whatever filters and slicers are active. The same measure produces different results per visual context.

**Trade-off:** Dynamic flexibility comes with per-query CPU and RAM cost. On large datasets, dynamic calculations are slower than pre-computed ones.

## The Decision Rule

> **Use Power Query when you know the numbers upfront. Use DAX when your users need to explore and slice the data themselves.**

## Hybrid Approach

The most efficient models use both:

- **Power Query:** pre-aggregate to monthly level, remove unused columns, clean data
- **DAX:** calculate dynamic metrics on top of the clean, lean model (profit margin, YoY growth, custom rankings)

Power Query handles what it can. DAX handles what it must.

## Related

- [[power-query-vs-dax-core-difference]] — when each tool runs
- [[power-query-vs-dax-model-size-performance]] — performance impact of the choice
- [[power-query-dax-combined-usage-patterns]] — rules for combining both
