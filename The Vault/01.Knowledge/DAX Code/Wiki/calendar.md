---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# CALENDAR

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table with a single column named "Date" that contains a contiguous set of

## Syntax

```dax
CALENDAR(<start_date>, <end_date>)
```

## Remarks

An error is returned if start_date is greater than end_date. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.