---
created: 2026-08-02
updated: 2026-08-03
source: Power BI Time Hacks: Mastering Dynamic Date Views
note_type: pattern
tags: [power-query, pattern, calendar-table, date, weekly, monthly]
---

# Calendar Table in Power Query: Daily + Weekly + Monthly Columns

Power Query M-code to build a date table with three granularities as separate columns.

```m
let
    GetMinDate = Date.StartOfMonth(List.Min(#"Asset Data"[Date])),
    GetMaxDate = Date.EndOfMonth(List.Max(#"Asset Data"[Date])),
    Source = #table({"MinDate", "MaxDate"}, {{GetMinDate, GetMaxDate}}),
    AddDateColumn = Table.AddColumn(Source, "Daily", each {Number.From([MinDate])..Number.From([MaxDate])}),
    ExpandDates = Table.ExpandListColumn(AddDateColumn, "Daily"),
    SelectColumns = Table.SelectColumns(ExpandDates, {"Daily"}),
    ChangeType = Table.TransformColumnTypes(SelectColumns,{{"Daily", type date}}),
    AddMonthlyColumn = Table.AddColumn(ChangeType, "Monthly", each Date.StartOfMonth([Daily]), type date),
    AddWeeklyColumn = Table.AddColumn(AddMonthlyColumn, "Weekly", each Date.StartOfWeek([Daily]), type date)
in
    AddWeeklyColumn
```

**Three columns:**

- `Daily` — each date in the range (type `date`)
- `Weekly` — `Date.StartOfWeek([Daily])` (first day of week per system locale)
- `Monthly` — `Date.StartOfMonth([Daily])` (first day of month)

These columns become the axis fields in a field parameter for dynamic granularity switching. Use `Date.StartOfMonth` on the asset data min/max to ensure the calendar spans full months.
