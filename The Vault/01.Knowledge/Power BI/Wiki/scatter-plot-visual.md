---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [power-bi, visual, scatter-plot, correlation, relationship]
---

# Scatter Plot Visual

Plots two numerical fields against each other to reveal relationships, clusters, and outliers.

## Signature

Power BI visual: Scatter Chart

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| X-axis | Numeric field | Independent variable |
| Y-axis | Numeric field | Dependent variable |
| Legend | Categorical field | Colour dots by group |
| Size | Numeric field | Bubble size (optional) |
| Details | Field(s) | Tooltip additional context |

## Returns

A cloud of dots. The pattern of dots reveals the relationship between the two variables.

## Examples

Plot Life Ladder vs Healthy Life Expectancy:

1. Insert → Scatter Chart
2. X-axis: Healthy life expectancy at birth
3. Y-axis: Life Ladder
4. Legend: Year (colour by year)
5. Enable Trend Line from Analytics pane

## Notes

- Each dot = one observation (or aggregated group)
- Upward-sloping cloud → positive correlation
- Downward-sloping cloud → negative correlation
- Random scatter → no clear relationship
- Always pair with a **trend line** to assess direction

## Related

- [[scatter-plot-trend-line-correlation]]
- [[correlation-does-not-imply-causation]]
