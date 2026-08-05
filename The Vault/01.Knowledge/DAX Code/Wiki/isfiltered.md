---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# ISFILTERED

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the specified table or column is being filtered directly.

## Syntax

```dax
ISFILTERED(<TableNameOrColumnName>)
```

## Remarks

A column or table is said to be filtered directly when a filter is applied to ColumnName or any column of TableName. A column or table is said to be cross-filtered when a filter is applied to ColumnName, any column of TableName, or to any column of a related table. Therefore, the ISCROSSFILTERED function also returns TRUE when ColumnName, any column of TableName, or a column of a related table is filtered. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.