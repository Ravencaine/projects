---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, optimization, best-practices, beginner, var, performance]
---

# DAX Optimisation: Best Practices Checklist

DAX that works and DAX that works fast are different. These practices separate slow reports from fast ones.

## 1. Use Variables (VAR) for Repeated Calculations

```dax
// ❌ Slow — same expression evaluated twice
Revenue Growth % =
DIVIDE(
    [Total Revenue] - [Revenue PY],
    [Revenue PY]
)

// ✅ Fast — calculated once, stored in variable
Revenue Growth % =
VAR CurrentRevenue = [Total Revenue]
VAR PreviousRevenue = [Revenue PY]
RETURN
    DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue, 0)
```

VAR evaluates once and the result is reused. For complex calculations this can be 2-5x faster.

## 2. Filter on Dimensions, Not Facts

```dax
// ❌ Slow — scans entire Orders table (millions of rows)
Laptop Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(Orders, RELATED(Products[ProductCategory]) = "Laptops")
)

// ✅ Fast — filters Products table (50 rows), relationship does the rest
Laptop Revenue =
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Laptops"
)
```

FILTER on a fact table scans every row. Filter on a dimension table filters a handful of rows and lets the relationship propagate.

## 3. Use DIVIDE Instead of /

```dax
// ❌ Error if Revenue is zero or BLANK
Margin = [Profit] / [Revenue]

// ✅ Handles BLANK and zero gracefully
Margin = DIVIDE([Profit], [Revenue], 0)
```

DIVIDE's third parameter is returned when the denominator is zero or BLANK. Always prefer DIVIDE.

## 4. Avoid Calculated Columns When Measures Work

```dax
// ❌ Adds storage, slows refresh, can't be filtered dynamically
Total Revenue Column = SUM(Orders[TotalAmount])  // Doesn't even work

// ✅ Measure — no storage, fast queries
Total Revenue = SUM(Orders[TotalAmount])
```

Use calculated columns only when: the value needs to be in a slicer; the value is truly static; you need RELATED() across tables.

## 5. Move Expensive Iterators to Calculated Columns

```dax
// ❌ Slow — runs every query
Total Profit =
SUMX(Orders, Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost])))

// ✅ Fast — calculated once at refresh
// Calculated column:
Profit = Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
// Measure:
Total Profit = SUM(Orders[Profit])
```

The calculated column pays its cost once at refresh. The measure has zero per-query cost.

## 6. Check Relationship Directions

Bidirectional filter propagation (filtering both sides of a relationship) creates ambiguity and duplicate row problems. Keep filter direction single: from dimension to fact.

## Best Practices Summary Table

| Practice | Impact |
|----------|--------|
| VAR for repeated expressions | High — avoids double evaluation |
| Filter on dimensions | High — reduces scan size dramatically |
| DIVIDE over / | Medium — prevents errors |
| Calculated columns for static values | High — zero per-query cost |
| Single filter direction | High — prevents row duplication |

## Well-Structured Measure Example

```dax
/*
    Customer Lifetime Value Estimate
    Assumes average customer lifespan of 3 years
    Based on current average order frequency and value
    Updated: 2024-09-15
*/
Customer Lifetime Value =
VAR AvgOrderValue = DIVIDE([Total Revenue], [Total Orders], 0)
VAR AvgOrdersPerYear = DIVIDE([Total Orders], DISTINCTCOUNT(Date[Year]), 0)
VAR EstimatedLifetimeOrders = AvgOrdersPerYear * 3
RETURN
    AvgOrderValue * EstimatedLifetimeOrders
```

Variables, comments, clear naming, safe division.

## Related

- [[iterator-performance-warning]] — detailed treatment of iterator optimisation
- [[filter-functions-allexcept-keepfilters]] — filtering on dimensions vs fact tables
- [[basic-aggregation-measures]] — _Measures table organisation
