---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [forecasting, power-bi, visual, analytics-pane, line-chart]
---

# Forecasting Visual in Power BI

A line chart with the Analytics pane's Forecast option enabled — the out-of-the-box forecasting feature.

## Signature

Power BI: Line Chart visual + Analytics pane → Forecast

## Parameters (Analytics Pane)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| Forecast | toggle | Off | Enable/disable |
| Units | dropdown | Auto | Points / Days / Weeks / Months / Years |
| Forecast periods | integer | Auto | How far ahead to predict |
| Ignore Last | toggle | Off | Ignore the last N data points for validation |
| Show Confidence Intervals | toggle | On | Display upper/lower bound shading |
| Confidence Level | percentage | 95% | Width of the confidence band |
| Seasonality | integer / Auto | Auto | Detect or specify seasonal period |

## Returns

A line chart extended beyond the last data point with:
- A **forecast line** (solid)
- A **confidence interval** (shaded region)
- An **ignore last** segment (dotted — the withheld validation portion)

## Example

Monthly Netherlands tourism data:

1. Create a Line Chart (Axis: Month, Values: Tourists)
2. Analytics pane → Forecast → On
3. Forecast periods: 12
4. Ignore Last: 6 (withhold last 6 months for validation)
5. Confidence Level: 95%

## Notes

- Requires a date/time column on the Axis
- Cannot forecast across gaps in the date series
- Only for time-series data — not suitable for non-sequential data

## Related

- [[ets-exponential-smoothing-model]]
- [[forecasting-configuration-cheatsheet]]
- [[validate-forecast-with-ignore-last]]
