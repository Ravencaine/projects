---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.RemoveItems

Removes all occurrences of the given values in the list2 from list1. If the values in list2 don't exist in list1, the original list is returned. Example Remove the items in the list {2, 4, 6} from the list {1, 2, 3, 4, 2, 5, 5}. Usage Power Query M List.RemoveItems({1, 2, 3, 4, 2, 5, 5}, {2, 4, 6}) Output {1, 3, 5, 5} Last updated on 03/24/2026 --- PAGE 763 ---

## Signature

```m
List.RemoveItems(list1 as list, list2 as list) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list1 | list | |
| list2 | list | |

## Returns

list

