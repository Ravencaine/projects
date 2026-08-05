---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["duration", "m-function"]
---


# Duration.TotalMinutes

Returns the total minutes spanned by duration.

## Signature

```m
Duration.TotalMinutes(duration as nullable duration) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| duration | nullable duration | |

## Returns

nullable number

### Example 1

Find the total minutes spanned by a duration value.

```m
Duration.TotalMinutes(#duration(5, 4, 3, 2))
```

// Output
```
7443.0333333333338
```

