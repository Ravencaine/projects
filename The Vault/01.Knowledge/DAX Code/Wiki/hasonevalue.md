---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# HASONEVALUE

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the context for columnName has been filtered down to one distinct

## Syntax

```dax
HASONEVALUE(<columnName>)
```

## Remarks

An equivalent expression for HASONEVALUE() is COUNTROWS(VALUES(<columnName>)) = 1. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.