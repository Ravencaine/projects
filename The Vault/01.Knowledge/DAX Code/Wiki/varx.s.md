---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# VARX.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of a sample population.

## Syntax

```dax
VARX.S(<table>, <expression>)
```

## Remarks

VARX.S evaluates expression for each row of table and returns the variance of expression; on the assumption that table refers to a sample of the population. If table represents the entire population, then you should compute the variance by using VARX.P. VAR.S uses the following formula: ∑(x - x̃)2/(n-1)