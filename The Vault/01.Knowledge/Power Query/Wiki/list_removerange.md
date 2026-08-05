---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.RemoveRange

Removes count values in the list starting at the specified position, index.

## Signature

```m
List.RemoveRange(
list as list,
index as number,
optional count as nullable number
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| index | number | |
| optional count | nullable number | |

## Returns

list

### Example 1

Remove 3 values in the list {1, 2, 3, 4, -6, -2, -1, 5} starting at index 4.

```m
List.RemoveRange({1, 2, 3, 4, -6, -2, -1, 5}, 4, 3)
```

// Output
```
{1, 2, 3, 4, 5}
```

