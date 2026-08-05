---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.EndsWith

Indicates whether the given text, text, ends with the specified value, substring. The indication is case sensitive. comparer is a Comparer which is used to control the comparison. Comparers can be used to provide case-insensitive or culture and locale-aware comparisons. The following built-in comparers are available in the formula language: Comparer.Ordinal: Used to perform an exact ordinal comparison Comparer.OrdinalIgnoreCase: Used to perform an exact ordinal case-insensitive comparison Comparer.FromCulture: Used to perform a culture-aware comparison

## Signature

```m
Text.EndsWith(
text as nullable text,
substring as text,
optional comparer as nullable function
) as nullable logical
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| substring | text | |
| optional comparer | nullable function | |

## Returns

nullable logical

### Example 1

Check if "Hello, World" ends with "world".

```m
Text.EndsWith("Hello, World", "world")
```

// Output
```
false
```

### Example 2

Check if "Hello, World" ends with "World".

```m
Text.EndsWith("Hello, World", "World")
```

// Output
```
true
```

## Related

[[culture_and_text_formatting]]

