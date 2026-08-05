---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Dates

Returns a list of date values of size count, starting at start. The given increment, step, is a duration value that is added to every value.

## Signature

```m
List.Dates(
start as date,
count as number,
step as duration
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | date | |
| count | number | |
| step | duration | |

## Returns

list

### Example 1

Create a list of 5 values starting from New Year's Eve (#date(2011, 12, 31)) incrementing by 1 day (#duration(1, 0, 0, 0)).

```m
List.Dates(#date(2011, 12, 31), 5, #duration(1, 0, 0, 0))
```

// Output
```
{
#date(2011, 12, 31),
#date(2012, 1, 1),
#date(2012, 1, 2),
#date(2012, 1, 3),
#date(2012, 1, 4)
}
```

