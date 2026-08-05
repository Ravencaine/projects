---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, measures, beginner, sum, count, average, distinctcount]
---

# Basic Aggregation Measures

DAX measures start with aggregations — SUM, COUNTROWS, AVERAGE, DISTINCTCOUNT. These are the building blocks every report starts with.

## The Core Five

```dax
Total Revenue = SUM(Orders[TotalAmount])
```
Sums all values in the TotalAmount column, filtered by current context.

```dax
Total Orders = COUNTROWS(Orders)
```
Counts rows in the table. Faster and cleaner than COUNT on a specific column.

```dax
Average Order Value = AVERAGE(Orders[TotalAmount])
```
Averages the TotalAmount column. BLANK values are excluded automatically.

```dax
Total Customers = DISTINCTCOUNT(Orders[CustomerID])
```
Counts unique customer IDs. C001 with 10 orders counts as 1 customer, not 10.

```dax
Total Quantity = SUM(Orders[Quantity])
```
Sum of the Quantity column.

## COUNTROWS Over COUNT

```dax
// ✅ Preferred
Total Orders = COUNTROWS(Orders)

// ❌ Works but less efficient
Total Orders = COUNT(Orders[OrderID])
```

COUNTROWS counts table rows directly. COUNT requires specifying a column. For counting orders/transactions, COUNTROWS is faster and doesn't depend on a specific column being non-null.

## Reusing Measures in Measures

Once a measure is defined, it can be referenced in other measures:

```dax
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

DIVIDE takes numerator, denominator, and an optional third parameter for what to return if the denominator is zero (0 in this case, avoiding #DIV/0 errors).

## The _Measures Table

Best practice: keep all measures in a dedicated table.

```dax
_Measures = ROW("Helper", 1)
```
Create a table with an underscore prefix (pushes it to the top of the field list), hide the Helper column, then move all measures into it.

This keeps the Fields pane organised: dimension tables at the top, measures table below.

## Testing Measures

Create a Card visual for each measure and verify the numbers match the source data. If the numbers don't match, the issue is usually in the model (relationships) rather than the measure itself.

## Related

- [[dax-vs-excel-mindset-difference]] — why these measures produce different results based on context
- [[row-context-vs-filter-context]] — filter context is what makes these measures reactive
- [[calculate-context-modifier]] — CALCULATE filters what these measures aggregate
- [[implicit-measure-trap]] — why explicit measures are better than dragging fields directly
