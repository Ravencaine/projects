---
created: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: reference
tags: [power-query, m-code, base64, binarytotext, reference, web-contents]
---

# Power Query Base64 Conversion — Key Concepts

Essential M functions and concepts for converting image URLs to Base64 text in Power Query.

## Quick Reference

| Function | Syntax | Purpose |
|----------|--------|---------|
| `Web.Contents` | `Web.Contents(url)` | Downloads content from a URL — returns binary |
| `Binary.ToText` | `Binary.ToText(binary, BinaryEncoding.Base64)` | Converts binary to a Base64 string |
| `BinaryEncoding.Base64` | `BinaryEncoding.Base64` | Encoding constant for Base64 output |

## The Pattern

```m
let
    Source  = Web.Contents(ImageUrl),          // download as binary
    AsBase64 = Binary.ToText(Source, BinaryEncoding.Base64),
    DataUrl  = "data:image/jpeg;base64," & AsBase64  // prepend media type
in
    DataUrl
```

## Data URL Format

`data:<media-type>;base64,<base64-string>`

| Media type | Use for |
|-----------|---------|
| `data:image/jpeg;base64,` | JPG images |
| `data:image/png;base64,` | PNG images |
| `data:image/gif;base64,` | GIF images |

## Notes

- **Privacy levels:** `Web.Contents` is subject to Power Query privacy levels — the target domain must be accessible under the current privacy setting
- **One-time cost:** The Base64 string is computed once and stored as text — no re-download on each refresh
- **Model size impact:** Base64 strings are ~33% larger than the original binary. For large image libraries, this can significantly bloat the PBIX file size
- **Stored as text:** After conversion, the `ImageBase64` column is just text — it can be loaded to the model and used in DAX measures without re-executing the web request
- **JPG vs PNG:** Set the correct media type in the prefix — mismatched types don't break rendering but may affect display in some contexts

## Related

- [[fxImageToBase64-Power-Query]]
- [[Circular-Image-Power-BI-Table-Pattern]]
- [[Image-Masking-Limitation-Power-BI]]
