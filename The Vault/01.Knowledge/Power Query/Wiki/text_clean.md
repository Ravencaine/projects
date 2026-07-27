---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Clean

Returns a text value with all control characters of text removed.

## Signature

```m
Text.Clean(text as nullable text) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |

## Returns

nullable text

### Example 1

Remove line feeds and other control characters from a text value.

```m
Text.Clean("ABC#(lf)D")
```

// Output
```
"ABCD"
```

