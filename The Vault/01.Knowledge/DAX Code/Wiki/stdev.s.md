---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# STDEV.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of a sample population.

## Syntax

```dax
STDEV.S(<ColumnName>)
```

## Remarks

STDEV.S assumes that the column refers to a sample of the population. If your data represents the entire population, then compute the standard deviation by using STDEV.P. STDEV.S uses the following formula: √[∑(x - x̃)2/(n-1)]