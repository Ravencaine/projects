---
created: 2026-08-13
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: comparison
tags: [circular-image, decision-guide, image-url, png, svg, base64, comparison]
---

# Circular Image Approaches — Decision Guide

Three practical paths to circular images in Power BI, picked by what you have on hand (files vs URLs), how many images there are, and whether they live in fixed positions or scrollable tables.

## Summary

Use the **cheapest approach that fits your scenario**. Pre-process a handful of files in PowerPoint; batch a hundred in Python; mask a fixed-position card; only drop to SVG + Base64 when you have nothing but URLs and need them inside tables.

## Quick Decision Table

| Situation | Best Approach |
|-----------|---------------|
| A handful of local image files; you can update them once | A. Pre-process in PowerPoint or Python |
| Images always in a fixed position (e.g. card header) | B. Circular overlay (mask) |
| Only image URLs available; images inside tables/lists; content changes regularly | C. SVG measure with Base64 (see [[circular-image-power-bi-table-pattern]]) |

## Approach A — Pre-Process to Circular PNG

### When
You have the actual files (not just URLs) and the list rarely changes.

### Methods
- **Manual (small set, <20):** [[pre-circularize-images-in-powerpoint]] — open in PowerPoint, Crop to Shape → Oval, Save as Picture → PNG.
- **Script (large set):** [[batch-circularize-images-with-python]] — Pillow script that applies a circular mask to every file in a folder.

### Pros
- Output is a normal raster — works in every image-aware visual (Card, Table, Matrix, Multi-row Card, Slicer image).
- Zero code, zero model changes (manual path).
- Scales (Python path).

### Cons
- One-shot batch — new images require a re-run.
- Original image URL becomes orphaned (the circular version is a separate file).
- No dynamic switching back to the square version.

## Approach B — Circular Overlay (Mask)

### When
Images live in a fixed, non-scrolling position on a page (e.g. a profile card header).

### Method
[[circular-overlay-mask-powerpoint-power-bi]] — build a mask PNG in PowerPoint (rectangle + circle + Combine), then layer it on top of the original image in Power BI.

### Pros
- Original image file stays untouched.
- Quick to set up (one PowerPoint action).
- Output is a circular-looking image — no model changes.

### Cons
- **Breaks inside tables/matrices** — the overlay visual doesn't scroll with rows.
- Mask colour must match report background; theme changes require a re-export.
- Pixel alignment is fiddly at non-default DPI.

## Approach C — SVG Measure with Base64

### When
You only have URLs, you need circular images inside tables/lists, and the content changes regularly.

### Method
See [[circular-image-power-bi-table-pattern]] and [[DAX-SVG-Circular-Image-Snippet]] — Power Query function converts URL → Base64; DAX measure builds SVG with `<clipPath><circle/></clipPath>`; rendered in a table visual with Image URL format.

### Pros
- Dynamic — re-renders if the URL or its content changes.
- Works inside scrolling tables and matrices.
- Single source of truth — no separate PNG to manage.

### Cons
- 32k character column limit — large images overflow; pre-resize/compress before encoding.
- Requires DAX + Power Query complexity.
- Some visuals (older Card variants) don't accept the SVG string format.
- Image source must be reachable at refresh time unless embedded.

## Comparison Table

| Criterion | A — Pre-process | B — Overlay mask | C — SVG + Base64 |
|-----------|-----------------|------------------|-------------------|
| Have files vs only URLs | Files | Files | URLs OK |
| Scalability (count) | Manual: ~20 / Python: 1000s | One image at a time | Hundreds (URL-bound) |
| Works in tables/matrices | ✅ | ❌ | ✅ |
| Original image preserved | ❌ (replaced) | ✅ | ✅ (URL) |
| Requires code/script | Manual: no / Python: yes | No | Yes (DAX + M) |
| Reacts to image changes | Manual re-export | Re-align | Auto (re-renders) |
| Best for | Profile photos, logos, icons | Hero images in card headers | Avatar columns in tables |

## When to Combine

- Approach **A** for static logos/branding across the report (once).
- Approach **C** for user-uploaded photos that change in the source data.
- Approach **B** rarely — only for design-heavy hero placements.

## Related

- [[circular-image-power-bi-table-pattern]] — full pattern for Approach C
- [[DAX-SVG-Circular-Image-Snippet]] — copy-paste DAX for Approach C
- [[fxImageToBase64-Power-Query]] — Power Query function for Approach C
- [[SVG-in-Power-BI-Key-Concepts]] — reference for the SVG mechanics
