---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Middle

Returns count characters, or through the end of text; at the offset start.

## Signature

```m
Text.Middle(
text as nullable text,
start as number,
optional count as nullable number
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| start | number | |
| optional count | nullable number | |

## Returns

nullable text

### Example 1

Find the substring from the text "Hello World" starting at index 6 spanning 5 characters.

```m
Text.Middle("Hello World", 6, 5)
```

// Output
```
"World"
```

### Example 2

Find the substring from the text "Hello World" starting at index 6 through the end.

```m
Text.Middle("Hello World", 6, 20)
```

// Output
```
"World"
```

### Example 3

Find the substring from the text "Hello World" starting at index 0 spanning 2 characters.

```m
Text.Middle("Hello World", 0, 2)
```

// Output
```
"He"
```

