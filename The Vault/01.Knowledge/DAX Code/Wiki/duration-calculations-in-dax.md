---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "time", "duration", "date-time"]
note_type: pattern

---

# Duration Calculations in DAX (No Native Duration)

DAX has no native duration data type. Durations are computed by subtracting datetime values and converting the result to the desired unit.

## Purpose

When you need the elapsed time between two timestamps — in seconds, minutes, hours, or days — you subtract the start from the end and convert.

## Core Formula

```dax
Duration in Days := [EndDateTime] - [StartDateTime]
-- Returns a decimal fraction of a day
-- 0.5 = 12 hours, 1.0 = 24 hours

Duration in Hours := ( [EndDateTime] - [StartDateTime] ) * 24
Duration in Minutes := ( [EndDateTime] - [StartDateTime] ) * 1440
Duration in Seconds := ( [EndDateTime] - [StartDateTime] ) * 86400
```

## Practical Pattern

```dax
Duration (Hours) :=
VAR __Start = [StartTime]
VAR __End = [EndTime]
RETURN
DATEDIFF( __Start, __End, HOUR )
```

## Common Duration Scenarios

| Scenario | Formula |
|----------|---------|
| Days between dates | `DATEDIFF( Start, End, DAY )` |
| Business days | Custom — exclude weekends and holidays |
| Elapsed seconds | `(End - Start) * 86400` |
| Elapsed minutes | `(End - Start) * 1440` |

## Notes

- `DATEDIFF()` is cleaner for whole-unit differences
- Decimal subtraction (`End - Start`) gives fractional units
- 1 day = 86400 seconds, 1 hour = 3600 seconds, 1 minute = 60 seconds

## Related

- [[elapsed-time-between-timestamps]]
- [[duration]]
- [[time-tables-in-dax]]
