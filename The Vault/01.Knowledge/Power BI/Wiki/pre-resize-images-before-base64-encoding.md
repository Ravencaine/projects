---
created: 2026-08-14
source: 3 Hacks to Turn Any Image into a Circle in Power BI (datatraining.io + video)
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: atomic
tags: [power-bi, base64, image-resize, compression, m-function, external-api, 32k-limit]
---

# Pre-Resize Images Before Base64 Encoding (External API)

Power BI's text column limit (~32,767 characters) truncates raw base64 strings for any non-tiny image, so a base64 SVG + clipPath circular-image measure appears blank when the underlying image exceeds the limit. The fix: **compress and resize the image before encoding**.

## Why the Standard `Binary.ToText` Function Fails

`Binary.ToText([Content], BinaryFormat.Base64)` (the only base64 helper in M) does not compress or resize — it just emits the raw bytes as base64. A typical 500×500 PNG balloon to 700 KB+ of base64 text; multi-megapixel images are unusable.

## External API Approach (datatraining.io pattern)

The video ([exTSUPJPSqE](https://www.youtube.com/watch?v=exTSUPJPSqE)) demonstrates an M custom function that calls **resize.now** (a free image-resize API) before encoding:

```m
// "URL to base64 compression" custom function (sketch)
(imageUrl as text) as text =>
let
    // 1. Strip Dropbox suffix if present (sample-specific)
    Cleaned = if Text.EndsWith(imageUrl, "?dl=0") then
                  Text.Replace(imageUrl, "?dl=0", "?raw=1")
              else imageUrl,

    // 2. Resize / compress via external API
    Resized = Web.Contents("https://resize.now/?url=" & Cleaned & "&w=128&h=128"),

    // 3. Encode the resized bytes
    Encoded = Binary.ToText(Resized, BinaryFormat.Base64),

    // 4. Add MIME prefix (PNG/JPEG/GIF)
    Result = "data:image/png;base64," & Encoded
in
    Result
```

## When to Use

- You only have image URLs (not files) — Approach C from [[circular-image-approaches-decision-guide]].
- The image set has too many entries to pre-process manually.
- New images appear regularly and you can't round-trip them through PowerPoint.

## Trade-offs

| Concern | Detail |
|---------|--------|
| **External API dependency** | The third-party service must be reachable at refresh time and accept your images. Confirm ToS before sending PII / internal assets. |
| **Latency** | Each row hits the API — refresh time scales with image count. |
| **Quality** | Re-encoding loses detail; profile photos at 128×128 are visually fine, headshots at higher resolutions may need a larger size. |
| **MIME type** | The prefix must match the actual image type (`png`/`jpeg`/`gif`) or the image fails to render. |

## Alternative — Resize on Disk

If you control the source files, skip the API and re-save them with the [[batch-circularize-images-with-python]] flow (Pillow `thumbnail(...)` then base64). Same downstream measure, no external dependency.

## Related

- [[Binary-Base64-Image-Model]] — base64 in the model + the 32k limit
- [[Circular-Image-Power-BI-Table-Pattern]] — full pattern that uses this compression step
- [[batch-circularize-images-with-python]] — local-only alternative (no API)
- [[circular-image-approaches-decision-guide]] — Approach C
