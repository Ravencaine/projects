---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Last

Returns the last item in the specified list, or the optional default value if the list is empty. list: The list to examine. defaultValue: (Optional) The default value to return if the list is empty. If the list is empty and a default value isn't specified, the function returns null.

## Signature

```m
List.Last(list as list, optional defaultValue as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional defaultValue | any | |

## Returns

any

### Example 1

Find the last value in the list {1, 2, 3}.

```m
List.Last({1, 2, 3})
```

// Output
```
3
```

### Example 2

Find the last value in the list {} or -1 if it empty.

```m
List.Last({}, -1)
```

// Output
```
-1
Last updated on 10/31/2025
```

