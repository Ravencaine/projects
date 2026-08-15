---
created: 2026-08-11
source: How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals
note_type: gotcha
tags: [power-bi, error-bars, visualization]
---

# Error Bar Fill Area

In Power BI's Analytics pane, the error bar fill option must be set to **Fill** mode — not line — to act as a white fill mask.

## Expected Behaviour

Setting an error bar on a chart series creates a band between the upper and lower bounds that fills the space between them.

## Actual Behaviour

If the error band style is left as **Line** or **None**, no fill is applied. The band is invisible or renders only as a line, defeating the mask technique entirely.

## Fix

Open Analytics pane > Error Bars > select the series > set Style to **Fill** > set colour to white > Transparency 0.

## Context

This gotcha is the most commonly missed step in the [[how-i-built-a-modern-oblique-area-chart-native-visuals]] pattern. Users who skip it see no white masking and assume the technique doesn't work.
