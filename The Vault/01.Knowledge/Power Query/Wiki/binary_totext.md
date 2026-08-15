---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [binary, m-function]
---


# Binary.ToText

Returns the result of converting a binary list of numbers binary into a text value. Optionally, encoding may be specified to indicate the encoding to be used in the text value produced The following BinaryEncoding values may be used for encoding. BinaryEncoding.Base64: Base 64 encoding BinaryEncoding.Hex: Hex encoding --- PAGE 435 ---

## Signature

```m
Binary.ToText(binary as nullable binary, optional encoding as nullable number) as
nullable text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | nullable binary | |
| optional encoding | nullable number | |

## Returns

nullable text

