---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: atomic
tags: [error-bars, power-bi, pattern]
---

# Error Bars as Invisible Anchors

Error bars in Power BI do not need to display uncertainty ranges. By attaching to invisible (zero or constant) series, they become drawing primitives that can place lines, circles, and connectors anywhere on a chart canvas.

## Definition

An invisible anchor is a measure returning a constant value (0, 1, or the max of another series) assigned to a chart series and hidden via 100% transparency. The error bar attached to it then draws at that position using configured upper/lower bounds, colors, widths, and markers — entirely independent of the data values.

## Key Points

- **Transparency hides the series** — set series transparency to 100% so the anchor line/column is invisible but the error bar attached to it remains visible
- **Error bar draws at the anchor position** — the error bar is anchored to the series value, so upper/lower bounds are relative to that anchor point
- **Conditional display via BLANK()** — returning BLANK() from the anchor measure causes the error bar to draw nothing for that category; no IF() inside the error bar config needed
- **Marker shapes create new visual elements** — filled circles, dashes, and other marker shapes on error bars can add decorative or functional elements (rounded caps, whiskers, rings)
- **Series order controls layering** — add the anchor series to the chart alongside the data series; reduce series spacing and use Overlap to align anchor with data columns

## Related

- [[Dummy0-Lower-Bound-Anchor]]
- [[Error-Bar-Data-Flags]]
- [[Error-Bar-Rounded-Bars]]
- [[Error-Bar-Dumbbell-Chart]]
- [[Error-Bar-Boxplot]]
