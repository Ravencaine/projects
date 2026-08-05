---
created: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: atomic
tags: [power-bi, image, local-image, insert, static, logo]
---

# Local Image Import: Insert → Image

The simplest image import method: use the Insert ribbon to drop an image from the local machine directly onto the report canvas.

## Steps

1. **Home → Insert** (ribbon tab)
2. **Image** button (in the Elements section)
3. Select the image file → **Open**

The image is embedded in the PBIX.

## Best Use Cases

- Static branding elements: logos, report headers, watermark-style background images
- Decorative shapes or icons that never change
- One-off profile pictures or decorative graphics

## Limitations

| Limitation | Detail |
|-----------|--------|
| PBIX size | Image adds to PBIX file size — large images bloat the report |
| No dynamic selection | The image is static; cannot switch between images based on a slicer or measure |
| Performance | Many embedded images slow report load time |
| Offline | Works offline, but the PBIX must be republished to update images |

## When to Use

Use for truly static, never-changing assets (brand logos, report backgrounds). For anything that needs to vary by data context, use the [[Web-Image-URL-Measure]] or [[Binary-Base64-Image-Model]] approach instead.

## Related

- [[Web-Image-URL-Measure]]
- [[Binary-Base64-Image-Model]]
- [[SVG-Images-Power-BI]]
