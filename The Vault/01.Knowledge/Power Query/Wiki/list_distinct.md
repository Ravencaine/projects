---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Distinct

Returns a list that contains all the values in the specified list with duplicates removed. If the specified list is empty, the result is an empty list. list: The list from which distinct values are extracted. equationCriteria: (Optional) Specifies how equality is determined when comparing values. This parameter can be a key selector function, a comparer function, or a list containing both a key selector and a comparer.

## Signature

```m
List.Distinct(list as list, optional equationCriteria as any) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional equationCriteria | any | |

## Returns

list

### Example 1

Remove the duplicates from the list {1, 1, 2, 3, 3, 3}.

```m
List.Distinct({1, 1, 2, 3, 3, 3})
```

// Output
```
{1, 2, 3}
```

### Example 2

Starting at the end of the list, select the fruits that have a unique text length.

```m
let
Source = {"Apple", "Banana", "Cherry", "Date", "Fig"},
Result = List.Distinct(List.Reverse(Source), each Text.Length(_))
in
Result
```

// Output
```
{"Fig", "Date", "Cherry", "Apple"}
```

### Example 3

Starting at the beginning of the list, select the unique fruits while ignoring case.

```m
let
Source = {"apple", "Pear", "aPPle", "banana", "ORANGE", "pear", "Banana",
"Cherry"},
Result = List.Distinct(Source, Comparer.OrdinalIgnoreCase)
in
Result
```

// Output
```
{"apple", "Pear", "banana", "ORANGE", "Cherry"}
```

### Example 4

Extract from a list of lists the first lists with unique country names while ignoring case. Place the extracted lists in the rows of a new table.

```m
let
Source = {
{"USA", #date(2023, 8, 1), 567},
{"canada", #date(2023, 8, 1), 254},
{"Usa", #date(2023, 7, 1), 450},
{"CANADA", #date(2023, 6, 1), 357},
{"Panama", #date(2023, 6, 2), 20},
{"panama", #date(2023, 7, 1), 40}
},
DistinctByCountry = List.Distinct(
Source,
{each _{0}, Comparer.OrdinalIgnoreCase}
),
ToTable = Table.FromRows(DistinctByCountry, {"Country", "Date", "Value"}),
ChangeTypes = Table.TransformColumnTypes(
ToTable, {{"Country", type text}, {"Date", type date}, {"Value",
Int64.Type}}
)
in
ChangeTypes
```

// Output
```
#table(type table[Country = text, Date = date, Value = Int64.Type],
{
{"USA", #date(2023, 8, 1), 567},
{"canada", #date(2023, 8, 1), 254},
{"Panama", #date(2023, 6, 2), 20}
}
)
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

