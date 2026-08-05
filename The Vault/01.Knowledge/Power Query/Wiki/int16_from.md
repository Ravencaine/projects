---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["int16", "m-function"]
---


# Int16.From

Returns a 16-bit integer number value from the given value. If the given value is null, Int16.From returns null. If the given value is number within the range of 16-bit integer without a fractional part, value is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is RoundingMode.ToEven. If value is of any other type, it will first be converted to a number using Number.FromText. Refer to Number.Round for the available rounding modes. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Int16.From(
value as any,
optional culture as nullable text,
optional roundingMode as nullable number
) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |
| optional roundingMode | nullable number | |

## Returns

nullable number

### Example 1

Get the 16-bit integer number value of "4".

```m
Int64.From("4")
```

// Output
```
4
```

### Example 2

Get the 16-bit integer number value of "4.5" using RoundingMode.AwayFromZero.

```m
Int16.From("4.5", null, RoundingMode.AwayFromZero)
```

// Output
```
5
```

## Related

[[culture_and_text_formatting]]

