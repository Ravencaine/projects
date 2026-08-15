---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Transform

Returns a new list of values by applying the transform function transform to the list, list. Example Add 1 to each value in the list {1, 2}. Usage Power Query M List.Transform({1, 2}, each _ + 1) Output {2, 3} Last updated on 03/24/2026 --- PAGE 789 ---

## Signature

```m
List.Transform(list as list, transform as function) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| transform | function | |

## Returns

list

