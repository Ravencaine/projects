---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.ReplaceMatchingItems

Performs the given replacements to the list list. A replacement operation replacements consists of a list of two values, the old value and new value, provided in a list. An optional equation criteria value, equationCriteria, can be specified to control equality testing.

## Signature

```m
List.ReplaceMatchingItems(
list as list,
replacements as list,
optional equationCriteria as any
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| replacements | list | |
| optional equationCriteria | any | |

## Returns

list

### Example 1

Create a list from {1, 2, 3, 4, 5} replacing the value 5 with -5, and the value 1 with -1.

```m
List.ReplaceMatchingItems({1, 2, 3, 4, 5}, {{5, -5}, {1, -1}})
```

// Output
```
{-1, 2, 3, 4, -5}
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

