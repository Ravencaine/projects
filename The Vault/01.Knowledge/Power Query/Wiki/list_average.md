---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [list, m-function]
---


# List.Average

Returns the average value for the items in the list, list. The result is given in the same datatype as the values in the list. Only works with number, date, time, datetime, datetimezone and duration values. If the list is empty null is returned.

## Signature

```m
List.Average(list as list, optional precision as nullable number) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional precision | nullable number | |

## Returns

any

### Example 1

Find the average of the list of numbers, {3, 4, 6}.

```m
List.Average({3, 4, 6})
```

// Output
```
4.333333333333333
```

### Example 2

Find the average of the date values January 1, 2011, January 2, 2011 and January 3, 2011.

```m
List.Average({#date(2011, 1, 1), #date(2011, 1, 2), #date(2011, 1, 3)})
```

// Output
```
#date(2011, 1, 2)
```

