---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# RAND

Applies to: Calculated column Calculated table Measure Visual calculation Returns a random number greater than or equal to 0 and less than 1, evenly distributed.

## Syntax

```dax
RAND()
```

## Remarks

Recalculation depends on various factors, including whether the model is set to Manual or Automatic recalculation mode, and whether data has been refreshed. RAND and other volatile functions that do not have fixed values are not always recalculated. For