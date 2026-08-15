---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.PositionOf

Returns the offset at which the specified value appears in a list. Returns -1 if the value doesn't appear. list: The list to search. value: The value to find in the list. occurrence: (Optional) The specific occurrence to report. This value can be Occurrence.First, Occurrence.Last, or Occurrence.All. If no occurrence is specified, Occurrence.First is used. equationCriteria: (Optional) Specifies how equality is determined when comparing values. This parameter can be a key selector function, a comparer function, or a list containing both a key selector and a comparer.

## Signature

```m
List.PositionOf(
list as list,
value as any,
optional occurrence as nullable number,
optional equationCriteria as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| value | any | |
| optional occurrence | nullable number | |
| optional equationCriteria | any | |

## Returns

any

### Example 1

Find the position in the list {1, 2, 3} at which the value 3 appears.

```m
List.PositionOf({1, 2, 3}, 3)
```

// Output
```
2
```

### Example 2

Find the position in the list of all instances of dates from 2022.

```m
let
Source = {
#date(2021, 5, 10),
#date(2022, 6, 28),
#date(2023, 7, 15),
#date(2022, 12, 31),
#date(2022, 4, 8),
#date(2024, 3, 20)
},
YearList = List.Transform(Source, each Date.Year(_)),
TargetYear = 2022,
FindPositions = List.PositionOf(YearList, TargetYear, Occurrence.All)
in
FindPositions
```

// Output
```
{1, 3, 4}
```

### Example 3

Find the position in the list of the last occurrence of the word dog, ignoring case.

```m
let
Source = List.PositionOf(
{"dog", "cat", "DOG", "pony", "bat", "rabbit", "dOG"},
"dog",
Occurrence.Last,
Comparer.OrdinalIgnoreCase
)
in
Source
```

// Output
```
6
```

### Example 4

Find the position in the list that's within two units of the number 28.

```m
let
Source = { 10, 15, 20, 25, 30 },
Position = List.PositionOf(
Source,
28,
Occurrence.First,
(x, y) => Number.Abs(x - y) <= 2
)
in
Position
```

// Output
```
4
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

