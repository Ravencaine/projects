---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# HASONEFILTER

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the number of directly filtered values on columnName is one;

## Syntax

```dax
HASONEFILTER(<columnName>)
```

## Remarks

This function is similar to HASONEVALUE() with the difference that HASONEVALUE() works based on cross-filters while HASONEFILTER() works by a direct filter. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.