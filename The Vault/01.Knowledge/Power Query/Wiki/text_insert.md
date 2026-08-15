---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.Insert

Returns the result of inserting text value newText into the text value text at position offset. Positions start at number 0.

## Signature

```m
Text.Insert(
text as nullable text,
offset as number,
newText as text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| offset | number | |
| newText | text | |

## Returns

nullable text

### Example 1

Insert "C" between "B" and "D" in "ABD".

```m
Text.Insert("ABD", 2, "C")
```

// Output
```
"ABCD"
```

