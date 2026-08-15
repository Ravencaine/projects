---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [currency, m-function]
---


# Currency.From

Returns a currency value from the given value. If the given value is null, Currency.From returns null. If the given value is number within the range of currency, fractional part of the value is rounded to 4 decimal digits and returned. If value is of any other type, it will first be converted to a number using Number.FromText. Valid range for currency is -922,337,203,685,477.5808 to 922,337,203,685,477.5807. Refer to Number.Round for the available rounding modes. The default is RoundingMode.ToEven. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Currency.From(
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

Get the currency value of "1.23455".

```m
Currency.From("1.23455")
```

// Output
```
1.2346
```

### Example 2

Get the currency value of "1.23455" using RoundingMode.Down.

```m
Currency.From("1.23455", "en-US", RoundingMode.Down)
```

// Output
```
1.2345
```

## Related

[[culture_and_text_formatting]]

