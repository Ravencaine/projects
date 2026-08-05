---
created: 2026-08-05
updated: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
source_url: https://medium.com/microsoft-power-bi/how-to-create-circular-images-in-power-bi-that-actually-render-properly-6d51849415d6
note_type: function
tags: [power-query, m-code, base64, image, function, web-contents]
---

# fxImageToBase64 — Power Query M Function

Downloads an image from a URL and returns it as a Base64-encoded data URL string, ready to embed inside an SVG.

## Signature

```m
fxImageToBase64 = (ImageUrl as text) as text
```

## Definition

```m
// fxImageToBase64
let
    fxImageToBase64 = (ImageUrl as text) as text =>
    let
        Source    = Web.Contents(ImageUrl),
        AsBase64  = Binary.ToText(Source, BinaryEncoding.Base64),
        DataUrl   = "data:image/jpeg;base64," & AsBase64
    in
        DataUrl
in
    fxImageToBase64
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ImageUrl` | `text` | The full URL of the image to download |

## Returns

`text` — a data URL string of the form `data:image/jpeg;base64,<base64_string>`

Change `image/jpeg` to `image/png` for PNG images.

## Usage

1. Create the function in Power Query (Advanced Editor)
2. In the target table, add a custom column: **Add Column → Invoke Custom Function**
3. Function: `fxImageToBase64`
4. Argument: the existing URL column (e.g., `Employees[Image]`)
5. Name the new column: `ImageBase64`

## Notes

- Works for JPG and PNG images
- Requires internet access — privacy levels must allow the domain
- Base64 strings significantly increase table column size — use for reasonably sized images only
- Ideal for internal assets and controlled demo datasets; not recommended for large image libraries
- One-time preparation step — once stored as text, no re-download needed

## Related

- [[Power-Query-Base64-Conversion-Reference]]
- [[Circular-Image-Power-BI-Table-Pattern]]
- [[Image-Masking-Limitation-Power-BI]]
