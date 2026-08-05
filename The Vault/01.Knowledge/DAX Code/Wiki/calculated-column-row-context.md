---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, calculated-column, row-context, beginner, filter-context]
---

# Calculated Column: Row Context

Calculated columns evaluate one row at a time. This row context is the defining characteristic — and the source of the most common DAX mistakes.

## How Row Context Works

When a calculated column formula runs, Power BI looks at one row, evaluates the expression using values from that row, and stores the result. Then it moves to the next row. Each row is independent.

Think of it like Excel: when you write `=A1*B1` in cell C1, the formula looks at A1 and B1 in the same row. Calculated columns do the same thing across an entire table.

## Examples That Work in Row Context

```dax
FullName = Customers[FirstName] & " " & Customers[LastName]
```
Concatenating two columns from the same row — works because both values exist in the current row.

```dax
OrderTotal = Sales[Quantity] * Sales[UnitPrice]
```
Multiplying two columns in the same table — works because both values exist in the current row.

```dax
PriceCategory =
IF(Products[UnitPrice] < 10, "Budget",
IF(Products[UnitPrice] < 50, "Standard",
"Premium"))
```
Classifying each product based on its own price — works because UnitPrice exists in the current row.

```dax
DateKey = FORMAT(Orders[OrderDate], "YYYYMMDD")
```
Extracting a formatted date component — works because OrderDate exists in the current row.

## Examples That Fail in Row Context

```dax
TotalRevenue = SUM(Sales[SalesAmount])  // Does NOT work
```
Asking for the sum of ALL sales while evaluating one row. The result would be the grand total written to every single row — not what you intended.

```dax
ProfitCategory =
IF([Total Profit] > 10000, "High", "Low")  // Does NOT work as a column
```
Measures don't have row context. A calculated column can't evaluate a measure — there is no single "Total Profit" value for a single row.

## The Pattern

> **Row context = one row at a time. If your formula needs one value from the current row → column. If your formula needs an aggregation of many rows → measure.**

## Related

- [[measure-filter-context]] — the opposite context type
- [[calculated-column-vs-measure-decision-tree]] — decision framework using this distinction
- [[calculated-column-vs-measure-total-sums]] — why percentages in columns give wrong totals
