---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: reference
tags: [dax, power-query, reference, date-table, comparison]
---

# DAX vs M Date Table Quick Reference

Side-by-side comparison of the two primary approaches for building a Date Table in Power BI.

## Quick Reference

| Aspect | DAX | Power Query (M) |
|--------|-----|----------------|
| Location | Data model (calculated table) | Power Query (ETL layer) |
| Build speed | Fastest | Slower |
| Dynamic range | Requires MIN/MAX variables | Native via List.Min / List.Max |
| Calendar columns | ADDCOLUMNS inline | AddColumn chain |
| Auto-refresh | Recalculates on model refresh | Refreshes with data pipeline |
| Best for | Quick prototyping, static ranges | Production models, complex calendar logic |
| Requires Mark as Date Table | Yes | Yes |
| Supports fiscal year | Via calculated column | Native in M |
| Hidden auto date/time conflict | Yes — must disable | Yes — must disable |

## DAX Approach

```dax
DimDate =
ADDCOLUMNS (
    CALENDAR ( DATE(2018,1,1), DATE(2026,12,31) ),
    "Year",         YEAR ( [Date] ),
    "MonthNum",     MONTH ( [Date] ),
    "MonthName",    FORMAT ( [Date], "MMMM" ),
    "Quarter",      "Q" & FORMAT ( [Date], "Q" )
)
```

## Power Query (M) Approach

```m
let
    Source    = FactSales,
    StartDate = Date.From(List.Min(Source[OrderDate])),
    EndDate   = Date.EndOfYear(Date.From(List.Max(Source[OrderDate]))),
    Days      = Duration.Days(EndDate - StartDate) + 1,
    Dates     = List.Dates(StartDate, Days, #duration(1, 0, 0, 0)),
    Table     = Table.FromList(Dates, Splitter.SplitByNothing(), {"Date"}),
    Typed     = Table.TransformColumnTypes(Table, {{"Date", type date}}),
    AddYear   = Table.AddColumn(Typed, "Year",
                 each Date.Year([Date]), Int64.Type),
    AddMonthN = Table.AddColumn(AddYear, "MonthNum",
                 each Date.Month([Date]), Int64.Type)
in
    AddMonthN
```

## Recommendation

Use **Power Query** for production models — it is self-maintaining, keeps logic in the ETL layer where it belongs, and adapts automatically when the fact table's date range changes.

Use **DAX** for quick prototypes, simple static ranges, or when the model is built primarily in DAX without Power Query.

## Related

- [[calendar-dax]] — `function`
- [[calendarauto-dax]] — `function`
- [[list-dates-m]] — `function`
- [[list-min-m]] — `function`
- [[list-max-m]] — `function`
- [[power-query-date-table-build]] — `pattern`
- [[dax-date-table-build]] — `pattern`
