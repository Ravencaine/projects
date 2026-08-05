---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["double", "m-function"]
---


# Double.From

Returns a Double number value from the given value. If the given value is null, Double.From returns null. If the given value is number within the range of Double, value is returned, otherwise an error is returned. If value is of any other type, it will first be converted to a number using Number.FromText. An optional culture may also be provided (for example, "en-US").

## Signature

```m
Double.From(value as any, optional culture as nullable text) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |
| optional culture | nullable text | |

## Returns

nullable number

### Example 1

Get the Double number value of "4".

```m
Double.From("4.5")
```

// Output
```
4.5
```

## Related

[[culture_and_text_formatting]]

