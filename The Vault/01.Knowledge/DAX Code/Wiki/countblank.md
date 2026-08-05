---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# COUNTBLANK

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of blank cells in a column.

## Syntax

```dax
COUNTBLANK(<column>)
```

## Remarks

The only argument allowed to this function is a column. You can use columns containing any type of data, but only blank cells are counted. Cells that have the value zero (0) are not counted, as zero is considered a numeric value and not a blank. Whenever there are no rows to aggregate, the function returns a blank. However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns a zero if no rows are found that meet the conditions. In other words, if the COUNTBLANK function finds no blanks, the result will be zero, but if there are 