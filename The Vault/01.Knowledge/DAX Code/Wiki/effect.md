---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, financial]
---

# EFFECT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the effective annual interest rate, given the nominal annual interest rate and the

## Syntax

```dax
EFFECT(<nominal_rate>, <npery>)
```

## Remarks

EFFECT is calculated as follows: nominal_rate npery EFFECT = (1 + ) − 1 npery npery is rounded to the nearest integer. An error is returned if: nominal_rate ≤ 0.