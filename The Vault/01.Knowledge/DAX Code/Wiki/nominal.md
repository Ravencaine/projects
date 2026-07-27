---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# NOMINAL

Applies to: Calculated column Calculated table Measure Visual calculation Returns the nominal annual interest rate, given the effective rate and the number of

## Syntax

```dax
NOMINAL(<effect_rate>, <npery>)
```

## Remarks

The relationship between NOMINAL and EFFECT is shown in the following equation: nominal_rate npery EFFECT = (1 + ) − 1 npery npery is rounded to the nearest integer. An error is returned if: effect_rate ≤ 0.