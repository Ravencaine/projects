---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# PRODUCTX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the product of an expression evaluated for each row in a table.

## Syntax

```dax
PRODUCTX(<table>, <expression>)
```

## Remarks

To return the product of the numbers in a column, use PRODUCT. The PRODUCTX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the product, or an expression that evaluates to a column. Only the numbers in the column are counted. Blanks, logical values, and text are ignored.