---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# AVERAGEA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the average (arithmetic mean) of the values in a column. Handles text and non-

## Syntax

```dax
AVERAGEA(<column>)
```

## Remarks

The AVERAGEA function takes a column and averages the numbers in it, but also handles non-numeric data types according to the following rules: Values that evaluates to TRUE count as 1. Values that evaluate to FALSE count as 0 (zero). Values that contain non-numeric text count as 0 (zero). Empty text ("") counts as 0 (zero). If you do not want to include logical values and text representations of numbers in a reference as part of the calculation, use the AVERAGE function.