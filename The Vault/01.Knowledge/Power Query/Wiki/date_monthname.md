---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["date", "m-function"]
---


# Date.MonthName

Returns the name of the month component for the provided date. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Date.MonthName(date as any, optional culture as nullable text) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| date | any | |
| optional culture | nullable text | |

## Returns

nullable text

### Example 1

Get the month name.

```m
Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")
```

// Output
```
"December"
```

## Related

[[culture_and_text_formatting]]

