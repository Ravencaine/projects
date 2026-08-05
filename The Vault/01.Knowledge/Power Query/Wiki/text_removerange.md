---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.RemoveRange

Returns a copy of the text value text with all the characters from position offset removed. An optional parameter, count can by used to specify the number of characters to remove. The default value of count is 1. Position values start at 0.

## Signature

```m
Text.RemoveRange(
text as nullable text,
offset as number,
optional count as nullable number
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| offset | number | |
| optional count | nullable number | |

## Returns

nullable text

### Example 1

Remove 1 character from the text value "ABEFC" at position 2.

```m
Text.RemoveRange("ABEFC", 2)
```

// Output
```
"ABFC"
```

### Example 2

Remove two characters from the text value "ABEFC" starting at position 2.

```m
Text.RemoveRange("ABEFC", 2, 2)
```

// Output
```
"ABC"
```

