---
created: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: reference
tags: [svg, power-bi, dax, reference, viewbox, clippath, preserveaspectratio]
---

# SVG in Power BI — Key Concepts

Core SVG concepts used when generating SVG strings inside DAX measures for Power BI table visuals.

## Quick Reference

| Concept | SVG Syntax | Purpose |
|---------|-----------|---------|
| **SVG container** | `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 W H">` | Root element — xmlns required, viewBox sets coordinate space |
| **Circular clip** | `<defs><clipPath id="clip"><circle cx="50" cy="50" r="50"/></clipPath></defs>` | Defines the clipping shape |
| **Apply clip** | `clip-path="url(#clip)"` | On any element to constrain it to the clip shape |
| **Smart centering** | `preserveAspectRatio="xMidYMid slice"` | Centers image and fills the clip by cropping excess |
| **Image embedding** | `<image href="data:image/jpeg;base64,..."/>` | Embeds a Base64 image inside SVG — no external URL |
| **Text styling** | `<style>.cls { font-family:...; font-size:...; fill:...; }</style>` | Inline CSS for text elements |
| **Text element** | `<text x="N" y="N" class="cls">content</text>` | Renders text; `y` is the text baseline |
| **Background circle** | `<circle cx="50" cy="50" r="50" fill="#eeeeee"/>` | Optional: contrast fill behind the image |
| **XML escaping** | `SUBSTITUTE(val, "&", "&amp;")` | DAX: escape `&` (and `<`, `>`) for valid XML |
| **DAX data URI** | `"data:image/svg+xml;utf8," & svgString` | Prepend to the SVG string so Power BI renders it as an image |

## Notes

- Power BI requires the data URI prefix (`data:image/svg+xml;utf8,`) on the DAX measure output — without it, Power BI treats the string as plain text
- **External image URLs inside SVGs are blocked by Power BI** — always use Base64 data URLs for the image content
- `preserveAspectRatio="xMidYMid slice"` is the most reliable setting for circular crops: it centers the image (`xMidYMid`) and fills the circle by cropping (`slice`), preventing letterboxing
- `viewBox` units are independent of CSS pixel values — `"0 0 150 60"` means a 150×60 coordinate system; the actual rendered size in the visual is controlled by the table column's image height setting
- The `xmlns` attribute is mandatory: `xmlns="http://www.w3.org/2000/svg"` — without it, some Power BI renderers reject the SVG

## Related

- [[Circular-Image-Power-BI-Table-Pattern]]
- [[DAX-SVG-Circular-Image-Snippet]]
- [[DAX-SVG-Profile-Card-Snippet]]
- [[Image-Masking-Limitation-Power-BI]]
- [[Circular-Image-Parameters-Reference]]
