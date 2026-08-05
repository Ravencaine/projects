---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# COUNTA

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of rows in the specified column that contain non-blank values.

## Syntax

```dax
COUNTA(<column>)
```

## Remarks

When the function does not find any rows to count, the function returns a blank. Unlike COUNT, COUNTA supports Boolean data type. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.