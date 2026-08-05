---
created: 2026-08-02
source: One UDF to Build All Your SVG Pills in Power BI
note_type: atomic
tags: [svg, geometry, dax, pill, dynamic-sizing]
---

# SVG Pill Geometry (Dynamic Sizing)

How `UDF_SVGPillCanvas` computes pill dimensions from the label string — no hard-coded sizes.

## Core Geometry

```
pillW = LEN(label) × charW + hPad + extraLeft
```

| Constant | Value | Purpose |
|----------|-------|---------|
| `fontSize` | 11 | Text size in px |
| `charW` | 6 | Approximate px width per character |
| `hPad` | 9 | Horizontal padding (both sides) |
| `_extraLeft` | 8 or 8 + dotSpace | Left offset for text; includes dot clearance if `showDot = 1` |

## Dot Space Calculation

When `showDot = 1`, extra left clearance increases to accommodate the dot:

```
_extraLeft = 8 (base pad) + dotSpace
dotSpace  = (dotR × 2) + gapAfterDot
dotR      = fontSize × 0.55 / 2  = 3.025
gapAfterDot = 6
dotSpace  ≈ 12.05
_extraLeft (with dot) ≈ 20.05
```

## Vertical Centering

```
_rectY = (canvasHeight - pillH) / 2
_textY = canvasHeight / 2
_dotOffsetY = canvasHeight / 2
```

All three elements are vertically centred on the same axis, so they track together regardless of canvas height.

## Rectangle Dimensions

```
pillH = 24  (fixed)
corner = 12 = pillH / 2  → fully rounded ends
rect width = pillW - 1    (minus 1px to avoid pixel boundary clipping)
rect height = pillH - 1
```

## Key Points

- Pill width scales with `LEN(label)` — no fixed-width truncation
- The `−1` on width/height prevents the rect from touching the pill edge (aesthetic margin)
- `rx = pillH / 2` is the standard formula for a fully rounded pill (equal to half the height)
- `dominant-baseline="middle"` on the text element handles vertical centering natively in SVG

## Related

- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — full UDF that implements this geometry
- [[svg-pill-pattern-udf-based]] — `pattern` — the pill pattern
