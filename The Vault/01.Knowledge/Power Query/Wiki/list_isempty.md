---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.IsEmpty

Returns true if the list, list, contains no values (length 0). If the list contains values (length > 0), returns false.

## Signature

```m
List.IsEmpty(list as list) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |

## Returns

logical

### Example 1

Find if the list {} is empty.

```m
List.IsEmpty({})
```

// Output
```
true
```

### Example 2

Find if the list {1, 2} is empty.

```m
List.IsEmpty({1, 2})
```

// Output
```
false
```

