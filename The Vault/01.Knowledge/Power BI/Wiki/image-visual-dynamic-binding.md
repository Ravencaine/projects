---
created: 2026-08-02
updated: 2026-08-05
source: The New Image Visual in Power BI Is a Quiet Game Changer
note_type: atomic
tags: [power-bi, image-visual, dynamic-binding, dax, svg, url]
---

# Image Visual Dynamic Binding — Fields, Measures, URLs, SVG

The Image visual can now bind to any of these sources, enabling fully dynamic images that react to filters, slicers, and measure logic.

## Binding Options

| Source | Description | Example |
|--------|-------------|---------|
| **Field** | Column containing image URLs | `Product[ImageURL]` |
| **DAX measure** | Measure returning a URL or SVG string | `[Status Icon]` |
| **Calculated URL** | DAX `SELECTEDVALUE` or `IF` returning a URL | Dynamic category logo |
| **SVG string** | URL-encoded SVG via `UDF_EncodeSVG` | `[[udf_encodesvg-url-encoder-for-svg]]` |

## Key Capability

> **One DAX measure → infinite visual states.**

The same measure can return different image URLs or SVG strings based on the current filter context.

## Example: Dynamic Status Icon

```c
Status Icon :=
    SWITCH(
        TRUE(),
        [Risk Score] <= 3, "https://example.com/green-dot.png",
        [Risk Score] <= 6, "https://example.com/yellow-dot.png",
        "https://example.com/red-dot.png"
    )
```

## For SVG Content

Use `UDF_EncodeSVG` from `[[svg-pill-pattern-udf-based]]`:

```c
Status SVG := UDF_EncodeSVG("<circle fill='#59A14F' .../>")
```

Bind the measure to the Image visual — no table container needed.

## Related

- [[image-visual-as-design-system-container]]
- [[udf_encodesvg-url-encoder-for-svg]]
- [[svg-visualizations-in-power-bi]]
