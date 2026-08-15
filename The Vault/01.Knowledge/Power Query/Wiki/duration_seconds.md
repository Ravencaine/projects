---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [duration, m-function]
---


# Duration.Seconds

Returns the seconds portion of duration.

## Signature

```m
Duration.Seconds(duration as nullable duration) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| duration | nullable duration | |

## Returns

nullable number

### Example 1

Extract the seconds from a duration value.

```m
Duration.Seconds(#duration(5, 4, 3, 2))
```

// Output
```
2
```

