---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.ReplaceRange

Returns the result of removing a number of characters, count, from text value text beginning at position offset and then inserting the text value newText at the same position in text.

## Signature

```m
Text.ReplaceRange(
text as nullable text,
offset as number,
count as number,
newText as text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| offset | number | |
| count | number | |
| newText | text | |

## Returns

nullable text

### Example 1

Replace a single character at position 2 in text value "ABGF" with new text value "CDE".

```m
Text.ReplaceRange("ABGF", 2, 1, "CDE")
```

// Output
```
"ABCDEF"
```

