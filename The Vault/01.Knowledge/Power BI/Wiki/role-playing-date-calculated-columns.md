---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling (Part 2).md"
note_type: atomic
tags: [power-bi, data-modeling, beginner, role-playing-dates, userelationship, inactive-relationships]
---

# Role-Playing Dates: Multiple Date Columns

A fact table often has multiple date columns: OrderDate, ShipDate, DueDate. Each needs its own relationship to the Date dimension. Only one can be active at a time.

## The Problem

Orders table has:
- OrderDate (when the order was placed)
- ShipDate (when it was shipped)

You want to slice by both Order Date and Ship Date independently.

But: Power BI allows only one active relationship between two tables. The moment you create OrderDate → Date[Date], you can't create ShipDate → Date[Date] as active.

## The Solution: Calculated Columns + USERELATIONSHIP

### Step 1: Create Both Relationships

Create both relationships in Model View. One will be active (solid line), one will be inactive (dashed line).

The active relationship is used by default by all measures.

### Step 2: Create a Calculated Column for the Inactive Date

```dax
ShipDateOnly = DATE(
    YEAR(Orders[ShipDate]),
    MONTH(Orders[ShipDate]),
    DAY(Orders[ShipDate])
)
```

Or more simply:
```dax
ShipDateOnly = INT(Orders[ShipDate])
```

The key is converting DateTime to Date so it matches the Date table's data type.

### Step 3: Use USERELATIONSHIP in a Measure

```dax
Revenue by Ship Date =
CALCULATE(
    [Total Revenue],
    USERELATIONSHIP(Orders[ShipDateOnly], Date[Date])
)
```

USERELATIONSHIP temporarily activates the inactive relationship for this specific measure.

## Calculated Column for Relationship Key

Sometimes the date column doesn't match the Date table's format. Create a matching key:

```dax
// In Orders table
MonthYear = FORMAT(Orders[OrderDate], "YYYY-MM")

// In Date table
MonthYear = Date[Year] & "-" & FORMAT(Date[Month], "00")
```

Then create a relationship on the MonthYear column.

## When to Use Power Query Instead

Power Query transformations happen before data is compressed. For simple date extraction:

1. Select the DateTime column in Power Query
2. Transform → Date → Date Only
3. Rename to OrderDate

This is more efficient than a DAX calculated column — do it in Power Query when you can.

**Use DAX calculated columns when:** you need RELATED() to pull data from another table, or the calculation depends on model relationships.

## Related

- [[data-model-5-common-problems-fixes]] — Problem 4 covers this scenario
- [[power-query-vs-dax-calculated-columns]] — decision framework for Power Query vs DAX
- [[ecommerce-model-step-by-step]] — building the Date table with DAX
