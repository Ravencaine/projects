---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [text, m-function]
---


# Text.PadEnd

Returns a text value padded to length count by inserting spaces at the end of the text value text. An optional character character can be used to specify the character used for padding. The default pad character is a space.

## Signature

```m
Text.PadEnd(
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

Pad the end of a text value so it is 10 characters long.

```m
Text.PadEnd("Name", 10)
```

// Output
```
"Name "
```

### Example 2

Pad the end of a text value with "|" so it is 10 characters long.

```m
Text.PadEnd("Name", 10, "|")
```

// Output
```
"Name|"
```

