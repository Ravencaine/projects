---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, filter-functions, beginner, allexcept, keepfilters, filter]
---

# Filter Functions: ALLEXCEPT and KEEPFILTERS

ALLEXCEPT removes all filters except the ones you specify. KEEPFILTERS combines new filters with existing ones instead of replacing them.

## ALLEXCEPT — Keep Only Specific Filters

```dax
Revenue by Year Only =
CALCULATE(
    [Total Revenue],
    ALLEXCEPT(Date, Date[Year])
)
```

This removes all filters from the Date table EXCEPT Date[Year]. If a user has selected Quarter = Q1 and Month = January, this measure ignores those filters and shows the full year total.

**Common use case:** Customer lifetime revenue — total revenue per customer regardless of what date range is selected:

```dax
Customer Lifetime Revenue =
CALCULATE(
    [Total Revenue],
    ALLEXCEPT(Orders, Orders[CustomerID])
)
```

No matter the date range selected, each customer shows their all-time revenue total.

## ALLEXCEPT vs ALL

| Function | Removes | Keeps |
|----------|---------|-------|
| ALL(Date) | All filters from Date | Nothing |
| ALLEXCEPT(Date, Date[Year]) | All filters from Date | Date[Year] only |

## KEEPFILTERS — Combine Instead of Replace

By default, CALCULATE's filter argument replaces the existing filter on that column:

User selects "Furniture" in a slicer.

```dax
Monitor Revenue =
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Monitors"
)
```

This REPLACES "Furniture" with "Monitors" — shows monitor revenue even though the user selected Furniture.

```dax
Monitor Revenue =
CALCULATE(
    [Total Revenue],
    KEEPFILTERS(Products[ProductCategory] = "Monitors")
)
```

This COMBINES the filters: "Furniture" AND "Monitors" — since no product is both, this returns BLANK.

**When to use KEEPFILTERS:** When you want users to see blank results for combinations that don't exist, rather than silently showing data they didn't select.

## FILTER — Custom Row-by-Row Conditions

FILTER evaluates a table row by row and returns only rows that match a condition:

```dax
High Value Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(
        Orders,
        Orders[TotalAmount] > 1000
    )
)
```

1. FILTER looks at every row in Orders
2. Keeps only rows where TotalAmount > 1000
3. SUM calculates on those filtered rows

**Combining with CALCULATE filters:**

```dax
Enterprise High Value Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(
        Orders,
        Orders[TotalAmount] > 1000
    ),
    Customers[CustomerSegment] = "Enterprise"
)
```

FILTER creates a row-level condition; CALCULATE adds a separate filter. Both apply.

## Filter Function Decision Tree

| Goal | Use |
|------|-----|
| Remove all filters from a table/column | REMOVEFILTERS or ALL |
| Remove all filters except specific ones | ALLEXCEPT |
| Respect visual filters but ignore row context | ALLSELECTED |
| Create a custom row-by-row condition | FILTER |
| Combine new filter with existing instead of replacing | KEEPFILTERS |

## Related

- [[filter-functions-all-allselected]] — ALL and ALLSELECTED for the % of total pattern
- [[calculate-context-modifier]] — CALCULATE is where all these filters are applied
- [[advanced-patterns-ranking-abc-pareto]] — ALLEXCEPT used in customer lifetime value and ranking patterns
