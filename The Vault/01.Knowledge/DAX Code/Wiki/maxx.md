---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MAXX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the highest value that results from evaluating an expression for each row of a

## Syntax

```dax
MAXX(<table>,<expression>,[<variant>])
```

## Remarks

The table argument to the MAXX function can be a table name or an expression that evaluates to a table. The second argument indicates the expression to be evaluated for each row of the table. Of the values to evaluate, only the following are counted: Numbers