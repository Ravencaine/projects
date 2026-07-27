---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# STDEVX.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of the entire population.

## Syntax

```dax
STDEVX.P(<table>, <expression>)
```

## Remarks

STDEVX.P evaluates expression for each row of table and returns the standard deviation of expression assuming that table refers to the entire population. If the data in table represents a sample of the population, you should compute the standard deviation by using STDEVX.S instead. STDEVX.P uses the following formula: √[∑(x - x̃)2/n]