---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.ToRecord

Returns a record containing the parts of the given date value, date. date: A date value for from which the record of its parts is to be calculated.

## Signature

```m
Date.ToRecord(date as date) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| date | date | |

## Returns

record

### Example 1

Convert the #date(2011, 12, 31) value into a record containing parts from the date value.

```m
Date.ToRecord(#date(2011, 12, 31))
```

// Output
```
[
Year = 2011,
Month = 12,
Day = 31
]
```

