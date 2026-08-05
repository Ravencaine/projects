---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["character", "m-function"]
---


# Character.ToNumber

Returns the number equivalent of the character. The result will be the 21-bit Unicode code point represented by the provided character or surrogate pair.

## Signature

```m
Character.ToNumber(character as nullable text) as nullable number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| character | nullable text | |

## Returns

nullable number

### Example 1

Convert a character to its equivalent number value.

```m
Character.ToNumber("#(tab)")
```

// Output
```
9
```

### Example 2

Convert the UTF-16 surrogate pair for the "grinning face" emoticon to its equivalent hexadecimal code point.

```m
Number.ToText(Character.ToNumber("#(0001F600)"), "X")
```

// Output
```
"1F600"
Last updated on 04/03/2026
```

