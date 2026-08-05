---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.Decompress

Decompresses a binary value using the given compression type. The result of this call is a decompressed copy of the input. Compression types include: Compression.GZip Compression.Deflate

## Signature

```m
Binary.Decompress(binary as nullable binary, compressionType as number) as
nullable binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | nullable binary | |
| compressionType | number | |

## Returns

nullable binary

### Example 1

Decompress the binary value.

```m
Binary.Decompress(#binary({115, 103, 200, 7, 194, 20, 134, 36, 134, 74, 134, 84,
6, 0}), Compression.Deflate)
```

// Output
```
#binary({71, 0, 111, 0, 111, 0, 100, 0, 98, 0, 121, 0, 101, 0})
```

