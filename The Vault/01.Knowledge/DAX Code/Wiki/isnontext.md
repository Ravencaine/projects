---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# ISNONTEXT

Applies to: Calculated column Calculated table Measure Visual calculation Checks if a value is not text (blank cells are not text), and returns TRUE or FALSE.

## Syntax

```dax
ISNONTEXT(<value>)
```

## Remarks

An empty string is considered text. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.