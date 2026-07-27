---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# COUNT

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of rows in the specified column that contain non-blank values.

## Syntax

```dax
COUNT(<column>)
```

## Remarks

The only argument allowed to this function is a column. The COUNT function counts rows that contain the following kinds of values: Numbers Dates Strings When the function finds no rows to count, it returns a blank. Blank values are skipped. TRUE/FALSE values are not supported. If you want to evaluate a column of TRUE/FALSE values, use the COUNTA function.