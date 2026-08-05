---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.FromText

Returns the result of converting text value text to a binary (list of number). encoding may be specified to indicate the encoding used in the text value. The following BinaryEncoding values may be used for encoding. BinaryEncoding.Base64: Base 64 encoding BinaryEncoding.Hex: Hex encoding

## Signature

```m
Binary.FromText(text as nullable text, optional encoding as nullable number) as
nullable binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| text | nullable text | |
| optional encoding | nullable number | |

## Returns

nullable binary

### Example 1

Decode "1011" into binary.

```m
Binary.FromText("1011")
```

// Output
```
Binary.FromText("1011", BinaryEncoding.Base64)
```

### Example 2

Decode "1011" into binary with Hex encoding.

```m
Binary.FromText("1011", BinaryEncoding.Hex)
```

// Output
```
Binary.FromText("EBE=", BinaryEncoding.Base64)
Last updated on 04/02/2026
```

