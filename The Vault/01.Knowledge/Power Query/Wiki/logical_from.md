---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["logical", "m-function"]
---


# Logical.From

Returns a logical value from the given value. If the given value is null, Logical.From returns null. If the given value is logical, value is returned. Values of the following types can be converted to a logical value: text: A logical value from the text value, either "true" or "false". Refer to Logical.FromText for details. number: false if value equals 0, true otherwise. If value is of any other type, an error is returned.

## Signature

```m
Logical.From(value as any) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | any | |

## Returns

nullable logical

### Example 1

Convert 2 to a logical value.

```m
Logical.From(2)
```

// Output
```
true
```

