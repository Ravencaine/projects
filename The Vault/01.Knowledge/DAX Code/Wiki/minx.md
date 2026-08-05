---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# MINX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the lowest value that results from evaluating an expression for each row of a

## Syntax

```dax
MINX(<table>, < expression>,[<variant>])
```

## Return Value

a table. The second argument contains the expression that is evaluated for each row of the table. Blank values are skipped. TRUE/FALSE values are not supported.

## Remarks

The MINX function takes as its first argument a table or an expression that returns a table. The second argument contains the expression that is evaluated for each row of the table. Blank values are skipped. TRUE/FALSE values are not supported.