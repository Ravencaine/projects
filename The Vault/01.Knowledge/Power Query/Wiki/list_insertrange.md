---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.InsertRange

Returns a new list produced by inserting the values in values into list at index. The first position in the list is at index 0. list: The target list where values are to be inserted. index: The index of the target list(list) where the values are to be inserted. The first position in the list is at index 0. values: The list of values which are to be inserted into list.

## Signature

```m
List.InsertRange(
list as list,
index as number,
values as list
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| index | number | |
| values | list | |

## Returns

list

### Example 1

Insert the list ({3, 4}) into the target list ({1, 2, 5}) at index 2.

```m
List.InsertRange({1, 2, 5}, 2, {3, 4})
```

// Output
```
{
1,
2,
3,
4,
5
}
```

### Example 2

Insert a list with a nested list ({1, {1.1, 1.2}}) into a target list ({2, 3, 4}) at index 0.

```m
List.InsertRange({2, 3, 4}, 0, {1, {1.1, 1.2}})
```

// Output
```
{
1,
{
1.1,
1.2
},
2,
3,
4
}
```

