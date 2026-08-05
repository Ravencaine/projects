---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [power-query, calendar-table, date-dimension, M-code]
related: [Date.StartOfMonth, Date.EndOfMonth, DATESINPERIOD]
---

# Build a Calendar/Date Table (Power Query)

Create a dedicated date dimension table in Power Query. Used to support time intelligence functions, date hierarchies, and cross-filtering in Power BI.

## Pattern

```m
= let
    Source = List.Dates(
        #date(2020, 1, 1),
        Duration.Days(#date(2030, 12, 31) - #date(2020, 1, 1)) + 1,
        #duration(1, 0, 0, 0)
    ),
    TableFromList = Table.FromList(Source, Splitter.SplitByNothing(), {"Date"}),
    ChangedType = Table.TransformColumnTypes(TableFromList, {{"Date", type date}}),

    // Add Year column
    YearColumn = Table.AddColumn(ChangedType, "Year", each Date.Year([Date]), Int64.Type),

    // Add Month column
    MonthColumn = Table.AddColumn(YearColumn, "Month Number", each Date.Month([Date]), Int64.Type),

    // Add Month Name
    MonthNameColumn = Table.AddColumn(MonthColumn, "Month", each Date.MonthName([Date]), type text),

    // Add Start of Month (used for DAX time intelligence)
    StartOfMonthColumn = Table.AddColumn(MonthNameColumn, "Start of Month", each Date.StartOfMonth([Date]), type date),

    // Add End of Month
    EndOfMonthColumn = Table.AddColumn(StartOfMonthColumn, "End of Month", each Date.EndOfMonth([Date]), type date),

    // Add Quarter
    QuarterColumn = Table.AddColumn(EndOfMonthColumn, "Quarter", each "Q" & Number.ToText(Date.QuarterOfYear([Date])), type text),

    // Select only needed columns
    FinalTable = Table.SelectColumns(
        QuarterColumn,
        {"Date", "Year", "Month Number", "Month", "Start of Month", "End of Month", "Quarter"}
    )
in
    FinalTable
```

## Key M Functions Used

| Function | Purpose |
|----------|---------|
| `List.Dates` | Generate a list of dates from start to end |
| `Table.AddColumn` | Add a calculated column |
| `Date.StartOfMonth` | Return the first day of the month |
| `Date.EndOfMonth` | Return the last day of the month |
| `Table.SelectColumns` | Keep only the columns needed |
| `Date.Year`, `Date.Month`, `Date.QuarterOfYear` | Extract date parts |
| `Date.MonthName` | Human-readable month name |

## Notes

- Bittar uses this pattern to build calendar tables that feed DAX time intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, etc.).
- `Date.StartOfMonth` and `Date.EndOfMonth` are used to create anchor columns that make DAX time intelligence calculations deterministic.
- Always mark the `Date` column as a date type and configure it as a date hierarchy or role-playing dimension in the model.
- For fiscal calendars, replace the `Date.Month` / `Date.QuarterOfYear` extraction with fiscal equivalents.

## Related

- [[startofmonth]] — M function, first day of month
- [[endofmonth]] — M function, last day of month
- [[addcolumns]] — add calculated columns
- [[selectcolumns]] — remove unneeded columns
- [[totalytd]] — DAX time intelligence using this table
