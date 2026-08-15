---
created: 2026-08-11
source: How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals
note_type: pattern
tags: [power-bi, visualization, tooltip]
---

# Custom Tooltip Page

Using a separate Power BI report page as a custom tooltip to display clean, designed information while hiding helper measures and technical labels.

## Purpose

Some chart configurations require helper measures (e.g., MinGraphArea, MaxGraphArea) that should not appear in the default tooltip. A custom tooltip page lets you show only the intended values and labels.

## Technique

1. Create a new report page (typically 350 x 250 px or smaller)
2. Build the desired tooltip layout using card visuals, text boxes, or images
3. Add the measures and fields that should appear in the tooltip
4. Hide any helper measures from the field list
5. Return to the main chart > Format pane > Tooltip > Type: Tooltip > Page: select the tooltip page

## Key Points

- Page must be set to exactly the right size; standard is 350 x 250
- Only fields placed on the tooltip page will appear — use this to exclude helper measures
- Works with all standard visuals (line chart, column chart, etc.)
- The tooltip page can include branding, icons, and formatted text

## Context

Used in the [[how-i-built-a-modern-oblique-area-chart-native-visuals]] pattern to hide MinGraphArea and MaxGraphArea from the tooltip while showing clean Min/Max/Average vital readings.
