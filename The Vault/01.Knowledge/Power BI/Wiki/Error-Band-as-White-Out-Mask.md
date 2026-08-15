---
created: 2026-08-04
updated: 2026-08-05
source: "How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals.md"
note_type: atomic
tags: [error-bands, error-band, white-out-mask, analytics-pane, area-chart, line-chart, decorative, oblique]
related: [Oblique-Area-Chart, Time-Period-Slicers, figma-to-power-bi-canvas-background, Source-Oblique-Area-Chart]
---

# Error Band as White-Out Mask

A **decorative repurpose** of the Analytics-pane error bands feature: instead of communicating statistical uncertainty, the error band is filled solid white to "paint over" parts of the chart — letting a decorative background PNG show through and creating oblique / shaped / letterboxed chart looks that Power BI does not natively support.

## Definition

The **Error Band** control (Analytics pane → Error bars → enable only "Error Band", not "Bar" or "Line") creates a filled region between two bound values on a series. Normally you would set upper bound = `Metric + SD` and lower bound = `Metric - SD`. The white-out mask flips that:

1. Set fill style to **Fill**.
2. Set the fill color to **white** (or whatever colour matches the *background outside the plot area*).
3. Set **Transparency = 0%:** fully opaque.
4. Bind the upper/lower bounds to deliberately inflated values that extend beyond the natural data range.

The painted region looks like a solid blank rectangle, but it only covers the parts of the chart between the bounds — so it can be used to mask specific edges, corners, or ranges while leaving the rest of the chart intact.

## Key Points

- **Not statistical.** There is no uncertainty being communicated. The error band is a graphics primitive, not a statistical indicator. Document and label so reviewers don't read statistical intent.
- **Use the chart's Y-axis to set the bounds deliberately.** The upper/lower bound measures are usually arithmetic extras (e.g., `Max Vital + 5%`) that define a region *outside* the interesting data — that region is what gets painted white.
- **Combine with a background image.** The whole point is to let *something else show through*. Pair the white-out with a transparent PNG/SVG placed behind the chart and you've got a graphics layer composition.
- **Hide helper lines.** If you wire the bounds to helper measures, set those helper series' line colours to white so they don't appear in the tooltip or in the legend.
- **Line charts > area charts for this.** A line chart's translucent strokes leave the background visible; an area chart's solid fill fights the background image.

## Examples

### Example 1 — Oblique area chart illusion

The original Bittar use case ([[Oblique-Area-Chart]]):

- Chart: line chart of `Average Vital`, `Max Vital`, `Min Vital` over `Date`.
- Background: Figma PNG with a diagonal cut on the bottom edge, sized to the plot area.
- `Max Vital` series gets an error band: upper bound = `Max Graph Area` (= MaxVital + 5%), lower bound = `Max Vital`. Fill = white, opacity 100%.
- `Min Vital` series gets an error band: upper bound = `Min Vital`, lower bound = `Min Graph Area` (= MinVital − 5%). Fill = white, opacity 100%.

Anything above `Max Vital` and anything below `Min Vital` becomes solid white. The diagonal cut in the background PNG "shows through" the white, producing the oblique-area illusion with no custom visual and no shape objects in Power BI.

### Example 2 — Sketch ideas

- **Letterboxed chart:** fill the top and bottom 10% of a tall chart white to leave only the middle band visible, mimicking a 16:9 cinematic crop on a chart meant to be embedded in a wider page.
- **Notched sparkline:** fill the extreme left and right tails of a sparkline white to leave only the active data window.
- **Rounded-corner card chart:** fill the four corners with white after overlaying a card-shaped background PNG to fake `border-radius` on a chart (Power BI does not support rounded plot areas natively).

## When to Use

Use when:

- You need a chart shape (oblique, notched, letterboxed, rounded-corner) that Power BI doesn't render natively.
- You are already loading a decorative background PNG/SVG behind the chart.
- The alternative (custom visual) is undesirable for performance, certification, or maintenance reasons.

Do not use when:

- You actually want statistical uncertainty bands. Use real error bars instead.
- The chart is dense data (high point count, narrow band) and the mask would obscure useful data points.
- The audience would read statistical intent into the white region.

## Related

- [[Oblique-Area-Chart]] — the canonical workflow that uses this technique
- [[Time-Period-Slicers]] — pairs well: dynamic X-axis for the same chart
- [[figma-to-power-bi-canvas-background]] — the broader Figma → Power BI background workflow
