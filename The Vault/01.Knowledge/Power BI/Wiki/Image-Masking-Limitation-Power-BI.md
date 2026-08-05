---
created: 2026-08-05
updated: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, svg, base64, image-masking, limitation, workaround]
---

# Image Masking Limitation in Power BI

Power BI has no native image masking or cropping. Attempting to use SVG `<image href="external-url.jpg">` inside a table visual produces a broken image icon — because Power BI blocks external image URLs referenced from within SVG markup.

## Definition

Power BI's rendering engine prevents external image URLs from loading inside SVG elements. This is a security/rendering restriction that affects all attempts to use SVG as a masking wrapper for remote images.

## Key Points

- **No built-in image masking:** Power BI has no "make this image a circle" option
- **SVG clipPath is blocked for external URLs:** A naive approach — `<image href="https://example.com/photo.jpg" clip-path="url(#circle)"/>` — fails silently (broken image icon)
- **The workaround:** Download the image, convert to Base64 in Power Query, embed the Base64 string as a `data:` URI inside the SVG. Power BI can render `data:` URGs — only external HTTP(S) URLs are blocked
- **Base64 separation:** The image data (`data:image/jpeg;base64,...`) and the presentation (SVG clipPath, viewBox) must be kept separate — SVG handles shape, Base64 handles the image
- **One-time conversion:** `fxImageToBase64` in Power Query converts URLs to Base64 once; the result is stored as text and reused on every refresh

## The Fix

1. **Power Query:** `Web.Contents(url)` → `Binary.ToText(..., BinaryEncoding.Base64)` → prepend `data:image/jpeg;base64,`
2. **DAX:** Build an SVG with `clipPath` and `<image href="data:image/jpeg;base64,...">` — no external URLs
3. **Power BI:** Set the measure's data format to **Image URL**

## Related

- [[fxImageToBase64-Power-Query]]
- [[Circular-Image-Power-BI-Table-Pattern]]
- [[SVG-in-Power-BI-Key-Concepts]]
- [[Power-Query-Base64-Conversion-Reference]]
