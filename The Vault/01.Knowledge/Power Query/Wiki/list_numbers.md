---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Numbers

Returns a list of numbers given an initial value, count, and optional increment value. The default increment value is 1. start: The initial value in the list. count: The number of values to create. increment: [Optional] The value to increment by. If omitted values are incremented by 1.

## Signature

```m
List.Numbers(
start as number,
count as number,
optional increment as nullable number
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | number | |
| count | number | |
| optional increment | nullable number | |

## Returns

list

### Example 1

Generate a list of 10 consecutive numbers starting at 1.

```m
List.Numbers(1, 10)
```

// Output
```
{
1,
2,
3,
4,
5,
6,
7,
8,
9,
10
}
```

### Example 2

Generate a list of 10 numbers starting at 1, with an increment of 2 for each subsequent number.

```m
List.Numbers(1, 10, 2)
```

// Output
```
{
1,
3,
5,
7,
9,
11,
13,
15,
17,
19
}
```

