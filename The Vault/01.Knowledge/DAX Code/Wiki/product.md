---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# PRODUCT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the product of the numbers in a column.

## Syntax

```dax
PRODUCT(<column>)
```

## Remarks

To return the product of an expression evaluated for each row in a table, use PRODUCTX function. Only the numbers in the column are counted. Blanks, logical values, and text are ignored. For