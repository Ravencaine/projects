---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: pattern
tags: [power-bi, pattern, date-table, dax, data-modeling]
---

# DAX Date Table Build

A Date Table created using DAX functions (`CALENDAR` or `CALENDARAUTO`) inside the data model, with calendar columns added via `ADDCOLUMNS`. Fastest approach for static or simple date ranges.

## Purpose

Provides an alternative to Power Query for teams that prefer to keep dimension logic in the model layer. Suitable for static date ranges or when the model is built primarily in DAX.

## Components

- `CALENDAR` or `CALENDARAUTO` to generate the date series
- `ADDCOLUMNS` to add Year, MonthNum, MonthName, Quarter, YearMonth
- Sort-by-column settings for MonthName and DayName

## DAX Code

```dax
-- Simple CALENDAR (static range):
DimDate =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2018, 1, 1 ), DATE ( 2026, 12, 31 ) ),
    "Year",         YEAR ( [Date] ),
    "MonthNum",     MONTH ( [Date] ),
    "MonthName",    FORMAT ( [Date], "MMMM" ),
    "MonthShort",   FORMAT ( [Date], "MMM" ),
    "Quarter",      "Q" & FORMAT ( [Date], "Q" ),
    "YearQuarter",  FORMAT ( [Date], "YYYY" ) & "-Q" & FORMAT ( [Date], "Q" ),
    "YearMonth",    FORMAT ( [Date], "YYYY" ) & "-" & FORMAT ( [Date], "MM" ),
    "YearMonthKey", VALUE ( FORMAT ( [Date], "YYYYMM" ) ),
    "DayOfWeekNum", WEEKDAY ( [Date], 2 )
)

-- Dynamic CALENDAR (from fact table):
DimDate =
VAR MinDate = MIN ( FactSales[OrderDate] )
VAR MaxDate = DATE ( YEAR ( MAX ( FactSales[OrderDate] ) ), 12, 31 )
RETURN
    ADDCOLUMNS (
        CALENDAR ( MinDate, MaxDate ),
        "Year",         YEAR ( [Date] ),
        "MonthNum",     MONTH ( [Date] ),
        "MonthName",    FORMAT ( [Date], "MMMM" ),
        "Quarter",      "Q" & FORMAT ( [Date], "Q" ),
        "YearMonth",    FORMAT ( [Date], "YYYY" ) & "-" & FORMAT ( [Date], "MM" )
    )

-- CALENDARAUTO (simplest option):
DimDate = CALENDARAUTO()
```

## Post-Load Steps

1. Mark as Date Table: Table Tools → Mark as Date Table → select `Date` column
2. Set Sort by Column: `MonthName` → `MonthNum`, `DayName` → `DayOfWeekNum`
3. Build relationships: drag fact table date columns to `DimDate[Date]`

## Related

- [[calendar-dax]] — `function`
- [[calendarauto-dax]] — `function`
- [[power-query-date-table-build]] — `pattern`
- [[dax-vs-m-date-table-quick-reference]] — `reference`
