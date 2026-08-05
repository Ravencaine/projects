---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "time", "hours", "breakdown", "duration"]
note_type: pattern

---

# Hours Breakdown in DAX

Breaking elapsed time into component hours (business hours, overtime, etc.).

## Extract Hours from Duration

```dax
Hours Breakdown :=
VAR __TotalHours = ( [EndTime] - [StartTime] ) * 24
VAR __Hours   = TRUNC( __TotalHours )
VAR __Minutes = ( __TotalHours - __Hours ) * 60
VAR __Seconds = MOD( __Minutes, 1 ) * 60
RETURN
"Hours: " & __Hours & ", Minutes: " & TRUNC( __Minutes )
```

## Business Hours Only

```dax
Business Hours :=
VAR __Hours = ( [EndTime] - [StartTime] ) * 24
VAR __BusinessHoursPerDay = 8
RETURN
__Hours / 24 * __BusinessHoursPerDay
```

## Notes

- Use `TRUNC()` for hours since TRUNC(3.7) = 3 (not 4)
- For time-of-day tracking, use TIME() and MOD() functions

## Related

- [[duration-calculations-in-dax]]
- [[duration]]
