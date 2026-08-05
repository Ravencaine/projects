---
created: 2026-08-02
source: The New Image Visual in Power BI Is a Quiet Game Changer
note_type: pattern
tags: [power-bi, image-visual, design-system, ux, visualization, components]
---

# Image Visual as Design System Container

The revamped Image visual in Power BI acts as a reusable, dynamic design system component — replacing buttons, shapes, and hacky bookmark toggles for micro-UX elements.

## What It Replaces

| Before (hacky) | Now (Image visual) |
|----------------|-------------------|
| Buttons for navigation | SVG icon with action bound |
| Shapes as spacers/containers | Images with precise sizing |
| Invisible overlays for tooltips | Clickable image triggers |
| Table visual as image container | Native Image visual |
| Workarounds for SVG pills | Direct SVG rendering |

## Design System Components Possible

- **Dynamic status dots** — color changes by rule (low/medium/high risk)
- **Help button with nudge animation** — discoverable onboarding UX
- **Navigation bar** — SVG icons that highlight the active page
- **Category logos** — switches automatically based on user selection
- **Dynamic rating stars** — for surveys, feedback, HR dashboards
- **KPI icons** — status-aware, filter-reactive icons

## Architecture

```
DAX measure returning image URL/SVG
        ↓
Image visual (bound to field)
        ↓
Layout: Fit / Fill / Cover / Crop
        ↓
Optional: action bound to image
```

One measure → infinite visual states. Reusable via `[[udf_encodesvg-url-encoder-for-svg]]` for SVG content.

## Related

- [[image-visual-dynamic-binding]] — binding to fields, measures, URLs, SVG
- [[image-visual-layout-modes]] — Fit, Fill, Cover, Crop, Scale
- [[image-visual-clickable-actions]]
- [[svg-visualizations-in-power-bi]] — SVG rendering in Power BI
- [[svg-pill-pattern-udf-based]] — SVG pill pattern via UDF
