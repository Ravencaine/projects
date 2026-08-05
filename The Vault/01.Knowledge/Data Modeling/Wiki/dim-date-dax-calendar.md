---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: reference
tags: [date-table, dim-date, dax, calendar, power-bi]
---

# dim_date DAX (CALENDAR + ADDCOLUMNS)

A reusable DAX expression for building a complete date dimension table in Power BI — replacing the auto-generated date hierarchies with a single, controllable dim_date table.

## Quick Reference

```dax
dim_date =
VAR StartDate = DATE(2020, 1, 1)
VAR EndDate   = DATE(2030, 12, 31)
RETURN
    ADDCOLUMNS (
        CALENDAR ( StartDate, EndDate ),
        "DateKey",        INT ( FORMAT ( [Date], "YYYYMMDD" ) ),
        "FullDate",       [Date],
        "Year",           YEAR ( [Date] ),
        "QuarterNum",     QUARTER ( [Date] ),
        "Quarter",        "Q" & QUARTER ( [Date] ),
        "MonthNum",       MONTH ( [Date] ),
        "MonthName",      FORMAT ( [Date], "MMMM" ),
        "MonthShort",     FORMAT ( [Date], "MMM" ),
        "WeekNum",        WEEKNUM ( [Date] ),
        "DayOfWeekNum",   WEEKDAY ( [Date], 1 ),
        "DayOfWeekName",  FORMAT ( [Date], "DDDD" ),
        "IsWeekend",      IF ( WEEKDAY ( [Date], 2 ) > 5, "Weekend", "Weekday" )
    )
```

## Columns Added

| Column | Description |
|--------|-------------|
| DateKey | Integer YYYYMMDD — surrogate join key |
| FullDate | The date value itself |
| Year | Calendar year |
| QuarterNum | 1–4 |
| Quarter | "Q1", "Q2", etc. |
| MonthNum | 1–12 |
| MonthName | Full month name (January, etc.) |
| MonthShort | Abbreviated (Jan, etc.) |
| WeekNum | ISO week number |
| DayOfWeekNum | 1 (Monday) – 7 (Sunday) |
| DayOfWeekName | Day name |
| IsWeekend | Weekend / Weekday flag |

## Why Not Auto-Generated Date Hierarchy?

- Auto-generated dates create hidden tables per column — one per date column used
- dim_date consolidates to one table; all date columns join to it
- Enables custom columns: IsHoliday, FinanceCloseDate, FiscalYearStart, etc.
- Required for correct time intelligence function behaviour

## Related

- [[totalmtd]], [[totalytd]], [[sameperiodlastyear]] — time intelligence functions requiring a date table
- [[time-intelligence-quick-reference-retail-analytics]] — time intel function reference
