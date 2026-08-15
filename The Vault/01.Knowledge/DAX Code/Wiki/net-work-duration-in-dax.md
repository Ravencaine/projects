---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, duration, business-hours, work-duration]
note_type: pattern

---

# Net Work Duration in DAX

Calculating the time between two timestamps excluding non-working hours.

## Pattern

```dax
Net Work Hours :=
VAR __Start = [StartDateTime]
VAR __End = [EndDateTime]
VAR __TotalHours = ( __End - __Start ) * 24
VAR __WorkHoursPerDay = 8
VAR __WorkingDays = TRUNC( DIVIDE( __TotalHours, 24 ) )
VAR __RemainingHours = MOD( __TotalHours, 24 )
RETURN
__WorkingDays * __WorkHoursPerDay
    + MIN( __RemainingHours, __WorkHoursPerDay )
```

## Notes

- For complex business hours (shifts, holidays), use a dedicated calendar table
- Excel-style NETWORKDAYS equivalent: COUNTROWS( FILTER( date_table, is_workday ) )

## Related

- [[duration-calculations-in-dax]]
- [[hours-breakdown-in-dax]]
