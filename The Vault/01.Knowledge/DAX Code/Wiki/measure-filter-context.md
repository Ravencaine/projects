---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, measure, filter-context, beginner, aggregation]
---

# Measure: Filter Context

Measures don't evaluate row-by-row — they aggregate all the rows currently visible under the active filters in your report. This filter context is the opposite of row context.

## How Filter Context Works

When a visual renders, Power BI applies every active filter (slicer selections, visual-level filters, page-level filters, report-level filters, relationships) to determine which rows are visible. The measure then aggregates those visible rows.

The measure has no single-row access — it only sees the set of rows that pass through all the active filters. It computes a single result from that set.

## Examples That Work in Measures

```dax
Total Sales = SUM(Sales[SalesAmount])
```
Sums all visible SalesAmount values. If you slice by 2024, it sums 2024. If you drill to Q1, it sums Q1. The same formula, different results depending on what is filtered.

```dax
Total Customers = DISTINCTCOUNT(Sales[CustomerID])
```
Counts distinct customers visible under the current filter. Same principle — a different slice of the data gives a different number.

```dax
Average Order Value =
DIVIDE(
    SUM(Sales[SalesAmount]),
    DISTINCTCOUNT(Sales[OrderID]),
    0
)
```
Combines two aggregations — works because both are computed over the same filtered set of rows.

## The Impossible in a Measure (Without Iteration)

```dax
Invalid Measure = Sales[Quantity] * Sales[UnitPrice]  // Error
```
"A single value for column 'Quantity' cannot be determined." The measure sees thousands of rows under the filter — it doesn't know which row's Quantity to multiply. This is why SUMX exists: it creates row context inside a measure.

```dax
Total Revenue = SUMX(Sales, Sales[Quantity] * Sales[UnitPrice])
```
SUMX iterates row-by-row within the measure, computes the expression for each row, then sums. This is the bridge between filter context (where the measure lives) and row context (where the per-row calculation happens).

## The Pattern

> **Filter context = the set of rows currently visible. If your formula needs to aggregate many rows → measure. If it needs to work row-by-row and then aggregate → SUMX (or other iterator).**

## Related

- [[calculated-column-row-context]] — the opposite context type
- [[calculated-column-vs-measure-decision-tree]] — decision framework
- [[field-as-raw-data-column]] — where implicit measures come from
