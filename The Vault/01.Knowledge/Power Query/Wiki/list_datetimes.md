---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.DateTimes

Returns a list of datetime values of size count, starting at start. The given increment, step, is a duration value that is added to every value. Example Create a list of 10 values starting from 5 minutes before New Year's Day (#datetime(2011, 12, 31, 23, 55, 0)) incrementing by 1 minute (#duration(0, 0, 1, 0)). Usage Power Query M List.DateTimes(#datetime(2011, 12, 31, 23, 55, 0), 10, #duration(0, 0, 1, 0)) Output Power Query M { #datetime(2011, 12, 31, 23, 55, 0), #datetime(2011, 12, 31, 23, 56, 0), #datetime(2011, 12, 31, 23, 57, 0), #datetime(2011, 12, 31, 23, 58, 0), #datetime(2011, 12, 31, 23, 59, 0), #datetime(2012, 1, 1, 0, 0, 0), #datetime(2012, 1, 1, 0, 1, 0), #datetime(2012, 1, 1, 0, 2, 0), #datetime(2012, 1, 1, 0, 3, 0), --- PAGE 698 --- #datetime(2012, 1, 1, 0, 4, 0) } --- PAGE 699 ---

## Signature

```m
List.DateTimes(
start as datetime,
count as number,
step as duration
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | datetime | |
| count | number | |
| step | duration | |

## Returns

list

