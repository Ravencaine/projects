---
created: 2026-08-05
updated: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: pattern
tags: [svg, base64, image, circular, power-bi, dax, power-query, pattern]
---

# Circular Image in Power BI Table (SVG + Base64)

Display rectangular images as circular thumbnails inside Power BI table visuals — using Power Query to convert image URLs to Base64, then DAX to generate an SVG circular clipPath.

## Purpose

Power BI has no native image masking. This pattern works around that by: (1) embedding the image as Base64 text in Power Query, then (2) using DAX to generate an SVG that clips the Base64 image into a circle.

## Why the Pattern Works

Power BI blocks external image URLs referenced from inside SVGs. The solution: store the image as a Base64 data URL string — not an external URL — and let SVG handle only the shape.

## Components

| Step | Tool | What it does |
|------|------|-------------|
| 1 — Download & encode | Power Query `fxImageToBase64` | Downloads image URL, returns Base64 data URL |
| 2 — Store as text | Power Query custom column | Adds `ImageBase64` column to the table |
| 3 — Generate SVG | DAX measure | Builds `data:image/svg+xml;utf8,<svg>...</svg>` string |
| 4 — Set format | Power BI table visual | Column data format → Image URL |

## Structure

### Step 1 — Power Query: `fxImageToBase64`

```m
let
    fxImageToBase64 = (ImageUrl as text) as text =>
    let
        Source   = Web.Contents(ImageUrl),
        AsBase64 = Binary.ToText(Source, BinaryEncoding.Base64),
        DataUrl  = "data:image/jpeg;base64," & AsBase64
    in
        DataUrl
in
    fxImageToBase64
```

Invoke it on the image URL column → new column `ImageBase64`.

### Step 2 — DAX: Circular Profile Image Measure

```dax
Profile Image (SVG) =
VAR ImgDataUrl = SELECTEDVALUE('Employees'[ImageBase64])
RETURN
    IF(
        NOT ISBLANK(ImgDataUrl),
        "data:image/svg+xml;utf8," &
        "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 150 60"">" &
            "<defs>" &
                "<clipPath id=""clipCircle"">" &
                    "<circle cx=""50"" cy=""50"" r=""50"" />" &
                "</clipPath>" &
            "</defs>" &
            "<circle cx=""50"" cy=""50"" r=""50"" fill=""#eeeeee"" />" &
            "<image href=""" & ImgDataUrl & """ " &
                "x=""0"" y=""0"" width=""100"" height=""100"" " &
                "preserveAspectRatio=""xMidYMid slice"" " &
                "clip-path=""url(#clipCircle)"" />" &
        "</svg>"
    )
```

### Step 3 — Power BI Table Visual

1. Add the DAX measure to a table visual
2. Select the column → **Data format: Image URL**
3. Adjust the table visual's image height to match the SVG `viewBox`

## Key SVG Parameters

| Parameter | Value | Effect |
|-----------|-------|--------|
| `viewBox` | `"0 0 150 60"` | SVG coordinate system — set to match your layout |
| `clipPath` circle `r` | `50` | Radius of the circular clip — controls final circle size |
| `image` width/height | `100` | Source image dimensions inside the SVG |
| `preserveAspectRatio` | `"xMidYMid slice"` | Centers image and crops overflow to fill circle |

## Variations

- **Different image sizes:** adjust `viewBox`, circle `cx/cy/r`, and image `width/height` proportionally
- **Fallback when image is missing:** wrap the `<image>` element in `IF(NOT ISBLANK(ImgDataUrl), ...)` as shown
- **Colored status border:** add a second `<circle>` behind the clipped image with a status-based `fill`
- **Initials fallback:** use DAX `SUBSTITUTE` logic to show text initials when `ImgDataUrl` is blank

## Related

- [[DAX-SVG-Circular-Image-Snippet]]
- [[DAX-SVG-Profile-Card-Snippet]]
- [[fxImageToBase64-Power-Query]]
- [[SVG-in-Power-BI-Key-Concepts]]
- [[Circular-Image-Parameters-Reference]]
- [[Image-Masking-Limitation-Power-BI]]
- [[Power-Query-Base64-Conversion-Reference]]
