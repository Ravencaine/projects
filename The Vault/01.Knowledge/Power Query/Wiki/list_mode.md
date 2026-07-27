---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Mode

Returns the item that appears most frequently in list. If the list is empty an error is raised. If multiple items appear with the same maximum frequency, the last one is chosen. An optional comparison criteria value, equationCriteria, can be specified to control equality testing.

## Signature

```m
List.Mode(list as list, optional equationCriteria as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional equationCriteria | any | |

## Returns

any

### Example 1

Find the item that appears most frequently in the list {"A", 1, 2, 3, 3, 4, 5}.

```m
List.Mode({"A", 1, 2, 3, 3, 4, 5})
```

// Output
```
3
```

### Example 2

Find the item that appears most frequently in the list {"A", 1, 2, 3, 3, 4, 5, 5}.

```m
List.Mode({"A", 1, 2, 3, 3, 4, 5, 5})
```

// Output
```
5
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

