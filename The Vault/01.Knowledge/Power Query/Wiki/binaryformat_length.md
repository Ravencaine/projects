---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binaryformat", "m-function"]
---


# BinaryFormat.Length

Returns a binary format that limits the amount of data that can be read. Both BinaryFormat.List and BinaryFormat.Binary can be used to read until end of the data. BinaryFormat.Length can be used to limit the number of bytes that are read. The binaryFormat parameter specifies the binary format to limit. The length parameter specifies the number of bytes to read. The length parameter may either be a number value, or a binary format value that specifies the format of the length value that appears that precedes the value being read.

## Signature

```m
BinaryFormat.Length(binaryFormat as function, length as any) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binaryFormat | function | |
| length | any | |

## Returns

function

### Example 1

Limit the number of bytes read to 2 when reading a list of bytes.

```m
let
binaryData = #binary({1, 2, 3}),
listFormat = BinaryFormat.Length(
BinaryFormat.List(BinaryFormat.Byte),
2
)
in
listFormat(binaryData)
```

// Output
```
{1, 2}
```

### Example 2

Limit the number of byte read when reading a list of bytes to the byte value preceding the list.

```m
let
binaryData = #binary({1, 2, 3}),
listFormat = BinaryFormat.Length(
BinaryFormat.List(BinaryFormat.Byte),
BinaryFormat.Byte
)
in
listFormat(binaryData)
```

// Output
```
{2}
```

