---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.First

Returns the first item in the list list, or the optional default value, defaultValue, if the list is empty. If the list is empty and a default value is not specified, the function returns null.

## Signature

```m
List.First(list as list, optional defaultValue as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional defaultValue | any | |

## Returns

any

### Example 1

Find the first value in the list {1, 2, 3}.

```m
List.First({1, 2, 3})
```

// Output
```
1
```

### Example 2

Find the first value in the list {}. If the list is empty, return -1.

```m
List.First({}, -1)
```

// Output
```
-1
```

