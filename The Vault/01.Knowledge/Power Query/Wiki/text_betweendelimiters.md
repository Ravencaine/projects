---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.BetweenDelimiters

Returns the portion of text between the specified startDelimiter and endDelimiter. An optional numeric startIndex indicates which occurrence of the startDelimiter should be considered. An optional list startIndex indicates which occurrence of the startDelimiter should be considered, as well as whether indexing should be done from the start or end of the input. The endIndex is similar, except that indexing is done relative to the startIndex.

## Signature

```m
Text.BetweenDelimiters(
text as nullable text,
startDelimiter as text,
endDelimiter as text,
optional startIndex as any,
optional endIndex as any
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| startDelimiter | text | |
| endDelimiter | text | |
| optional startIndex | any | |
| optional endIndex | any | |

## Returns

any

### Example 1

Get the portion of "111 (222) 333 (444)" between the (first) open parenthesis and the (first) closed parenthesis that follows it.

```m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")")
```

// Output
```
"222"
```

### Example 2

```m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", 1, 0)
```

// Output
```
"444"
```

### Example 3

Get the portion of "111 (222) 333 (444)" between the second open parenthesis from the end and the second closed parenthesis that follows it.

```m
Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", {1,
RelativePosition.FromEnd}, {1, RelativePosition.FromStart})
```

// Output
```
"222) 333 (444"
```

