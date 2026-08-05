---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, parent-child]
---

# PATHCONTAINS

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE if the specified item exists within the specified path.

## Syntax

```dax
PATHCONTAINS(<path>, <item>)
```

## Remarks

If item is an integer number it is converted to text and then the function is evaluated. If conversion fails then the function returns an error. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.