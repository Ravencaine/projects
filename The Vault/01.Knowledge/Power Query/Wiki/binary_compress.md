---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.Compress

Compresses a binary value using the given compression type. The result of this call is a compressed copy of the input. Compression types include: Compression.GZip Compression.Deflate Example Compress the binary value. Usage Power Query M Binary.Compress(Binary.FromList(List.Repeat({10}, 1000)), Compression.Deflate) Output #binary({227, 226, 26, 5, 163, 96, 20, 12, 119, 0, 0}) Last updated on 03/24/2026 --- PAGE 424 ---

## Signature

```m
Binary.Compress(binary as nullable binary, compressionType as number) as nullable
binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | nullable binary | |
| compressionType | number | |

## Returns

nullable binary

