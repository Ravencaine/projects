---
created: 2026-08-14
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: function
tags: [power-query, m-code, base64, image, compression, resize, external-api, function, 32k-limit]
---

# URL-to-Base64-Compressed — Power Query M Function

Downloads an image from a URL, resizes it via an external API (to shrink the base64 output below Power BI's 32,767 character column limit), then returns it as a Base64-encoded data URL. Use this when [[URL-to-Base64-Power-Query]] produces blank or truncated images because the raw base64 string exceeds the limit.

## Signature

```m
URL-to-Base64-Compressed = (imageUrl as text) as text
```

## Definition

```m
// URL-to-Base64-Compressed
let
    URL-to-Base64-Compressed = (imageUrl as text) as text =>
    let
        // 1. Normalise the URL (Dropbox dl=0 → raw=1)
        Cleaned = if Text.EndsWith(imageUrl, "?dl=0") then
                      Text.Replace(imageUrl, "?dl=0", "?raw=1")
                  else imageUrl,

        // 2. Resize via resize.now API (width=128, height=128)
        Resized = Web.Contents(
            "https://resize.now/?url=" & Cleaned & "&w=128&h=128"
        ),

        // 3. Encode the resized bytes to base64
        Encoded = Binary.ToText(Resized, BinaryEncoding.Base64),

        // 4. Add MIME prefix (PNG for resize.now output)
        Result  = "data:image/png;base64," & Encoded
    in
        Result
in
    URL-to-Base64-Compressed
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `imageUrl` | `text` | The full URL of the image to download and resize |

## Returns

`text` — a data URL of the form `data:image/png;base64,<base64_string>`

resize.now always returns PNG output at the requested dimensions.

## Usage

1. **Create the function:** Home → New Source → Blank Query → open Advanced Editor → paste the definition → rename to `URL-to-Base64-Compressed`
2. **Strip the Dropbox suffix:** The function includes a Dropbox-specific `?dl=0 → ?raw=1` normalisation step. Remove or adapt this for other hosts.
3. **Invoke:** Add Column → Invoke Custom Function → Function: `URL-to-Base64-Compressed` → Argument: your URL column → name the new column `ImageBase64Compressed`
4. **Wire in DAX:** Update the SVG measure to reference the compressed column instead of the raw Base64 column

## Why the Resize Step Is Required

| Image source | Approximate raw base64 size |
|--------------|---------------------------|
| 500×500 PNG avatar | ~700 KB → 900k+ chars |
| 128×128 PNG avatar | ~20–50 KB → 27–68k chars (fits) |

Power BI's text column hard limit is ~32,767 characters. The resize step brings most images under the threshold.

## External API Dependency

resize.now is a third-party service. Considerations:

- The service must be reachable at every refresh
- Confirm the resize.now Terms of Service allow your image types before sending internal or PII images
- Latency scales with image count — each row hits the API once
- If resize.now is unavailable, the column fails at refresh time

## Notes

- The `?dl=0 → ?raw=1` normalisation is Dropbox-specific — remove or replace for other hosts
- resize.now always outputs PNG regardless of the source format
- 128×128 is sufficient for avatar/thumbnail use cases; increase `w=` and `h=` for larger display sizes (watch the 32k limit)
- For local files, the [[batch-circularize-images-with-python]] approach avoids the external API entirely

## Related

- [[URL-to-Base64-Power-Query]] — the uncompressed version (use when images are already small)
- [[pre-resize-images-before-base64-encoding]] — the concept note explaining why compression is needed
- [[Circular-Image-Power-BI-Table-Pattern]] — full pattern that uses this function
- [[batch-circularize-images-with-python]] — local-only alternative (no external API)
