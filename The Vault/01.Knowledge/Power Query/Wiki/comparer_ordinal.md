---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["comparer", "m-function"]
---


# Comparer.Ordinal

Returns a comparer function which uses Ordinal rules to compare the provided values x and y.

## Signature

```m
Comparer.Ordinal(x as any, y as any) as number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | any | |
| y | any | |

## Returns

number

### Example 1

Using Ordinal rules, compare if "encyclopædia" and "encyclopaedia" are equivalent. Note these are equivalent using Comparer.FromCulture("en-US"). A comparer function accepts two arguments and returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second.

```m
Comparer.Equals(Comparer.Ordinal, "encyclopædia", "encyclopaedia")
```

// Output
```
false
```

## Related

[[culture_and_text_formatting]]

