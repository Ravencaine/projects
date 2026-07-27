---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# CONFIDENCE.T

Applies to: Calculated column Calculated table Measure Visual calculation Returns the confidence interval for a population mean, using a Student's t distribution.

## Syntax

```dax
CONFIDENCE.T(alpha,standard_dev,size)
```

## Remarks

If any argument is nonnumeric, CONFIDENCE.T returns the #VALUE! error value. If alpha ≤ 0 or alpha ≥ 1, CONFIDENCE.T returns the #NUM! error value. If standard_dev ≤ 0, CONFIDENCE.T returns the #NUM! error value.