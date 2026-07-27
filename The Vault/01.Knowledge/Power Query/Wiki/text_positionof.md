---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.PositionOf

Returns the position of the specified occurrence of the text value substring found in text. An optional parameter occurrence may be used to specify which occurrence position to return (first occurrence by default). Returns -1 if substring was not found. comparer is a Comparer which is used to control the comparison. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons. The following built-in comparers are available in the formula language: Comparer.Ordinal: Used to perform an exact ordinal comparison Comparer.OrdinalIgnoreCase: Used to perform an exact ordinal case-insensitive comparison Comparer.FromCulture: Used to perform a culture-aware comparison

## Signature

```m
Text.PositionOf(
text as text,
substring as text,
optional occurrence as nullable number,
optional comparer as nullable function
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | text | |
| substring | text | |
| optional occurrence | nullable number | |
| optional comparer | nullable function | |

## Returns

any

### Example 1

Get the position of the first occurrence of "World" in the text "Hello, World! Hello, World!".

```m
Text.PositionOf("Hello, World! Hello, World!", "World")
```

// Output
```
7
```

### Example 2

Get the position of the last occurrence of "World" in "Hello, World! Hello, World!".

```m
Text.PositionOf("Hello, World! Hello, World!", "World", Occurrence.Last)
```

// Output
```
21
```

## Related

[[culture_and_text_formatting]]

