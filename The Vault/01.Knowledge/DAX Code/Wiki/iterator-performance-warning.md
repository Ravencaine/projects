---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, iterator, performance, optimization, beginner]
---

# Iterator Performance: When SUMX Is Expensive

Iterator functions are powerful but computationally expensive. For a million-row fact table, SUMX performs a million calculations per query. Understand when they're necessary and when to avoid them.

## The Performance Cost

SUMX/AVERAGEX iterate row by row. Each row in the specified table triggers a full evaluation of the expression.

| Table size | SUMX operations per query |
|-----------|------------------------|
| 10,000 rows | 10,000 |
| 1,000,000 rows | 1,000,000 |
| 10,000,000 rows | 10,000,000 |

This is why a simple `SUM(Orders[Profit])` is faster than `SUMX(Orders, Orders[TotalAmount] - Orders[Cost])` — SUM directly aggregates a column without row-by-row evaluation.

## When to Avoid Iterators

- Simple aggregations (use SUM, AVERAGE, COUNTROWS directly)
- Large fact tables with millions of rows
- Nested iterators (performance compounds)
- Calculations that don't need per-row logic

## When Iterators Are Necessary

- The expression requires data from multiple tables via RELATED()
- Each row needs a different calculated value before summing
- Dynamic per-row conditions that can't be expressed as a simple column aggregation

## The Calculated Column Alternative

If the calculation doesn't need to be dynamic, do it once as a calculated column during refresh:

```dax
// ✅ Slow: calculated every query
Total Profit =
SUMX(Orders, Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost])))

// ✅ Fast: calculated once during refresh, stored in column
// Calculated column in Orders:
Profit = Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))

// Then simply:
Total Profit = SUM(Orders[Profit])
```

The column approach: one-time calculation at refresh, zero per-query cost.

## Avoiding Repeated Calculations in VAR

The most expensive mistake: repeating the same iterator inside VAR:

```dax
// ❌ SLOW — profit expression runs twice
Profit Analysis =
VAR HighValueProfit =
    SUMX(
        FILTER(Orders, Orders[TotalAmount] > 1000),
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
    )
VAR TotalProfit =
    SUMX(
        Orders,
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
    )
RETURN
    DIVIDE(HighValueProfit, TotalProfit)

// ✅ FAST — use calculated column instead
// Orders[Profit] column already computed once at refresh
High Value Profit =
    CALCULATE(
        SUM(Orders[Profit]),
        Orders[TotalAmount] > 1000
    )
Total Profit = SUM(Orders[Profit])
Profit % = DIVIDE([High Value Profit], [Total Profit])
```

## The Performance Decision Tree

| Question | Answer | Action |
|----------|--------|--------|
| Does each row need a different value from a related table? | Yes | SUMX with RELATED() |
| Can it be done as a calculated column once at refresh? | Yes | Use calculated column |
| Is it a simple column sum? | Yes | Use SUM directly |
| Is the fact table very large? | Yes | Avoid iterators; use columns |

## Related

- [[iterator-functions-sumx]] — the iterator functions this warning applies to
- [[dax-optimization-best-practices]] — full optimisation checklist including VAR and filter direction
