---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Sum

Returns the sum of the non-null values in the list, list. Returns null if there are no non-null values in the list.

## Signature

```m
List.Sum(list as list, optional precision as nullable number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional precision | nullable number | |

## Returns

any

### Example 1

Find the sum of the numbers in the list {1, 2, 3}.

```m
List.Sum({1, 2, 3})
```

// Output
```
6
```

