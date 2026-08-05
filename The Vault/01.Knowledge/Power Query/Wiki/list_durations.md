---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Durations

Returns a list of count duration values, starting at start and incremented by the given duration step. Example Create a list of 5 values starting with 1 hour and incrementing by an hour. Usage Power Query M List.Durations(#duration(0, 1, 0, 0), 5, #duration(0, 1, 0, 0)) Output Power Query M { #duration(0, 1, 0, 0), #duration(0, 2, 0, 0), #duration(0, 3, 0, 0), #duration(0, 4, 0, 0), #duration(0, 5, 0, 0) } Last updated on 04/03/2026 --- PAGE 707 ---

## Signature

```m
List.Durations(
start as duration,
count as number,
step as duration
) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | duration | |
| count | number | |
| step | duration | |

## Returns

list

