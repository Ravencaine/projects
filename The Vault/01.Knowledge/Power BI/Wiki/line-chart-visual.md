---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [power-bi, visual, line-chart, time-series, trend]
---

# Line Chart Visual

Plots a continuous variable over time or a sequential category, revealing trends and seasonality.

## Signature

Power BI visual: Insert → Line Chart

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Axis | Date/Category field | X-axis — typically a time field |
| Values | Numeric field | Y-axis — the measure to plot |
| Legend | Optional categorical field | Group lines by a dimension |

## Returns

A line chart showing how a numeric value changes across a sequence.

## Examples

Plot average Life Ladder score per year:

1. Create a line chart
2. Drag Year to the Axis well
3. Drag Life Ladder to the Values well
4. Change aggregation from Sum to Average (▼ → Average)
5. Set Y-axis Start = 0, End = 10 to avoid misleading scale

## Notes

- Use with a **Date hierarchy** or date column for time-series
- Enable **Auto Date/Time** in Power BI options to get automatic date tables
- Add **forecast** from the Analytics pane
- Aggregation choice matters: Sum for totals, Average for per-unit rates, Count for frequencies

## Related

- [[forecasting-visual-power-bi]]
- [[scatter-plot-visual]]
- [[time-series-data-requirements]]
