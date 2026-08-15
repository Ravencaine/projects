---
created: 2026-08-14
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: snippet
tags: [dax, svg, base64, image, circular, snippet, clippath]
---

# DAX SVG Circular Image Measure (3 Hacks Version)

DAX measure that wraps an image URL in an SVG with a circular `<clipPath>` — the third and most flexible approach from the "3 Hacks" video. Unlike the [[DAX-SVG-Circular-Image-Snippet]] (Isabelle Bittar version), this version uses the `ImageCircle` variable name and points to the compressed Base64 column produced by [[URL-to-Base64-Compressed-Power-Query]].

## Code

```dax
Image Circle =
VAR ImgDataUrl = SELECTEDVALUE('Table'[ImageBase64Compressed])
RETURN
    IF(
        NOT ISBLANK(ImgDataUrl),
        "data:image/svg+xml;utf8," &
        "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 100 100"">" &
            "<defs>" &
                "<clipPath id=""circleView"">" &
                    "<circle cx=""50"" cy=""50"" r=""45"" />" &
                "</clipPath>" &
            "</defs>" &
            "<image href=""" & ImgDataUrl & """ " &
                "x=""0"" y=""0"" width=""100"" height=""100"" " &
                "preserveAspectRatio=""xMidYMid slice"" " &
                "clip-path=""url(#circleView)"" />" &
        "</svg>"
    )
```

## When to Use

Drop this measure into any Power BI visual where you want a circular thumbnail image rendered from a Base64 data URL column. Bind the measure to the visual and set its data format to **Image URL**.

This is Approach C from [[circular-image-approaches-decision-guide]] — use when:
- You only have image URLs (not local files)
- Images need to appear inside tables, matrices, or lists (scrolling contexts where [[circular-overlay-mask-powerpoint-power-bi]] breaks)
- Content changes dynamically (new employees, updated photos, etc.)

## Requirements

- A Base64 text column in the same table as the measure — produced by [[URL-to-Base64-Power-Query]] (small images) or [[URL-to-Base64-Compressed-Power-Query]] (large images)
- The measure's data format in the visual set to **Image URL**
- The visual must support image rendering (Card, Table, Multi-row Card, Matrix)

## Key Parameters

| Parameter | Value | Effect |
|-----------|-------|--------|
| `viewBox` | `"0 0 100 100"` | SVG coordinate space — set to match desired display size |
| `clipPath` circle `cx/cy` | `50/50` | Centers the clip circle in the SVG |
| `clipPath` circle `r` | `45` | Radius slightly less than 50 — clips the outer edge cleanly |
| `image width/height` | `100/100` | Source image dimensions inside the SVG |
| `preserveAspectRatio` | `"xMidYMid slice"` | Centers image and crops overflow to fill the circle |

## Variations

| Variation | Change |
|-----------|--------|
| No grey ring (transparent background) | Remove any background `<circle>` element |
| Larger circle | Increase `cx`, `cy`, `r` and `width`/`height` proportionally |
| Rounded rectangle instead of circle | Replace `<circle cx="50" cy="50" r="45" />` with `<rect x="0" y="0" width="100" height="100" rx="15" />` in both the `<clipPath>` and any background element |
| Dynamic radius via measure | Replace the hard-coded `45` with a DAX expression returning a number |

## Gotcha — SVG Measure Fails Silently with External URLs

Power BI blocks external image URLs inside SVG `<image href>`. The image appears blank with no error. **Always use a Base64 data URL** (`data:image/...;base64,...`) in the `ImgDataUrl` variable — never a raw `https://...` URL.

If the URL column is not Base64-encoded, the image renders as a broken/blank thumbnail.

## Related

- [[DAX-SVG-Circular-Image-Snippet]] — Isabelle Bittar's version (different variable name, same mechanics)
- [[URL-to-Base64-Compressed-Power-Query]] — produces the `ImageBase64Compressed` column this measure reads
- [[circular-image-approaches-decision-guide]] — when to use this approach vs. the other two hacks
- [[SVG-in-Power-BI-Key-Concepts]] — reference for SVG mechanics in Power BI
