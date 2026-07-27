---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter]
---

# TREATAS

Applies to: Calculated column Calculated table Measure Visual Applies the result of a table expression as filters to columns from an unrelated table.

## Syntax

```dax
TREATAS(table_expression, <column>[, <column>[, <column>[,…]]]} )
```

## Remarks

The number of columns specified must match the number of columns in the table expression and be in the same order. If a value returned in the table expression does not exist in the column, it is ignored. For