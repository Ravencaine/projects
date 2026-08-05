---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, calculate, patterns, beginner, filter]
---

# CALCULATE Pattern Library

Six patterns covering the most common uses of CALCULATE. Each is a copy-paste template.

## Pattern 1: Specific Value

Filter to one exact value.

```dax
Furniture Revenue =
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Furniture"
)
```

## Pattern 2: Greater Than / Less Than

Numeric comparison filters.

```dax
Large Order Revenue =
CALCULATE(
    [Total Revenue],
    Orders[TotalAmount] > 1000
)
```

## Pattern 3: Between Two Values

Two conditions on the same column.

```dax
Mid-Range Revenue =
CALCULATE(
    [Total Revenue],
    Orders[TotalAmount] >= 100,
    Orders[TotalAmount] <= 500
)
```

## Pattern 4: IN List

Multiple specific values — cleaner than chained OR.

```dax
Tech Revenue =
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] IN {"Laptops", "Monitors", "Tablets"}
)
```

## Pattern 5: NOT Equal

Exclude a value.

```dax
Non-Technology Revenue =
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] <> "Technology"
)
```

## Pattern 6: Combining Dimension Filters

Filter across multiple related tables.

```dax
Enterprise Furniture Revenue =
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Furniture",
    Customers[CustomerSegment] = "Enterprise",
    Date[Year] = 2024
)
```

All three filters apply simultaneously — AND logic across tables.

## Combining with Measures

CALCULATE filters a measure (which already has filter context). The CALCULATE filter adds on top of whatever is already in place:

```dax
Enterprise % of Total =
DIVIDE(
    [Enterprise Revenue],     // Already a measure with context
    [Total Revenue],
    0
)

Enterprise Revenue =
CALCULATE(
    [Total Revenue],
    Customers[CustomerSegment] = "Enterprise"
)
```

## Related

- [[calculate-context-modifier]] — what CALCULATE does and why it matters
- [[filter-functions-all-allselected]] — % of total pattern uses ALL() inside CALCULATE
- [[time-intelligence-functions]] — time filters use CALCULATE as their foundation
