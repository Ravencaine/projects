---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Intersect

Returns the intersection of the list values found in the input list lists. An optional parameter, equationCriteria, can be specified.

## Signature

```m
List.Intersect(lists as list, optional equationCriteria as any) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| lists | list | |
| optional equationCriteria | any | |

## Returns

list

### Example 1

Find the intersection of the lists {1..5}, {2..6}, {3..7}.

```m
List.Intersect({{1..5}, {2..6}, {3..7}})
```

// Output
```
{3, 4, 5}
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

