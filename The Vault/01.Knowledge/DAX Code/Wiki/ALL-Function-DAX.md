---
created: 2026-08-05
updated: 2026-08-05
source: ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)
note_type: function
tags: [dax, all, filter-context, calculate, return-table, sumx]
---

# `ALL()` DAX

Removes all filters from a table or column and returns the result as a table or column value — enabling unfiltered calculations and use as a table expression in other DAX functions like SUMX and FILTER.

## Definition

> ALL returns all the rows in a table, or all the values in a column, ignoring any filters that might have been applied.

## Syntax

```dax
ALL(<TableName>)
ALL(<ColumnName>[, <ColumnName>[, …]])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `TableName` | table | Remove filters from the entire table |
| `ColumnName` | column | Remove filters from one or more columns (can specify multiple) |

- Providing a table: removes filters from all columns in that table
- Providing column names: removes filters from only those columns
- No arguments: returns all rows from all tables in the model — rarely used

## Return Value

**A table or column with all filters removed.** This is the key property: ALL's result can be stored, passed to another function, or used as a table expression.

## Common Pattern: Remove Slicer Filters

```dax
Total Sales = SUM(Sales[Amount])

Total Sales ALL =
CALCULATE(
    [Total Sales],
    ALL(DimProduct),
    ALL(DimSalesTerritory)
)
```

`Total Sales ALL` ignores the Country and Color slicers — it always returns the grand total across all products and territories.

## ALL as Table Expression: SUMX

Because ALL returns a table, it can be used inside SUMX:

```dax
Total Sales SUMX =
SUMX(
    ALL(Sales),          -- iterate over all rows, ignoring filters
    Sales[Quantity] * Sales[Price]
)
```

This is the critical difference from REMOVEFILTERS — ALL can appear as an argument to SUMX.

## ALL vs REMOVEFILTERS

| Behaviour | ALL | REMOVEFILTERS |
|-----------|-----|---------------|
| Removes filters | ✓ | ✓ |
| Returns a value | ✓ (table/column) | ✗ (nothing) |
| Usable in SUMX | ✓ | ✗ |
| Usable in FILTER | ✓ | ✗ |
| Modern DAX preference | Legacy | Preferred for clarity |

## Related

- [[REMOVEFILTERS-Function-DAX]]
- [[ALL-vs-REMOVEFILTERS]]
- [[Removing-Slicer-Filters-ALL]]
