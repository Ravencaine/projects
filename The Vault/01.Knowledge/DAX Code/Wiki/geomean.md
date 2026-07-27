---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# GEOMEAN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the geometric mean of the numbers in a column.

## Syntax

```dax
GEOMEAN(<column>)
```

## Remarks

Only the numbers in the column are counted. Blanks, logical values, and text are ignored. GEOMEAN( Table[Column] ) is equivalent to GEOMEANX( Table, Table[Column] ) This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.