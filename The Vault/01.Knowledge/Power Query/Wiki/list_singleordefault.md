---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.SingleOrDefault

If there is only one item in the list list, returns that item. If the list is empty, the function returns null unless an optional default is specified. If there is more than one item in the list, the function returns an error.

## Signature

```m
List.SingleOrDefault(list as list, optional default as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional default | any | |

## Returns

any

### Example 1

Find the single value in the list {1}.

```m
List.SingleOrDefault({1})
```

// Output
```
1
```

### Example 2

Find the single value in the list {}.

```m
List.SingleOrDefault({})
```

// Output
```
null
```

### Example 3

Find the single value in the list {}. If is empty, return -1.

```m
List.SingleOrDefault({}, -1)
```

// Output
```
-1
```

