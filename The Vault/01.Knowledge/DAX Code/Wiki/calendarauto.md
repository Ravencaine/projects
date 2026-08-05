---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# CALENDARAUTO

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged for use in visual calculations as it likely returns meaningless

## Syntax

```dax
CALENDARAUTO([fiscal_year_end_month])
```

## Remarks

The date range is calculated as follows: The earliest date in the model which is not in a calculated column or calculated table is taken as the MinDate.