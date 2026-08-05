---
created: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
note_type: reference
tags: [svg, circular-image, power-bi, dax, reference, viewbox, clippath]
---

# Circular Image Pattern Parameters — Quick Reference

Key SVG dimension values and their effects when building circular image measures in DAX.

## Quick Reference

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `viewBox` | `"0 0 150 60"` | Overall SVG canvas size in local coordinates |
| `circle cx` | `50` | Circle centre X — should be at 1/3 of width for left-aligned avatar |
| `circle cy` | `50` | Circle centre Y — centred vertically |
| `circle r` | `50` | Circle radius — half the display diameter |
| `image width` | `100` | Source image width inside SVG (coordinate units) |
| `image height` | `100` | Source image height inside SVG |
| `image x` | `0` | Image top-left X within the SVG |
| `image y` | `0` | Image top-left Y within the SVG |
| `preserveAspectRatio` | `"xMidYMid slice"` | Centers image and fills circle by cropping |
| `fill="#eeeeee"` | Light grey | Background circle fill — contrast during image load |

## Proportional Sizing Rule

For a circle of radius `r`, set `image width` and `image height` to `r * 2` (the full diameter) to ensure the image fully covers the circle without padding.

## Notes

- **For a larger circle:** increase `r`, `cx`, `cy`, and `image width/height` proportionally; shrink `viewBox` width accordingly
- **For the SVG Profile Card:** avatar takes ~60px of the 320px viewBox width; text starts at `x=70` to leave a 10px gap
- **Text `y` values:** `y` in SVG text is the baseline, not the top. For vertical centering in a 60px viewBox: name baseline ≈ `cy + size/3`, email baseline ≈ `cy + size*0.7`

## Related

- [[DAX-SVG-Circular-Image-Snippet]]
- [[DAX-SVG-Profile-Card-Snippet]]
- [[SVG-in-Power-BI-Key-Concepts]]
