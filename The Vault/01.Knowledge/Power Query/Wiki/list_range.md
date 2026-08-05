---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Range

Returns a subset of list beginning at offset. An optional parameter, count, sets the maximum number of items in the subset.

## Signature

```m
List.Range(
list as list,
offset as number,
optional count as nullable number
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| offset | number | |
| optional count | nullable number | |

## Returns

list

### Example 1

Find the subset starting at offset 6 of the list of numbers 1 through 10.

```m
List.Range({1..10}, 6)
```

// Output
```
{7, 8, 9, 10}
```

### Example 2

Find the subset of length 2 from offset 6, from the list of numbers 1 through 10.

```m
List.Range({1..10}, 6, 2)
```

// Output
```
{7, 8}
```

