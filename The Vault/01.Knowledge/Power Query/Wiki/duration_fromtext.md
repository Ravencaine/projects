---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [duration, m-function]
---


# Duration.FromText

Returns a duration value from the specified text, text. The following formats can be parsed by this function: (-)hh:mm(:ss(.ff)) (-)ddd(.hh:mm(:ss(.ff))) (All ranges are inclusive) ddd: Number of days. hh: Number of hours, between 0 and 23. mm: Number of minutes, between 0 and 59. ss: Number of seconds, between 0 and 59. ff: Fraction of seconds, between 0 and 9999999.

## Signature

```m
Duration.FromText(text as nullable text) as nullable duration
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |

## Returns

nullable duration

### Example 1

Convert "2.05:55:20" into a duration value.

```m
Duration.FromText("2.05:55:20")
```

// Output
```
#duration(2, 5, 55, 20)
```

