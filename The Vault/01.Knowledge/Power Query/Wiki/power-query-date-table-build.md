---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: pattern
tags: [power-query, pattern, date-table, m, time-intelligence]
---

# Power Query Date Table Build

A self-maintaining Date Table built in Power Query using M functions. Automatically adapts to the date range in the source data — no manual updates required.

## Purpose

Creates a `DimDate` dimension table inside Power Query that reads the actual date range from the fact table and generates a complete, gapless date series with all required calendar columns.

## Components

- Reference to the fact table (`FactSales`)
- Dynamic start/end dates via `List.Min()` and `List.Max()`
- Date series generation via `List.Dates()`
- Column type conversion to `type date`
- Calendar columns: Year, MonthNum, MonthName, Quarter, YearMonth, YearMonthKey
- Additional columns: Day of Week, IsWeekend, FiscalYear, FiscalQuarter (as needed)

## M Code

```m
let
    // Reference your fact table
    Source = FactSales,

    // Dynamic date range from source data
    StartDate = Date.From(List.Min(Source[OrderDate])),
    EndDate   = Date.EndOfYear(Date.From(List.Max(Source[OrderDate]))),
    Days      = Duration.Days(EndDate - StartDate) + 1,

    // Generate date series
    Dates = List.Dates(StartDate, Days, #duration(1, 0, 0, 0)),

    // Convert list to table
    Table = Table.FromList(Dates, Splitter.SplitByNothing(), {"Date"}),

    // Set correct type
    Typed = Table.TransformColumnTypes(Table, {{"Date", type date}}),

    // Add calendar columns
    AddYear    = Table.AddColumn(Typed, "Year",
                  each Date.Year([Date]), Int64.Type),
    AddMonthN  = Table.AddColumn(AddYear, "MonthNum",
                  each Date.Month([Date]), Int64.Type),
    AddMonthNm = Table.AddColumn(AddMonthN, "MonthName",
                  each Date.MonthName([Date]), type text),
    AddQtr     = Table.AddColumn(AddMonthNm, "Quarter",
                  each "Q" & Text.From(Date.QuarterOfYear([Date])), type text),
    AddYM      = Table.AddColumn(AddQtr, "YearMonth",
                  each Text.From([Year]) & "-" &
                       Text.PadStart(Text.From([MonthNum]), 2, "0"), type text),
    AddYMKey   = Table.AddColumn(AddYM, "YearMonthKey",
                  each [Year] * 100 + [MonthNum], Int64.Type)
in
    AddYMKey
```

## Steps

1. Open Power Query Editor → Transform Data
2. New Source → Blank Query
3. Open Advanced Editor → paste M code (replace `FactSales` and `OrderDate` with your actual names)
4. Add additional calendar columns as needed (DayOfWeek, IsWeekend, FiscalYear)
5. Rename the query to `DimDate`
6. Close & Apply

## Post-Load Steps

1. Mark as Date Table: Table Tools → Mark as Date Table → select `Date` column
2. Set Sort by Column: `MonthName` → `MonthNum`, `MonthShort` → `MonthNum`, `DayName` → `DayOfWeekNum`
3. Disable Auto date/time: File → Options → Data Load → uncheck Auto date/time

## Related

- [[list-dates-m]] — `function`
- [[list-min-m]] — `function`
- [[list-max-m]] — `function`
- [[calendar-dax]] — `function`
- [[calendarauto-dax]] — `function`
- [[dax-vs-m-date-table-quick-reference]] — `reference`
- [[calendar-table-time-intelligence]] — `pattern` (Power BI KB)
