---
created: 2026-08-05
updated: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: reference
tags: [power-query, binarytotext, base64, image, binary]
---

# Binary.ToText — Power Query Binary to Base64

Power Query M function that converts binary data to a base64-encoded text string — the core step in embedding images directly in the Power BI model.

## Function Signature

```m
Binary.ToText(binary as binary, encoding as BinaryEncoding.Type) as text
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `binary` | `binary` | The binary content of the file (from a Folder connector, Web.Contents, or binary column) |
| `encoding` | `BinaryEncoding.Type` | The encoding format: `BinaryFormat.Base64` or `BinaryFormat.Hex` |

## Usage for Images

```m
Binary.ToText([Content], BinaryFormat.Base64)
```

Returns the raw base64 string (without the MIME prefix). The result is prepended with `data:image/png;base64,` (or the appropriate MIME type) to create a data URI.

## Complete Pattern

```m
let
    Source = Folder.Files("C:\Images"),
    Filtered = Table.SelectRows(Source, each [Extension] = ".png"),
    WithBase64 = Table.AddColumn(
        Filtered,
        "ImageData",
        each "data:image/png;base64," & Binary.ToText([Content], BinaryFormat.Base64)
    )
in
    WithBase64
```

## BinaryFormat.Base64 vs BinaryFormat.Hex

| Encoding | Output | Use case |
|----------|--------|----------|
| `BinaryFormat.Base64` | Base64 string | Images for Power BI Image URL data category |
| `BinaryFormat.Hex` | Hex string | Debugging binary content |

## Related

- [[Binary-Base64-Image-Model]]
- [[Power-Query-Base64-Conversion-Reference]]
