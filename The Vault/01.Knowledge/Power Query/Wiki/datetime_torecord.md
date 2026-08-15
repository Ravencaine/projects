---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [datetime, m-function]
---


# DateTime.ToRecord

Returns a record containing the parts of the given datetime value, dateTime. dateTime: A datetime value for from which the record of its parts is to be calculated.

## Signature

```m
DateTime.ToRecord(dateTime as datetime) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | datetime | |

## Returns

record

### Example 1

Convert the #datetime(2011, 12, 31, 11, 56, 2) value into a record containing Date and Time values.

```m
DateTime.ToRecord(#datetime(2011, 12, 31, 11, 56, 2))
```

// Output
```
[
Year = 2011,
Month = 12,
Day = 31,
Hour = 11,
Minute = 56,
Second = 2
]
```

