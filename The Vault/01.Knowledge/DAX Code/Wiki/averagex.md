---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# AVERAGEX

Applies to: Calculated column Calculated table Measure Visual calculation Calculates the average (arithmetic mean) of a set of expressions evaluated over a table.

## Syntax

```dax
AVERAGEX(<table>,<expression>)
```

## Remarks

The AVERAGEX function enables you to evaluate expressions for each row of a table, and then take the resulting set of values and calculate its arithmetic mean. Therefore, the function takes a table as its first argument, and an expression as the second argument. In all other respects, AVERAGEX follows the same rules as AVERAGE. You cannot include non-numeric or null cells. Both the table and expression arguments are required.