---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.RemoveFirstN

Returns a list that removes the first element of list list. If list is an empty list an empty list is returned. This function takes an optional parameter, countOrCondition, to support removing multiple values as listed below. If a number is specified, up to that many items are removed. If a condition is specified, any consecutive matching items at the start of list are removed. If this parameter is null, the default behavior is observed.

## Signature

```m
List.RemoveFirstN(list as list, optional countOrCondition as any) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional countOrCondition | any | |

## Returns

list

### Example 1

Create a list from {1, 2, 3, 4, 5} without the first 3 numbers.

```m
List.RemoveFirstN({1, 2, 3, 4, 5}, 3)
```

// Output
```
{4, 5}
```

### Example 2

Create a list from {5, 4, 2, 6, 1} that starts with a number less than 3.

```m
List.RemoveFirstN({5, 4, 2, 6, 1}, each _ > 3)
```

// Output
```
{2, 6, 1}
```

