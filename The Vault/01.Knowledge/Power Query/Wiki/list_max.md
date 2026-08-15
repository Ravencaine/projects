---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Max

Returns the maximum item in the list or the optional default value if the list is empty. list: The list of values. default: (Optional) The value to return if the list is empty. comparisonCriteria: (Optional) A function that's used to transform the values before they're compared. If this parameter is null, then the values are compared without any transformation. includeNulls: (Optional) Indicates whether null values in the list should be included in determining the maximum item. The default value is true.

## Signature

```m
List.Max(
list as list,
optional default as any,
optional comparisonCriteria as any,
optional includeNulls as nullable logical
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional default | any | |
| optional comparisonCriteria | any | |
| optional includeNulls | nullable logical | |

## Returns

any

### Example 1

Find the maximum value in the specified list.

```m
List.Max({1, 4, 7, 3, -2, 5}, 1)
```

// Output
```
7
```

### Example 2

```m
List.Max({}, -1)
```

// Output
```
-1
```

### Example 3

Find the item in a list of text values that's last alphabetically. If the list is empty, return "none".

```m
let
Source = {"boy", "dog", "girl", "zebra", "cat", "mouse", "rabbit"},
MaxText = List.Max(Source, "none")
in
MaxText
```

// Output
```
"zebra"
```

### Example 4

Find the most recent date from a list of German dates. If the list is empty, return January 1, 2000.

```m
let
Source = {"12.02.2024", "15.05.2025", "10.10.2021", "16.01.2025",
"30.12.2022"},
MaxDate = List.Max(Source, #date(2000, 1, 1), each Date.FromText(_, [Culture =
"de-DE"]))
in
MaxDate
```

// Output
```
"15.05.2025"
```

## Related

[[comparison_criteria]]

