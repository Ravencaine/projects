---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MEDIANX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the median number of an expression evaluated for each row in a table.

## Syntax

```dax
MEDIANX(<table>, <expression>)
```

## Remarks

The MEDIANX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the median, or an expression that evaluates to a column. Only the numbers in the column are counted. Logical values and text are ignored.