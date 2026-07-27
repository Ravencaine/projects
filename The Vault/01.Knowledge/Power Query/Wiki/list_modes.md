---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Modes

Returns the items that appear most frequently in list. If the list is empty an error is raised. If multiple items appear with the same maximum frequency, all of them are returned. An optional comparison criteria value, equationCriteria, can be specified to control equality testing.

## Signature

```m
List.Modes(list as list, optional equationCriteria as any) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional equationCriteria | any | |

## Returns

list

### Example 1

Find the items that appears most frequently in the list {"A", 1, 2, 3, 3, 4, 5, 5}.

```m
List.Modes({"A", 1, 2, 3, 3, 4, 5, 5})
```

// Output
```
{3, 5}
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

