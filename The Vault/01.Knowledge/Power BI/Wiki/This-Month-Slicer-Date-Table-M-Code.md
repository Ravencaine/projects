---
created: 2026-08-10
updated: 2026-08-10
source: A Simple Trick to Always Display the Latest Month in Power BI (Even After Refresh)
source_url: https://medium.com/microsoft-power-bi/a-simple-trick-to-always-display-the-latest-month-in-power-bi-even-after-refresh-0630fef5e2f3
note_type: reference
tags: [powerbi, power-query, date-table, this-month, reference]
---

# This Month Slicer — Date Table M Code

Power Query M code for a fully dynamic date table that includes the "This Month" sticky slicer column. Min/max dates pull from the fact table so the calendar always covers the full range of available data — even after refresh.

## M Code

```m
let
    // Reference your fact table
    Source = Sales,

    // Get min and max dates from the fact
    MinDate = Date.StartOfMonth( List.Min( Source[Date] ) ),
    MaxDate = Date.EndOfMonth( List.Max( Source[Date] ) ),

    // Generate continuous date range
    DateList =
        List.Dates(
            MinDate,
            Duration.Days( MaxDate - MinDate ) + 1,
            #duration(1, 0, 0, 0)
        ),

    // Convert to table
    DateTable =
        Table.FromList(
            DateList,
            Splitter.SplitByNothing(),
            {"Date"},
            null,
            ExtraValues.Error
        ),

    // Change type
    ChangeType =
        Table.TransformColumnTypes(
            DateTable,
            {{"Date", type date}}
        ),

    // Add Year
    AddYear =
        Table.AddColumn(
            ChangeType,
            "Year",
            each Date.Year([Date]),
            Int64.Type
        ),

    // Add Month Number
    AddMonthNumber =
        Table.AddColumn(
            AddYear,
            "Month Number",
            each Date.Month([Date]),
            Int64.Type
        ),

    // Add First Day of Month
    AddFirstDayOfMonth =
        Table.AddColumn(
            AddMonthNumber,
            "First Day of Month",
            each Date.StartOfMonth([Date]),
            type date
        ),

    // Add Month + Year label (e.g. Jan 2026)
    AddMonthYear =
        Table.AddColumn(
            AddFirstDayOfMonth,
            "Month",
            each Date.ToText([Date], "MMM yyyy"),
            type text
        ),

    // Add "This Month" column
    AddThisMonthOrMonthYear =
        Table.AddColumn(
            AddMonthYear,
            "This Month",
            each
                if Date.StartOfMonth([Date])
                    = Date.StartOfMonth(Date.From(DateTime.LocalNow()))
                then "This Month"
                else [Month],
            type text
        )

in
    AddThisMonthOrMonthYear
```

## Key Columns

| Column | Type | Description |
|--------|------|-------------|
| `Date` | date | Daily date values |
| `Year` | integer | Year from Date |
| `Month Number` | integer | Month number (1–12) |
| `First Day of Month` | date | First day of the month for each row |
| `Month` | text | Formatted label, e.g. `"Jan 2026"` |
| `This Month` | text | `"This Month"` for current calendar month; `"MMM yyyy"` for all others |

## Dynamic Behaviour

- `MinDate` and `MaxDate` pull from the fact table — the calendar expands automatically as new data arrives
- `DateTime.LocalNow()` evaluates at refresh time — the "This Month" label moves forward with each refresh
- The slicer should be placed on the `This Month` column, with `"This Month"` pre-selected

## Related

- [[Sticky-Slicer-This-Month-Auto-Select]] — pattern overview and when to use this approach
