---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, context, row-context, filter-context, beginner, calculated-column, measure]
---

# Row Context vs Filter Context

Context is what determines which rows DAX looks at. Two types, two behaviours.

## Row Context — "I'm Looking at This Specific Row"

Row context activates automatically when you create a calculated column. DAX evaluates the formula for each row, one at a time.

```dax
// Calculated column in Orders table
Order Size Category =
IF(Orders[TotalAmount] > 1000, "Large", "Small")
```

DAX evaluates row by row:
- Row 1: TotalAmount = $2,400 → "Large"
- Row 2: TotalAmount = $125 → "Small"
- Row 3: TotalAmount = $300 → "Small"

Each row is evaluated independently. `RELATED()` works in row context — it follows relationships to fetch values from related tables.

```dax
// Works in row context — follows the relationship
Profit = Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
```

## Filter Context — "I'm Only Considering Rows That Match These Criteria"

Filter context activates when a measure runs. DAX evaluates based on whatever filters are currently active in the report — slicers, visual-level filters, page filters, and relationships.

```dax
Total Revenue = SUM(Orders[TotalAmount])
```

- No filters: sums ALL orders ($2,657,000)
- Year = 2024: sums only 2024 orders ($1,823,000)
- Year = 2024 AND Category = "Laptops": sums only 2024 laptop orders ($1,247,000)

The measure didn't change. The filter context changed.

## How Visuals Create Filter Context

A table visual with ProductCategory and Total Revenue creates filter context automatically per row:

```
Category     | Total Revenue
Laptops      | $1,847,000   ← Power BI filtered to Category = "Laptops"
Monitors     | $523,000     ← Power BI filtered to Category = "Monitors"
```

For the "Laptops" row, the measure calculates with Category = "Laptops" filter applied. For "Monitors", a different filter. All from one measure.

## The Quick Test

```dax
Test Measure = SUM(Orders[TotalAmount])     // ✅ Works as a measure
Test Column  = Orders[TotalAmount]           // ❌ Error in a measure
```

`Orders[TotalAmount]` in a measure has no row context — there is no single row. The column has thousands of rows. DAX can't pick one.

## The Mental Model

| Type | Think of it as | Activated by |
|------|---------------|--------------|
| Row context | "This row right here" | Calculated columns, iterators |
| Filter context | "The set of rows currently visible" | Measures, visuals, slicers |

## Related

- [[dax-vs-excel-mindset-difference]] — context is the key difference from Excel
- [[calculate-context-modifier]] — CALCULATE changes filter context
- [[iterator-functions-sumx]] — SUMX creates row context inside a measure
