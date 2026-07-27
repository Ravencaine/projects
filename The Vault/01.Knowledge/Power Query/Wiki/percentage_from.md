---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["percentage", "m-function"]
---


# Percentage.From

Returns a percentage value from the given value. If the given value is null, Percentage.From returns null. If the given value is text with a trailing percent symbol, then the converted decimal number will be returned. Otherwise, the value will be converted to a number using Number.From. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Percentage.From(value as any, optional culture as nullable text) as nullable
number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable number

### Example 1

Get the percentage value of "12.3%".

```m
Percentage.From("12.3%")
```

// Output
```
0.123
```

## Related

[[culture_and_text_formatting]]

