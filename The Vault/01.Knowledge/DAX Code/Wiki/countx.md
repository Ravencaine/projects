---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# COUNTX

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of rows that contain a non-blank value or an expression that

## Syntax

```dax
COUNTX(<table>,<expression>)
```

## Remarks

The COUNTX function takes two arguments. The first argument must always be a table, or any expression that returns a table. The second argument is the column or expression that is searched by COUNTX. The COUNTX function counts only values, dates, or strings. If the function finds no rows to count, it returns a blank. If you want to count logical values, use the COUNTAX function.