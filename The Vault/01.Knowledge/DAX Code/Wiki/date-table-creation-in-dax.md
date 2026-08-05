---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "date-table", "power-bi"]
note_type: pattern

---

# Date Table Creation in DAX

Creating a dedicated date dimension table in DAX using CALENDAR and ADDCOLUMNS.

## Purpose

Nearly every Power BI semantic model needs a date table for time intelligence. Building it in DAX is simpler than Power Query and keeps everything self-contained.

## Structure

```dax
Dates =
VAR __Calendar =
ADDCOLUMNS(
    CALENDAR( DATE( 2020, 1, 1 ), DATE( 2025, 12, 31 ) ),
    "Quarter",      QUARTER( [Date] ),
    "Month",        FORMAT( [Date], "mmmm" ),
    "MonthSort",    MONTH( [Date] ),
    "Year",         YEAR( [Date] )
)
RETURN
__Calendar
```

After creating the table, set the Sort by column for `Month` to `MonthSort`.

## Key Functions

- `CALENDAR(start, end)` — generates a single-column table of dates
- `ADDCOLUMNS(table, "Name", expression)` — adds calculated columns
- `FORMAT(date, "mmmm")` — returns full month name
- `MONTH(date)` / `QUARTER(date)` / `YEAR(date)` — extract date parts

## Notes

- Always mark the date table as a date table in the model properties
- Include a full range of dates covering all fact table dates
- Month sort column prevents alphabetical sorting (April before January)

## Related

- [[no-calculate-time-intelligence-pattern]]
- [[offset-based-date-calculations]]
- [[measure-tables-in-power-bi]]
