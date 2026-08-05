---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["duration", "m-function"]
---


# Duration.ToRecord

Returns a record containing the parts the duration value, duration. duration: A duration from which the record is created. Example Convert #duration(2, 5, 55, 20) into a record of its parts including days, hours, minutes, and seconds if applicable. Usage Power Query M Duration.ToRecord(#duration(2, 5, 55, 20)) Output Power Query M [ Days = 2, Hours = 5, Minutes = 55, Seconds = 20 ] Last updated on 03/24/2026 --- PAGE 627 ---

## Signature

```m
Duration.ToRecord(duration as duration) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| duration | duration | |

## Returns

record

