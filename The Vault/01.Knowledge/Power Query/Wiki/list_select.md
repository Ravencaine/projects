---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Select

Returns the values from the specified list that match the selection condition. list: The list to examine. selection: The function that determines the values to select.

## Signature

```m
List.Select(list as list, selection as function) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| selection | function | |

## Returns

list

### Example 1

Find the values in the list {1, -3, 4, 9, -2} that are greater than 0.

```m
List.Select({1, -3, 4, 9, -2}, each _ > 0)
```

// Output
```
{1, 4, 9}
```

### Example 2

Select dates from the list that fall on Saturday or Sunday.

```m
let
dates = {
#date(2025, 10, 20), // Monday
#date(2025, 10, 21), // Tuesday
#date(2025, 10, 25), // Saturday
#date(2025, 10, 26), // Sunday
#date(2025, 10, 27) // Monday
},
weekendDates = List.Select(
dates,
each Date.DayOfWeek(_, Day.Monday) >= 5
)
in
weekendDates
```

// Output
```
{
#date(2025, 10, 25),
#date(2025, 10, 26)
}
```

### Example 3

Display a table of active customers with purchase totals over $100.

```m
let
customers = {
[Name = "Alice", Status = "Active", Purchases = 150],
[Name = "Bob", Status = "Inactive", Purchases = 200],
[Name = "Carol", Status = "Active", Purchases = 90],
[Name = "Dave", Status = "Active", Purchases = 120]
},
highValueActiveCustomers = List.Select(
customers,
each [Status] = "Active" and [Purchases] > 100
),
resultTable = Table.FromRecords(
highValueActiveCustomers,
type table [Name = text, Status = text, Purchases = number]
)
in
resultTable
```

// Output
```
#table(type table[Name = text, Status = text, Purchases = number],
{
{"Alice", "Active", 150},
{"Dave", "Active", 120}
})
Last updated on 10/30/2025
```

