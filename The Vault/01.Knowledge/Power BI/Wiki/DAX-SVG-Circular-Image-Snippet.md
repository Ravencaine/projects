---
created: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: snippet
tags: [dax, svg, base64, image, circular, snippet]
---

# DAX SVG Circular Image Measure — Copy-Paste

DAX measure that generates an SVG circular profile image for a Power BI table visual. Requires a `Base64` text column produced by `fxImageToBase64` in Power Query.

## Code

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

## When to Use

Drop this measure into any Power BI table visual where you want a circular thumbnail image. Replace `'Employees'[ImageBase64]` with your own table and column names.

## Requirements

- Power Query `fxImageToBase64` must have been run on the image URL column first
- The resulting `ImageBase64` column must be in the same table as the DAX measure
- In the table visual, set the measure's data format to **Image URL**

## Variations

| Variation | Change |
|-----------|--------|
| No grey background circle | Remove the `<circle fill=""#eeeeee"" />` line |
| Larger circle | Increase `cx`, `cy`, `r` and `width`/`height` proportionally; adjust `viewBox` |
| Colored status ring | Add a second `<circle>` with a dynamic `fill` before the `<image>` tag |
| Rounded rectangle (not circle) | Replace `<circle>` with `<rect rx=""..."">` in the `clipPath` and background |

## Related

- [[Circular-Image-Power-BI-Table-Pattern]]
- [[DAX-SVG-Profile-Card-Snippet]]
- [[fxImageToBase64-Power-Query]]
- [[SVG-in-Power-BI-Key-Concepts]]
