---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# STDEVX.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of a sample population.

## Syntax

```dax
STDEVX.S(<table>, <expression>)
```

## Remarks

STDEVX.S evaluates expression for each row of table and returns the standard deviation of expression assuming that table refers to a sample of the population. If table represents the entire population, then compute the standard deviation by using STDEVX.P.