---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MINA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the smallest value in a column.

## Syntax

```dax
MINA(<column>)
```

## Remarks

The MINA function takes as argument a column that contains numbers, and determines the smallest value as follows: If the column contains no values, MINA returns 0 (zero). Rows in the column that evaluates to logical values, such as TRUE and FALSE are treated as 1 if TRUE and 0 (zero) if FALSE. Empty cells are ignored. If you want to compare text values, use the MIN function. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.