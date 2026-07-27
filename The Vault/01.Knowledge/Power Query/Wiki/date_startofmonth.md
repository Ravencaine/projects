---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.StartOfMonth

Returns the start of the month that contains dateTime. dateTime must be a date or datetime value.

## Signature

```m
Date.StartOfMonth(dateTime as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dateTime | any | |

## Returns

any

### Example 1

Find the start of the month for October 10th, 2011, 8:10:32AM.

```m
Date.StartOfMonth(#datetime(2011, 10, 10, 8, 10, 32))
```

// Output
```
#datetime(2011, 10, 1, 0, 0, 0)
```

