---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# STDEV.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of the entire population.

## Syntax

```dax
STDEV.P(<ColumnName>)
```

## Remarks

STDEV.P assumes that the column refers to the entire population. If your data represents a sample of the population, then compute the standard deviation by using STDEV.S. STDEV.P uses the following formula: √[∑(x - x̃)2/n] where x̃ is the average value of x for the entire population and n is the population size.