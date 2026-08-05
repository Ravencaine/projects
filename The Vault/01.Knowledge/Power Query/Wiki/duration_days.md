---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["duration", "m-function"]
---


# Duration.Days

Returns the days portion of duration.

## Signature

```m
Duration.Days(duration as nullable duration) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| duration | nullable duration | |

## Returns

nullable number

### Example 1

Extract the number of days between two dates.

```m
Duration.Days(#date(2022, 3, 4) - #date(2022, 2, 25))
```

// Output
```
7
```

