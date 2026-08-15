---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.RemoveMatchingRows

Removes all occurrences of the specified rows from the table. table: The table to search. rows: A list containing information about the rows to be removed. equationCriteria: (Optional) Specifies how equality is determined when comparing values. This parameter can be a key selector function, a comparer function, or a list of the columns in the table to use when comparing rows.

## Signature

```m
Table.RemoveMatchingRows(
table as table,
rows as list,
optional equationCriteria as any
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |
| rows | list | |
| optional equationCriteria | any | |

## Returns

table

### Example 1

Remove any rows where [a = 1] from the specified table.

```m
Table.RemoveMatchingRows(
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4],
[a = 1, b = 6]
}),
{[a = 1]},
"a"
)
```

// Output
```
Table.FromRecords({[a = 3, b = 4]})
```

### Example 2

Remove canceled orders, ignoring case.

```m
let
CurrentOrders = #table(type table[OrderID = number, Product = text, Quantity =
number],
{
{101, "Widget", 5},
{102, "Gadget", 3},
{103, "Widget", 5}
}),
CanceledOrders = {
[OrderID = 103, Product = "widget", Quantity = 5]
},
FilteredOrders = Table.RemoveMatchingRows(CurrentOrders, CanceledOrders,
Comparer.OrdinalIgnoreCase)
in
FilteredOrders
```

// Output
```
#table(type table[OrderID = number, Product = text, Quantity = number],
{
{101, "Widget", 5},
{102, "Gadget", 3}
})
```

### Example 3

Remove any maintenance tasks that fall on US holidays.

```m
let
MaintenanceSchedule = #table(type table [Task = text, Date = date],
{
{"HVAC Check", #date(2025, 7, 10)}, // Not a holiday
{"Window Washing", #date(2025, 9, 1)}, // Labor Day
{"Fire Drill", #date(2025, 9, 17)}, // Not a holiday
{"Light Bulb Replacement", #date(2025, 11, 27)} // Thanksgiving
}),
USHolidays = {
[Date = #date(2025, 1, 1)], // New Year's Day
[Date = #date(2025, 7, 4)], // Independence Day
[Date = #date(2025, 9, 1)], // Labor Day
[Date = #date(2025, 11, 27)], // Thanksgiving
[Date = #date(2025, 12, 25)] // Christmas
},
FilteredSchedule = Table.RemoveMatchingRows(
MaintenanceSchedule,
USHolidays,
{"Date"}
)
in
FilteredSchedule
```

// Output
```
#table(type table[Task = text, Date = date],
{
{"HVAC Check", #date(2025, 7, 10)},
{"Fire Drill", #date(2025, 9, 17)}
})
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

