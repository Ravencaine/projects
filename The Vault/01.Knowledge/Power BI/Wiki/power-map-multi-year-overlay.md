---


title: "Power Map Multi-Year Overlay"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, power-map, pattern]
note_type: pattern
description: "Overlaying multiple years on a single Power Map — bubble view, stacked bar, clustered column, 2D chart. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Map: Displaying Multiple Values

Power Map can show multiple values simultaneously — e.g., unemployment rates for two or more years overlaid on the same map.

## Methods

### Bubble Overlay
Place bubbles for 2011 (orange) and 2012 (blue) on the same map. Hover to see each year's value.

### Stacked Bar
Stacked bars show cumulative values across years at each location.

### Clustered Column
Side-by-side columns allow direct visual comparison between years at the same location.

### 2D Chart
Plot the time series as a line/column chart in the lower portion of the Power Map window while the map shows geographic distribution.

## Layering Rules

- Each numeric field goes into its own **Layer**
- Layers can be independently configured (aggregation, format, opacity)
- Layers can be reordered (Layer pane → drag)
- Only one geographic field per Layer

## Source Reference

Chapter 9, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
