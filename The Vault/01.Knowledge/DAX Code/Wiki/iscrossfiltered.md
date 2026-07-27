---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# ISCROSSFILTERED

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the specified table or column is cross-filtered.

## Syntax

```dax
ISCROSSFILTERED(<TableNameOrColumnName>)
```

## Remarks

A column or table is said to be cross-filtered when a filter is applied to ColumnName, any column of TableName, or to any column of a related table. A column or table is said to be filtered directly when a filter is applied to ColumnName or to any column of TableName. Therefore, the ISFILTERED function also returns TRUE when ColumnName or any column of TableName is filtered. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.