---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.At

Returns the character in the text value, text at position index. The first character in the text is at position 0.

## Signature

```m
Text.At(text as nullable text, index as number) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| index | number | |

## Returns

nullable text

### Example 1

Find the character at position 4 in string "Hello, World".

```m
Text.At("Hello, World", 4)
```

// Output
```
"o"
```

