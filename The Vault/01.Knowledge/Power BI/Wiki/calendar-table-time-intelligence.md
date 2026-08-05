---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, calendar-table, time-intelligence, data-modeling]
---

# Calendar Table for Time Intelligence

A dedicated date dimension table that enables time intelligence functions (TOTALYTD, SAMEPERIODLASTYEAR, TOTALMTD, etc.) and supports drill-down by Year → Quarter → Month → Week.

## Purpose

Power BI's time intelligence DAX functions require a contiguous date table marked as a date table. Without it, YTD, YoY, and period-over-period comparisons are impossible or unreliable.

## Components

- **Date dimension table** (`Calendar`) with one row per date
- **Columns**: Date, Year, Quarter Number, Quarter Name, Month Number, Month Name, Week Number, Day of Week, Fiscal Year, Fiscal Quarter
- **Mark as Date Table** on the Calendar table (Table Tools → Mark as Date Table)
- **Relationship** to the fact table on Date → Order Date

## Structure (M Query via Power Query)

```m
let
    StartDate = #date(2020, 1, 1),
    EndDate   = #date(2026, 12, 31),
    DateCount = Duration.Days(EndDate - StartDate) + 1,
    Dates     = List.Dates(StartDate, DateCount, #duration(1, 0, 0, 0)),
    Table     = Table.FromList(Dates, Splitter.SplitByNothing(), {"Date"}),
    #"Changed Type" = Table.TransformColumnTypes(Table, {{"Date", type date}}),
    #"Year Added"    = Table.AddColumn(#"Changed Type", "Year",
        each Date.Year([Date]), Int64.Type),
    #"Quarter Added" = Table.AddColumn(#"Year Added", "Quarter",
        each "Q" & Number.ToText(Date.QuarterOfYear([Date])), type text),
    #"Month Added"   = Table.AddColumn(#"Quarter Added", "Month Name",
        each Date.MonthName([Date]), type text),
    #"Month Num"     = Table.AddColumn(#"Month Added", "Month Number",
        each Date.Month([Date]), Int64.Type)
in
    #"Month Num"
```

## Notes

- Use M (Power Query) to generate the Calendar table — never build it manually.
- The table must cover all dates in the fact table, plus a buffer (e.g., 1 year before and after).
- `Mark as Date Table` is required for time intelligence functions to work correctly.
- For fiscal year calendars that don't align with calendar years, add a `Fiscal Year` column and use it in the axis instead of the calendar year.

## Related

- [[sales-trend-line-chart]] — `pattern`
- [[calendar]] — `function` (in Power Query KB)
