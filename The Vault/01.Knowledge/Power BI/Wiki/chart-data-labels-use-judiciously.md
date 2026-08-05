---
created: 2026-08-02
updated: 2026-08-05
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: pattern
tags: [powerbi, pattern, chart, data-label, design]
---

# Chart Data Labels: Use Detail Sub-Values Judiciously

The new Power BI chart data labels support rich detail sub-values — but adding too much information per label creates cluttered, overlapping charts.

## Principle

"Just because we can, doesn't mean we should." — The danger is going overboard with label options.

## Guidelines

- Add 1–2 detail sub-values maximum per label
- Prioritize: current value + directional change (↑/↓ or +/- variance)
- Avoid: raw secondary metrics, counts, or any value the chart axis already conveys
- Reserve rich labels for key callout charts; use standard labels for dense chart grids

## Trade-off

Detail sub-values increase label height → higher overlap risk → may require Y-axis headroom adjustment.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
