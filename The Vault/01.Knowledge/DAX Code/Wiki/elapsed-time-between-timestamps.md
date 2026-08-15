---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, date-time, duration, datediff]
note_type: pattern

---

# Elapsed Time Between Timestamps

Calculating the exact elapsed time between two datetime values in DAX.

## Basic Elapsed Time

```dax
Elapsed Days := DATEDIFF( [StartDate], [EndDate], DAY )
Elapsed Hours := DATEDIFF( [StartTime], [EndTime], HOUR )
Elapsed Minutes := DATEDIFF( [StartTime], [EndTime], MINUTE )
```

## Including Fractional Units

```dax
Elapsed Days (Decimal) := [EndDateTime] - [StartDateTime]
Elapsed Hours (Decimal) := ( [EndDateTime] - [StartDateTime] ) * 24
Elapsed Minutes (Decimal) := ( [EndDateTime] - [StartDateTime] ) * 1440
```

## Notes

- `DATEDIFF()` returns whole units only (no fractions)
- Use decimal subtraction for precise elapsed time
- `NOW()` returns the current datetime — useful for "time since" calculations

## Related

- [[duration-calculations-in-dax]]
- [[duration]]
- [[time-tables-in-dax]]
