---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["character", "m-function"]
---


# Character.FromNumber

Returns the character equivalent of the number. The provided number should be a 21-bit Unicode code point.

## Signature

```m
Character.FromNumber(number as nullable number) as nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| number | nullable number | |

## Returns

nullable text

### Example 1

Convert a number to its equivalent character value.

```m
Character.FromNumber(9)
```

// Output
```
"#(tab)"
```

### Example 2

Convert a character to a number and back again.

```m
Character.FromNumber(Character.ToNumber("A"))
```

// Output
```
"A"
```

### Example 3

Convert the hexadecimal code point for the "grinning face" emoticon to its equivalent UTF-16 surrogate pair.

```m
Character.FromNumber(0x1F600)
```

// Output
```
"#(0001F600)"
```

