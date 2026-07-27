---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["text", "m-function"]
---


# Text.PadStart

Returns a text value padded to length count by inserting spaces at the start of the text value text. An optional character character can be used to specify the character used for padding. The default pad character is a space.

## Signature

```m
Text.PadStart(
text as nullable text,
count as number,
optional character as nullable text
) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| count | number | |
| optional character | nullable text | |

## Returns

nullable text

### Example 1

Pad the start of a text value so it is 10 characters long.

```m
Text.PadStart("Name", 10)
```

// Output
```
" Name"
```

### Example 2

Pad the start of a text value with "|" so it is 10 characters long.

```m
Text.PadStart("Name", 10, "|")
```

// Output
```
"||||||Name"
```

