---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "time", "duration", "time-table", "minutes"]
note_type: pattern

---

# Time Tables in DAX

Creating a time dimension table for minute-level or hour-level granularity.

## Purpose

Standard date tables work at the day level. Time tables enable reporting at sub-day granularity (hours, minutes).

## Hour Table

```dax
Time =
ADDCOLUMNS(
    CALENDAR( DATE( 2000, 1, 1 ), DATE( 2000, 1, 1 ) ),
    "Hour", HOUR( [Date] ),
    "Hour Label", FORMAT( [Date], "hh AM/PM" ),
    "Half Hour", INT( HOUR( [Date] ) / 0.5 ) * 0.5
)
```

## Minute Table (0-1439)

```dax
Minutes =
SELECTCOLUMNS(
    GENERATESERIES( 0, 1439 ),
    "Minute", [Value],
    "Hour", INT( [Value] / 60 ),
    "Minute of Hour", MOD( [Value], 60 ),
    "Label", FORMAT( TIME( INT([Value]/60), MOD([Value],60), 0 ), "hh:mm" )
)
```

## Notes

- For day-level analysis, the date table is sufficient
- Time tables are rarely needed in DAX — most time intelligence is at day level

## Related

- [[date-table-creation-in-dax]]
- [[duration-calculations-in-dax]]
