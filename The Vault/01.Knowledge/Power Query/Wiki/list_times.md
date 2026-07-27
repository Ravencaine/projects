---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Times

Returns a list of time values of size count, starting at start. The given increment, step, is a duration value that is added to every value.

## Signature

```m
List.Times(
start as time,
count as number,
step as duration
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | time | |
| count | number | |
| step | duration | |

## Returns

list

### Example 1

Create a list of 4 values starting from noon (#time(12, 0, 0)) incrementing by one hour (#duration(0, 1, 0, 0)).

```m
List.Times(#time(12, 0, 0), 4, #duration(0, 1, 0, 0))
```

// Output
```
{
#time(12, 0, 0),
#time(13, 0, 0),
#time(14, 0, 0),
#time(15, 0, 0)
}
```

