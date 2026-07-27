---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.FirstN

If a number is specified, up to that many items are returned. If a condition is specified, all items are returned that initially meet the condition. Once an item fails the condition, no further items are considered.

## Signature

```m
List.FirstN(list as list, countOrCondition as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| countOrCondition | any | |

## Returns

any

### Example 1

Find the intial values in the list {3, 4, 5, -1, 7, 8, 2} that are greater than 0.

```m
List.FirstN({3, 4, 5, -1, 7, 8, 2}, each _ > 0)
```

// Output
```
{3, 4, 5}
```

