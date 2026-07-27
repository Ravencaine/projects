---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["duration", "m-function"]
---


# Duration.TotalSeconds

Returns the total seconds spanned by duration.

## Signature

```m
Duration.TotalSeconds(duration as nullable duration) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| duration | nullable duration | |

## Returns

nullable number

### Example 1

Find the total seconds spanned by a duration value.

```m
Duration.TotalSeconds(#duration(5, 4, 3, 2))
```

// Output
```
446582
```

