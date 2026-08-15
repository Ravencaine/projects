---
created: 2026-08-14
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: function
tags: [power-query, m-code, base64, image, function, web-contents, binarytotext]
---

# URL-to-Base64 — Power Query M Function

Downloads an image from a URL and returns it as a Base64-encoded data URL string. The foundational function for embedding images inside DAX SVG measures or any scenario where Power BI needs the image as inline text rather than an external URL.

## Signature

```m
URL-to-Base64 = (imageUrl as text) as text
```

## Definition

```m
// URL-to-Base64
let
    URL-to-Base64 = (imageUrl as text) as text =>
    let
        Source   = Web.Contents(imageUrl),
        AsBase64 = Binary.ToText(Source, BinaryEncoding.Base64),
        DataUrl  = "data:image/jpeg;base64," & AsBase64
    in
        DataUrl
in
    URL-to-Base64
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `imageUrl` | `text` | The full URL of the image to download |

## Returns

`text` — a data URL of the form `data:image/jpeg;base64,<base64_string>`

Change `image/jpeg` to `image/png` (or `image/gif`) to match the actual source format.

## Usage

1. **Create the function:** Home → New Source → Blank Query → open Advanced Editor → paste the definition → rename query to `URL-to-Base64`
2. **Invoke on a column:** Add Column → Invoke Custom Function → Function: `URL-to-Base64` → Argument: your URL column → name the new column `ImageBase64`
3. **Wire in Power BI:** Set the Data category on the URL column to **Image URL**; bind in a visual that accepts images (Card, Table, Multi-row Card)

## 32k Character Limit

Power BI text columns cap at ~32,767 characters. A typical non-tiny image produces a base64 string far exceeding this. When this function produces a blank or truncated image in Power BI:

- See [[pre-resize-images-before-base64-encoding]] — the image must be resized before encoding
- See [[URL-to-Base64-Compressed-Power-Query]] — adds a resize step via the resize.now API

## Notes

- Requires internet access at refresh time; Power BI privacy levels must allow the image domain
- `Web.Contents` respects any auth the URL needs — private Dropbox/OneDrive links work if credentials are cached
- Base64 strings bloat the model size — use for reasonably sized images (avatars, thumbnails, product photos)

## Related

- [[URL-to-Base64-Compressed-Power-Query]] — resize before encoding to avoid 32k limit
- [[Circular-Image-Power-BI-Table-Pattern]] — the full pattern this function enables
- [[fxImageToBase64-Power-Query]] — similar function from Isabelle Bittar's pattern (uses `image/jpeg` prefix only)
