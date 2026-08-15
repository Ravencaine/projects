---
created: 2026-08-06
updated: 2026-08-06
source: Conditionally Color-Coding Line Charts in Power BI 📈
note_type: atomic
tags: [line-chart, conditional-color, power-bi, visualization, dynamic-color]
---

# Conditional Color-Coding Line Charts in Power BI

Power BI line charts do not support conditional formatting via the Format pane — unlike bar/column charts, there is no fx option to set line color based on a measure. The workaround is to create two overlapping measure series, one showing data only when the condition is met and the other when it is not, then statically color each series in the Format pane.

<!-- one-line description: Overlay two measure series technique — one for positive, one for negative — to make a line chart change color dynamically based on a metric -->

## Definition

The overlay pattern creates two DAX measures derived from the same data, each returning BLANK() when its condition is not met. Both are placed on the Y-axis of a single line chart; the non-blank series displays at any given point. Each series is assigned a static color in the Format pane. The result is a line that visually changes color when the driving metric crosses a threshold.

## Key Points

- Line charts have no built-in conditional formatting — the Format pane does not expose color → fx for line series
- The workaround uses two overlapping series: one for positive values (green), one for negative (red)
- The IF() condition must return BLANK() — not 0 — when the condition is not met, otherwise the hidden series creates a flat zero line across the chart
- Critical: set the series colors **before** making the condition hide/show — if a series is hidden at color-set time, its color option is inaccessible
- The disconnected Calendar table technique: a single-column date table NOT connected to the model, used only to drive the X-axis continuity
- Price Variation = [Current Price] − [Last Price] drives the color condition — positive = green, negative = red
- Contrast with [[Color-Coding-4-Techniques]] — that note covers all four color-coding techniques; this note focuses on Technique 4 (overlay charts) for line/area visuals specifically
- Contrast with [[conditional-formatting-via-dax]] — that covers Format pane → field value conditional formatting; this covers the overlay series workaround for visuals without conditional formatting

## Why Two Measures Are Needed

A single measure cannot have two different colors in the same visual. Power BI assigns one color per measure/series. The overlay pattern works around this by having two measures that are never visible simultaneously — the hidden one returns BLANK() and does not render.

## Related

- [[Build-a-Conditionally-Color-Coded-Line-Chart]] — step-by-step workflow
- [[Line-Chart-Overlay-Pattern-for-Conditional-Color]] — pattern reference with full DAX
- [[Color-Coding-4-Techniques]] — 4-technique reference including this overlay approach (Technique 4)
- [[conditional-formatting-via-dax]] — DAX measure-driven conditional formatting for visuals that DO support it
