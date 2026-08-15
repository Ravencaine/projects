---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, unpivot, reshape, long-format, wide-to-long]
---

# Unpivot Columns

Convert wide (matrix) data to tall (normalized) format — essential for time-series and repeated metrics.

## Purpose

Reports often present data in cross-tab format (years or months as columns). Power BI visuals need tall format (one row per observation) for proper modelling. Unpivot converts attribute-value pairs from columns into rows.

## Components

- `Table.Unpivot`
- `Table.UnpivotOtherColumns`

## Structure

```m
// Unpivot specific columns only
Table.Unpivot(Source, {"Jan", "Feb", "Mar"}, "Month", "Sales")

// Unpivot all columns except identifier columns
Table.UnpivotOtherColumns(Source, {"ID", "Product"}, "Attribute", "Value")
```

## Example

```m
// Wide: columns = Jan, Feb, Mar, Apr
// Tall: one row per month with Month and Revenue columns
Table.Unpivot(Source, {"Jan_Revenue", "Feb_Revenue", "Mar_Revenue"}, "Month", "Revenue")
```

```
Before (wide):
ID | Jan | Feb | Mar
1  | 100 | 200 | 150

After (tall):
ID | Attribute | Value
1  | Jan       | 100
1  | Feb       | 200
1  | Mar       | 150
```

## When to Use

- Multiple time periods as columns
- Survey results with question columns
- Scorecards with metric names as headers

## Related

- [[Fill-Down-Up]] — fill nulls that may appear after unpivoting
- [[Group-By]] — aggregate after reshaping to tall format
