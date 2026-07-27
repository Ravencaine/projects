---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.DayOfWeekName

Returns the day of the week name for the provided date. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Date.DayOfWeekName(date as any, optional culture as nullable text) as nullable
text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| date | any | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Get the day of the week name.

```m
Date.DayOfWeekName(#date(2011, 12, 31), "en-US")
```

// Output
```
"Saturday"
```

## Related

[[culture_and_text_formatting]]

