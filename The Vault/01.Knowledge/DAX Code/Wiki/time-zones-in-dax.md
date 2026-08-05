---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "date-time", "time-zone", "utc", "offset"]
note_type: pattern

---

# Time Zones in DAX

Converting UTC timestamps to local time and handling multi-timezone reporting.

## UTC to Local Conversion

```dax
Local Time :=
[UTCTime] + TIME( [UTCOffsetHours], 0, 0 )
```

## Multi-timezone Table

```dax
Time Zone Offset =
SWITCH(
    TRUE(),
    [City] = "New York",  -5,
    [City] = "London",     0,
    [City] = "Tokyo",      9,
    [City] = "Sydney",    10,
    0
)
```

## Notes

- Always store data in UTC — convert to local time for display
- Daylight saving time requires a time zone dimension table, not a simple offset

## Related

- [[duration-calculations-in-dax]]
- [[time-tables-in-dax]]
