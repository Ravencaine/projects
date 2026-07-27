---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Length

Returns the number of characters in the text text.

## Signature

```m
Text.Length(text as nullable text) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |

## Returns

nullable number

### Example 1

Find how many characters are in the text "Hello World".

```m
Text.Length("Hello World")
```

// Output
```
11
```

