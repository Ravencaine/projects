---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Union

Takes a list of lists lists, unions the items in the individual lists and returns them in the output list. As a result, the returned list contains all items in any input lists. This operation maintains traditional bag semantics, so duplicate values are matched as part of the Union. An optional equation criteria value, equationCriteria, can be specified to control equality testing.

## Signature

```m
List.Union(lists as list, optional equationCriteria as any) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lists | list | |
| optional equationCriteria | any | |

## Returns

list

### Example 1

Create a union of the list {1..5}, {2..6}, {3..7}.

```m
List.Union({{1..5}, {2..6}, {3..7}})
```

// Output
```
{1, 2, 3, 4, 5, 6, 7}
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

