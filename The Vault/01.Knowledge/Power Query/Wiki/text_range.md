---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.Range

Returns the substring from the text text found at the offset offset. An optional parameter, count, can be included to specify how many characters to return. Raises an error if there aren't enough characters.

## Signature

```m
Text.Range(
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

Find the substring from the text "Hello World" starting at index 6.

```m
Text.Range("Hello World", 6)
```

// Output
```
"World"
```

### Example 2

Find the substring from the text "Hello World Hello" starting at index 6 spanning 5 characters.

```m
Text.Range("Hello World Hello", 6, 5)
```

// Output
```
"World"
Last updated on 02/11/2026
```

