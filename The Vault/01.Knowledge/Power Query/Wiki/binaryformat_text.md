---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binaryformat", "m-function"]
---


# BinaryFormat.Text

Returns a binary format that reads a text value. The length specifies the number of bytes to decode, or the binary format of the length that precedes the text. The optional encoding value specifies the encoding of the text. If the encoding is not specified, then the encoding is determined from the Unicode byte order marks. If no byte order marks are present, then TextEncoding.Utf8 is used.

## Signature

```m
BinaryFormat.Text(length as any, optional encoding as nullable number) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| length | any | |
| optional encoding | nullable number | |

## Returns

function

### Example 1

Decode two bytes as ASCII text.

```m
let
binaryData = #binary({65, 66, 67}),
textFormat = BinaryFormat.Text(2, TextEncoding.Ascii)
in
textFormat(binaryData)
```

// Output
```
"AB"
```

### Example 2

Decode ASCII text where the length of the text in bytes appears before the text as a byte.

```m
Power Query M
let
binaryData = #binary({2, 65, 66}),
textFormat = BinaryFormat.Text(
BinaryFormat.Byte,
TextEncoding.Ascii
)
in
textFormat(binaryData)
```

// Output
```
"AB"
```

