---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.IsDistinct

Returns a logical value whether there are duplicates in the list list; true if the list is distinct, false if there are duplicate values.

## Signature

```m
List.IsDistinct(list as list, optional equationCriteria as any) as logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional equationCriteria | any | |

## Returns

logical

### Example 1

Find if the list {1, 2, 3} is distinct (i.e. no duplicates).

```m
List.IsDistinct({1, 2, 3})
```

// Output
```
true
```

### Example 2

Find if the list {1, 2, 3, 3} is distinct (i.e. no duplicates).

```m
List.IsDistinct({1, 2, 3, 3})
```

// Output
```
false
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

