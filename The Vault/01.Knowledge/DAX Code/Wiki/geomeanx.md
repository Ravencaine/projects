---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# GEOMEANX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the geometric mean of an expression evaluated for each row in a table.

## Syntax

```dax
GEOMEANX(<table>, <expression>)
```

## Remarks

The GEOMEANX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the geometric mean, or an expression that evaluates to a column. Only the numbers in the column are counted. Blanks, logical values, and text are ignored.