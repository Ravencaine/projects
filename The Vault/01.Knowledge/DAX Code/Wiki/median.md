---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MEDIAN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the median of numbers in a column.

## Syntax

```dax
MEDIAN(<column>)
```

## Remarks

Only the numbers in the column are counted. Blanks are ignored. Logical values, dates, and text are not supported. MEDIAN( Table[Column] ) is equivalent to MEDIANX( Table, Table[Column] ). This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.