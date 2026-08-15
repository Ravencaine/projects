---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.ReplaceRange

Replaces count values in the list with the list replaceWith, starting at specified position, index. Example Replace {7, 8, 9} in the list {1, 2, 7, 8, 9, 5} with {3, 4}. Usage Power Query M List.ReplaceRange({1, 2, 7, 8, 9, 5}, 2, 3, {3, 4}) Output {1, 2, 3, 4, 5} Last updated on 03/24/2026 --- PAGE 771 ---

## Signature

```m
List.ReplaceRange(
list as list,
index as number,
count as number,
replaceWith as list
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| index | number | |
| count | number | |
| replaceWith | list | |

## Returns

list

