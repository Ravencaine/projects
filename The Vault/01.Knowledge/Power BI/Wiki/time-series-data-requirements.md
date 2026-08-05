---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [time-series, forecasting, requirements, date-column, numeric-value]
---

# Time-Series Data — Requirements for Forecasting

Forecasting in Power BI requires time-series data: a date column and a numeric value column, sampled at regular intervals.

## Definition

Time-series data is a sequence of observations recorded at regular time intervals (daily, monthly, quarterly, yearly). Power BI's Forecasting visual and Azure ML AutoML both require this structure.

## Requirements

| Requirement | Description |
|------------|-------------|
| **Date/Time column** | A sequential date or time field (daily, weekly, monthly, etc.) |
| **Numeric value column** | The measure to forecast (tourists, sales, revenue) |
| **Regular intervals** | Data sampled at consistent intervals — no gaps, or gaps are explicit |
| **Minimum data points** | Power BI Forecasting: sufficient history; AutoML: configurable horizon |
| **Trend and/or seasonality** | The model needs at least one of these patterns to extrapolate |

## Key Points

- Irregularly-spaced data cannot be reliably forecasted — interpolate to regular intervals first
- The date column should be at the right granularity for the business question (daily for demand, monthly for tourism)
- Enable **Auto Date/Time** in Power BI for automatic date hierarchies

## Related

- [[forecasting-visual-power-bi]]
- [[auto-date-time-power-bi]]
- [[trend-versus-seasonality]]
