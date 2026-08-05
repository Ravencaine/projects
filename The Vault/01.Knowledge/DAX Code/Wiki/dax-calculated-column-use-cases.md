---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, calculated-column, use-cases, beginner, related]
---

# DAX Calculated Column Use Cases

Calculated columns belong in the data model when the result is a property of each row — something you need to filter, slice, use as a dimension in a Matrix, or join across tables. These are the situations where a column (not a measure) is the right choice.

## Use Case 1: Categorisation / Classification

Create a category based on a threshold or condition. The result becomes a filterable attribute.

```dax
CustomerTier =
SWITCH(TRUE(),
    Customers[TotalPurchases] > 10000, "VIP",
    Customers[TotalPurchases] > 5000,  "Gold",
    Customers[TotalPurchases] > 1000,  "Silver",
    "Bronze"
)
```

Use CustomerTier in a slicer or as rows in a Matrix. This is the classic use case for a calculated column.

## Use Case 2: Relationship Key

Create a key column to establish or extend a relationship between tables.

```dax
DateKey = FORMAT(Orders[OrderDate], "YYYYMMDD")
```

Format the date as an integer string to match a date dimension's key column. This enables the relationship even when source and dimension use different date formats.

## Use Case 3: Text Combination / Full Name

Combine columns that belong logically together.

```dax
FullName = Customers[FirstName] & " " & Customers[LastName]
```

FullName as a column lets you filter by full name or display it as a single value in a visual without needing to concatenate in every measure.

## Use Case 4: Row-Level Property with RELATED()

Pull attributes from related tables into the current table for filtering or display without needing to use RELATED() in every measure.

```dax
ProductFullCategory =
RELATED(ProductCategory[CategoryName]) & " - " &
RELATED(ProductSubcategory[SubcategoryName])
```

This is the most DAX-specific use case — `RELATED()` only works in calculated columns and row context (within iterators). You cannot do this in Power Query without merging tables.

## Use Case 5: Row-Level Boolean Flag

Mark each row with a yes/no property.

```dax
IsLargeOrder =
IF(Sales[OrderQuantity] >= 100, "Yes", "No")
```

Use the flag in a slicer to separate large orders from standard orders.

## When NOT to Use a Calculated Column

- For aggregations (use a measure)
- For ratios or percentages that need correct totals (use a measure)
- For values that don't need to be filtered or sliced (use a measure)

## Related

- [[calculated-column-vs-measure-decision-tree]] — the decision framework
- [[calculated-column-row-context]] — the context that enables all these use cases
- [[power-query-vs-dax-calculated-columns]] — why RELATED() forces the DAX choice
