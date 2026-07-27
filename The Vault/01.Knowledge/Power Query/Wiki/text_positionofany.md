---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.PositionOfAny

Returns the first position of any character in the list characters that is found in text. An optional parameter occurrence may be used to specify which occurrence position to return.

## Signature

```m
Text.PositionOfAny(
text as text,
characters as list,
optional occurrence as nullable number
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | text | |
| characters | list | |
| optional occurrence | nullable number | |

## Returns

any

### Example 1

Find the first position of "W" or "H" in text "Hello, World!".

```m
Text.PositionOfAny("Hello, World!", {"H", "W"})
```

// Output
```
0
```

### Example 2

Find all the positions of "W" or "H" in text "Hello, World!".

```m
Text.PositionOfAny("Hello, World!", {"H", "W"}, Occurrence.All)
```

// Output
```
{0, 7}
```

