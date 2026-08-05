---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: pattern
tags: [power-bi, pattern, color, formatting, 100-stacked-chart, position, visual-formatting]
---

# Color by Position — Visual Formatting

Since each stacking slot is now its own measure (Position 1, Position 2, …), colors are set per measure in the visual formatting pane — not per category. The position-based series cannot be colored by category.

## Setup

1. Select the 100% Stacked Bar/Column chart
2. Open the **Format** pane
3. Expand **Data colors**

### Color Assignments

| Measure | Color | Notes |
|---|---|---|
| `Position 1` | Highlight color (e.g., brand color) | The selected category |
| `Position 2` | Light grey — `#CED4DA` | Closest to baseline |
| `Position 3` | Medium grey — `#ADB5BD` | |
| `Position 4` | Dark grey — `#6C757D` | |
| `Position 5` | Darkest grey — `#495057` | Farthest from baseline |

A light-to-dark grey gradient reinforces the visual hierarchy: the closer a segment is to the baseline, the more legible it is, so it gets the most contrast.

## Legend: Turn Off

The legend shows "Position 1 / 2 / 3…" — not real category names. Since the series are position-based rather than category-based, the legend cannot label them meaningfully.

**Format visual → Legend → Show = Off**

## Why Colors Cannot Be Set by Category

From the chart's perspective, the categories *are* the measures. There is no category field in the Series well — it was replaced by the N position measures. The visual formatting pane offers only per-measure color control.

## Related

- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
- [[stacked-chart-custom-tooltip]] — `pattern`
- [[stacked-highlight-test-checklist]] — `reference`
