---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# VARX.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of the entire population.

## Syntax

```dax
VARX.P(<table>, <expression>)
```

## Remarks

VARX.P evaluates <expression> for each row of <table> and returns the variance of <expression> assuming that <table> refers to the entire population.. If <table> represents a sample of the population, then compute the variance by using VARX.S. VARX.P uses the following formula: ∑(x - x̃)2/n