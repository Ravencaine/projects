---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# VAR.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of a sample population.

## Syntax

```dax
VAR.S(<columnName>)
```

## Remarks

VAR.S assumes that the column refers to a sample of the population. If your data represents the entire population, then compute the variance by using VAR.P. VAR.S uses the following formula: ∑(x - x̃)2/(n-1) where x̃ is the average value of x for the sample population and n is the population size