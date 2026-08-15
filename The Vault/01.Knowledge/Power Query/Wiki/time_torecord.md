---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [time, m-function]
---


# Time.ToRecord

Returns a record containing the parts of the given Time value, time. time: A time value for from which the record of its parts is to be calculated. Example Convert the #time(11, 56, 2) value into a record containing Time values. Usage Power Query M Time.ToRecord(#time(11, 56, 2)) Output Power Query M [ Hour = 11, Minute = 56, Second = 2 ] Last updated on 03/24/2026 --- PAGE 1256 ---

## Signature

```m
Time.ToRecord(time as time) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| time | time | |

## Returns

record

