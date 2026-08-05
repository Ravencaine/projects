---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["decimal", "m-function"]
---


# Decimal.From

Returns a Decimal number value from the given value. If the given value is null, Decimal.From returns null. If the given value is number within the range of Decimal, value is returned, otherwise an error is returned. If value is of any other type, it will first be converted to a number using Number.FromText. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Decimal.From(value as any, optional culture as nullable text) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable number

### Example 1

Get the Decimal number value of "4.5".

```m
Decimal.From("4.5")
```

// Output
```
4.5
```

## Related

[[culture_and_text_formatting]]

