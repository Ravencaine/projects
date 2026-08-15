---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.RemoveNulls

Removes all occurrences of "null" values in the list. If there are no 'null' values in the list, the original list is returned.

## Signature

```m
List.RemoveNulls(list as list) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

list

### Example 1

Remove the "null" values from the list {1, 2, 3, null, 4, 5, null, 6}.

```m
List.RemoveNulls({1, 2, 3, null, 4, 5, null, 6})
```

// Output
```
{1, 2, 3, 4, 5, 6}
```

