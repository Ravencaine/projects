---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, dax, performance, optimization, intermediate]
---

# DAX Measure Optimization Patterns

Once the model is clean, the measures themselves are the next target. The rule: push heavy, repeatable math upstream; keep DAX for light, dynamic work.

## The Anti-Pattern: SUMX with RELATED

```dax
-- SLOW: row-by-row context transition across 12M rows
Total Sales Slow =
SUMX (
    FactSales,
    FactSales[Quantity] * RELATED ( DimProduct[UnitPrice] )
)
```

`RELATED` forces a row-by-row lookup across every row in the fact table. With 12M rows, this is expensive on every visual refresh.

## The Fix: Precompute in Power Query

If `UnitPrice` is fixed at the time of transaction, compute `LineTotal` once during data load:

**In Power Query:** `LineTotal = Quantity * UnitPrice`

```dax
-- FAST: simple aggregation; engine handles it directly
Total Sales = SUM ( FactSales[LineTotal] )
```

No context transition. No row-by-row iteration. The storage engine processes it directly.

## When to Keep the Calculation in DAX

- Prices change historically and need to reflect current pricing
- Dynamic business rules that vary by filter context
- Any case where the calculation must react to the current state of the model

**Rule:** Optimize without changing the business meaning of the measure.

## Measure Branching

Build complex measures from smaller, reusable ones:

```dax
Total Revenue = SUM ( FactSales[LineTotal] )
Total Cost    = SUM ( FactSales[LineCost] )
Total Profit  = [Total Revenue] - [Total Cost]
Profit Margin = DIVIDE ( [Total Profit], [Total Revenue], 0 )
```

Benefits:
- Each sub-measure can be reused
- Easier to debug (test Total Revenue in isolation)
- Next round of optimization is simpler

## General Rules

- Prefer `SUM` over `SUMX` wherever possible
- Precompute in Power Query or SQL when the data doesn't change between refreshes
- Avoid `CALCULATE` wrapping `SUMX` unless the filter context is genuinely needed
- Use `DIVIDE` instead of `/` to handle division by zero gracefully

## Related

- [[star-schema-performance-impact]] — clean model is the foundation for fast measures
- [[filter-functions-all-allselected]] — CALCULATE context modifiers and their performance impact
