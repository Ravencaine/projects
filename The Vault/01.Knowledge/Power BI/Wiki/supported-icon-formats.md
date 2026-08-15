---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: atomic
tags: [power-bi, custom-icons, svg, png, emoji, unicode, base64, atomic]
---

# Supported Icon Formats Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

Power BI theme icons support multiple formats: SVG, PNG, JPEG, GIF, Unicode characters, emoji, Base64-encoded images, and Font Awesome icon codes.

## Format support

| Format | Notes |
|--------|-------|
| SVG | Scalable, lightweight, highly customizable; requires URL transformation |
| PNG | Raster; fixed size; good for complex icons |
| JPEG | Raster; lossy; suitable for photographic icons |
| GIF | Supports animation; fun but can be distracting |
| Unicode | No URL embedding needed; type directly in DAX measure |
| Emoji | Built-in; no embedding needed; type in DAX measure |
| Base64 PNG/JPEG | Embedded inline; larger data strings |
| Font Awesome | Unicode range; accessible via Unicode codes |

## SVG — recommended

SVG is the recommended format for theme icons because:
- Scales without pixelation
- Single color or multi-color
- Compact when URL-encoded
- Fully customizable in Figma, Sketch, Illustrator

## URL encoding requirements by format

| Format | Encoding |
|--------|---------|
| SVG | UTF-8 data URI (`data:image/svg+xml;utf8,...`) |
| PNG/JPEG/GIF | Base64 data URI (`data:image/png;base64,...`) |
| Unicode/emoji | Direct character in DAX measure — no URL encoding |
| Font Awesome | Unicode code in DAX measure |

## Quick source options

- **SVG Repo** (svgrepo.com) — free SVG library
- **Figma:** design custom icons, export as SVG
- **Font Awesome:** icon codes for Unicode embedding
- **Emoji:** system emoji directly in measures

## Related

- [[svg-to-theme-url-transformation]] — SVG URL encoding
- [[custom-icons-json-theme-cell-element-pattern]] — applying icons
