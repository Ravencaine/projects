---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.ContainsAll

Indicates whether the list includes all the values from another list. Returns true if all the values are found in the list, false otherwise. list: The list to search. values: The list of values to search for in the first list. equationCriteria: (Optional) The comparer used to determine if the two values are equal.

## Signature

```m
List.ContainsAll(
list as list,
values as list,
optional equationCriteria as any
) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| values | list | |
| optional equationCriteria | any | |

## Returns

logical

### Example 1

Determine if the list {1, 2, 3, 4, 5} contains 3 and 4.

```m
List.ContainsAll({1, 2, 3, 4, 5}, {3, 4})
```

// Output
```
true
```

### Example 2

Determine if the list {1, 2, 3, 4, 5} contains 5 and 6.

```m
Power Query M
List.ContainsAll({1, 2, 3, 4, 5}, {5, 6})
```

// Output
```
false
```

### Example 3

Determine if the list contains a dog and a horse, while ignoring case.

```m
List.ContainsAll({"dog", "cat", "racoon", "horse", "rabbit"}, {"DOG", "Horse"},
Comparer.OrdinalIgnoreCase)
```

// Output
```
true
```

### Example 4

Determine if the list contains the dates April 8, 2022 and July 6, 2021.

```m
let
Source = {#date(2024, 2, 23), #date(2023, 12, 2), #date(2022, 4, 8),
#date(2021, 7, 6)},
ContainsDates = List.ContainsAll(Source, {#date(2022, 4, 8), #date(2021, 7,
6)})
in
ContainsDates
```

// Output
```
true
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

