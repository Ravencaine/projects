---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# VAR.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of the entire population.

## Syntax

```dax
VAR.P(<columnName>)
```

## Remarks

VAR.P assumes that the column refers the entire population. If your data represents a sample of the population, then compute the variance by using VAR.S. VAR.P uses the following formula: ∑(x - x̃)2/n where x̃ is the average value of x for the entire population and n is the population size