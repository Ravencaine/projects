---
created: 2026-08-05
updated: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: snippet
tags: [dax, svg, base64, image, profile-card, circular, snippet]
---

# DAX SVG Profile Card Measure — Copy-Paste

DAX measure that generates an SVG profile card: circular avatar on the left + bold name + grey email text on the right, all in one table cell.

## Code

```dax
Profile Card (SVG) =
VAR ImgDataUrl = SELECTEDVALUE('Employees'[ImageBase64])
VAR _Name  = SELECTEDVALUE('Employees'[Member])
VAR Email  = SELECTEDVALUE('Employees'[Email])

VAR NameEsc  = SUBSTITUTE(_Name,  "&", "&amp;")
VAR EmailEsc = SUBSTITUTE(Email, "&", "&amp;")

RETURN
    IF(
        NOT ISBLANK(_Name),
        "data:image/svg+xml;utf8," &
        "<svg xmlns=""http://www.w3.org/2000/svg"" viewBox=""0 0 320 60"">"

            "<defs>"
                "<clipPath id=""clipCircle"">"
                    "<circle cx=""30"" cy=""30"" r=""24"" />"
                "</clipPath>"
            "</defs>"

            "<circle cx=""30"" cy=""30"" r=""24"" fill=""#eeeeee"" />"

            IF(
                NOT ISBLANK(ImgDataUrl),
                "<image href=""" & ImgDataUrl & """ " &
                    "x=""6"" y=""6"" width=""48"" height=""48"" " &
                    "preserveAspectRatio=""xMidYMid slice"" " &
                    "clip-path=""url(#clipCircle)"" />",
                ""
            )

            "<style>"
                ".name  { font-family:'Segoe UI Light', sans-serif; font-size:14px; font-weight:600; fill:#111111; }"
                ".email { font-family:'Segoe UI Light', sans-serif; font-size:11px; fill:#888888; }"
            "</style>"

            "<text x=""70"" y=""26"" class=""name"">"  & NameEsc  & "</text>"
            "<text x=""70"" y=""42"" class=""email"">" & EmailEsc & "</text>"

        "</svg>"
    )
```

## When to Use

Use this when a single table cell needs to show both a circular avatar and associated metadata (name, role, department, email). Replaces multiple columns in a table visual with one self-contained measure.

## Requirements

- `fxImageToBase64` Power Query function must have been run to produce `ImageBase64`
- `Member` and `Email` columns must be in the same table as the measure
- Table visual column data format: **Image URL**

## Key Details

- `&amp;` escaping: `SUBSTITUTE` replaces `&` with `&amp;` to produce valid XML
- CSS `<style>` block inside the SVG: controls font-family, size, weight, and fill colour
- `<text>` `y` positions: `26` (name baseline), `42` (email baseline) — chosen to vertically centre in the 60px viewBox height
- Avatar area: left 60px (viewBox `"0 0 320 60"`, circle at `cx=30`); text starts at `x=70`

## Related

- [[DAX-SVG-Circular-Image-Snippet]]
- [[Circular-Image-Power-BI-Table-Pattern]]
- [[SVG-in-Power-BI-Key-Concepts]]
