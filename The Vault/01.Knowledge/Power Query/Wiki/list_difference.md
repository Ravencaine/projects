---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Difference

Returns the items in list list1 that do not appear in list list2. Duplicate values are supported. An optional equation criteria value, equationCriteria, can be specified to control equality testing.

## Signature

```m
List.Difference(
list1 as list,
list2 as list,
optional equationCriteria as any
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list1 | list | |
| list2 | list | |
| optional equationCriteria | any | |

## Returns

list

### Example 1

Find the items in list {1, 2, 3, 4, 5} that do not appear in {4, 5, 3}.

```m
List.Difference({1, 2, 3, 4, 5}, {4, 5, 3})
```

// Output
```
{1, 2}
```

### Example 2

Find the items in the list {1, 2} that do not appear in {1, 2, 3}.

```m
List.Difference({1, 2}, {1, 2, 3})
```

// Output
```
{}
```

## Related

[[comparison_criteria]]
[[equation_criteria]]

