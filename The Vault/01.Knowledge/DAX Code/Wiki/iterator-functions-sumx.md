---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, iterator-functions, beginner, sumx, averagex, countx, minx, maxx]
---

# Iterator Functions: SUMX and Beyond

Iterator functions calculate an expression for each row, then aggregate the results. They bridge row context and aggregation.

## Why Simple Aggregations Sometimes Fail

**Problem:** Calculate total profit.

You have Orders[TotalAmount], Orders[Quantity], and Products[UnitCost]. Profit per order = TotalAmount - (Quantity × UnitCost).

```dax
// ❌ Wrong
Total Profit =
    SUM(Orders[TotalAmount])
    - SUM(Orders[Quantity]) * Products[UnitCost]
```

This uses a single UnitCost for all orders. But each order has a different product with a different cost.

**You need to calculate profit for EACH ORDER, then sum those individual profits.**

## SUMX — The Most Common Iterator

```dax
Total Profit =
SUMX(
    Orders,
    Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
)
```

**How it works:**
1. SUMX creates row context inside the Orders table
2. For each row: TotalAmount - (Quantity × UnitCost) → profit for that order
3. SUMX sums all the individual profits

## AVERAGEX — Average Per Row

```dax
Average Profit per Order =
AVERAGEX(
    Orders,
    Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
)
```

Calculates profit per order, then averages them.

## COUNTX — Count Rows Matching Condition

```dax
High Value Orders =
COUNTX(
    Orders,
    IF(Orders[TotalAmount] > 1000, 1, BLANK())
)
```

Returns 1 for each qualifying order, BLANK for others. COUNTX counts the 1s (BLANKs are ignored).

**Clearer alternative using FILTER + COUNTROWS:**

```dax
High Value Orders =
COUNTROWS(
    FILTER(Orders, Orders[TotalAmount] > 1000)
)
```

## MINX and MAXX — Extreme Values Per Row

```dax
Lowest Profit Margin =
MINX(
    Orders,
    DIVIDE(
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost])),
        Orders[TotalAmount]
    )
)
```

Finds the worst individual order margin.

## When Iterators Are Necessary

| Scenario | Use SUMX |
|----------|---------|
| Each row needs a different value from a related table | ✅ |
| Per-row calculation before aggregation | ✅ |
| Weighted calculations (quantity × price) | ✅ |
| Simple column sum | ❌ Use SUM directly |

## The Syntax Pattern

```dax
SUMX(
    <table>,          // The table to iterate over
    <expression>      // Calculated for each row
)
```

The expression has row context — it can reference columns from the iterated table directly and use RELATED() to pull from related tables.

## Related

- [[row-context-vs-filter-context]] — iterators create row context inside measures
- [[iterator-performance-warning]] — iterators are expensive; use calculated columns when possible
- [[advanced-patterns-ranking-abc-pareto]] — SUMX used in running totals and Pareto analysis
