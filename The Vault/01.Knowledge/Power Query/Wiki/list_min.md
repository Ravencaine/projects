---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Min

Returns the minimum item in the list list, or the optional default value default if the list is empty. An optional comparisonCriteria value, comparisonCriteria, may be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used.

## Signature

```m
List.Min(
list as list,
optional default as any,
optional comparisonCriteria as any,
optional includeNulls as nullable logical
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional default | any | |
| optional comparisonCriteria | any | |
| optional includeNulls | nullable logical | |

## Returns

any

### Example 1

Find the min in the list {1, 4, 7, 3, -2, 5}.

```m
List.Min({1, 4, 7, 3, -2, 5})
```

// Output
```
-2
```

### Example 2

Find the min in the list {} or return -1 if it is empty.

```m
List.Min({}, -1)
```

// Output
```
-1
```

## Related

[[comparison_criteria]]

