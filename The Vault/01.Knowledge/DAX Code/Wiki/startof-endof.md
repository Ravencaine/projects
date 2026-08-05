---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# STARTOF / ENDOF: Week, Month, Quarter, Year

Return the first or last date of the current context period.

## STARTOF Functions

```dax
STARTOFWEEK(<calendar>)
STARTOFMONTH(<dates or calendar>)
STARTOFQUARTER(<dates or calendar>)
STARTOFYEAR(<dates or calendar>[, <year_end_date>])
```

Return the first date of the period in the current context.

## ENDOF Functions

```dax
ENDOFWEEK(<calendar>)
ENDOFMONTH(<dates or calendar>)
ENDOFQUARTER(<dates or calendar>)
ENDOFYEAR(<dates or calendar>[, <year_end_date>])
```

Return the last date of the period in the current context.

## Examples

```dax
-- First date of current month
Start of Month = STARTOFMONTH('Date'[Date])

-- Last date of current month
End of Month = ENDOFMONTH('Date'[Date])

-- First day of fiscal year (ending June 30)
FY Start = STARTOFYEAR('Date'[Date], "06/30")
```

## Notes

- STARTOF/ENDOF WEEK require a calendar (ISO week date tables)
- STARTOFYEAR and ENDOFYEAR accept `year_end_date` for fiscal years
- For simple "last day of month", EOMONTH is often more readable
- Discouraged in visual calculations
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[eomonth]]
- [[openingbalance]]
- [[closingbalance]]
