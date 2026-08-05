---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Single

If there is only one item in the list list, returns that item. If there is more than one item or the list is empty, the function raises an error.

## Signature

```m
List.Single(list as list) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

any

### Example 1

Find the single value in the list {1}.

```m
List.Single({1})
```

// Output
```
1
```

### Example 2

Find the single value in the list {1, 2, 3}.

```m
List.Single({1, 2, 3})
```

// Output
```
[Expression.Error] There were too many elements in the enumeration to complete the
operation.
Last updated on 01/22/2026
```

