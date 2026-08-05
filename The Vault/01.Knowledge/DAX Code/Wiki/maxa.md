---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MAXA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the largest value in a column.

## Syntax

```dax
MAXA(<column>)
```

## Remarks

The MAXA function takes as argument a column, and looks for the largest value among the following types of values: Numbers Dates Logical values, such as TRUE and FALSE. Rows that evaluate to TRUE count as 1; rows that evaluate to FALSE count as 0 (zero). Empty cells are ignored. If the column contains no values that can be used, MAXA returns 0 (zero). If you want to compare text values, use the MAX function.