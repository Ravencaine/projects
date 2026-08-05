---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.RemoveMatchingItems

Removes all occurrences of the given values in list2 from the list list1. If the values in list2 don't exist in list1, the original list is returned. An optional equation criteria value, equationCriteria, can be specified to control equality testing. Example Create a list from {1, 2, 3, 4, 5, 5} without {1, 5}. Usage Power Query M List.RemoveMatchingItems({1, 2, 3, 4, 5, 5}, {1, 5}) Output {2, 3, 4} Related content Equation criteria Last updated on 03/24/2026 --- PAGE 766 ---

## Signature

```m
List.RemoveMatchingItems(
list1 as list,
list2 as list,
optional equationCriteria as any
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list1 | list | |
| list2 | list | |
| optional equationCriteria | any | |

## Returns

list

