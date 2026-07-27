---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter]
---

# ALLCROSSFILTERED

Applies to: Calculated column Calculated table Measure Visual calculation Clear all filters which are applied to a table.

## Syntax

```dax
ALLCROSSFILTERED(<table>)
```

## Remarks

ALLCROSSFILTERED can only be used to clear filters but not to return a table. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.