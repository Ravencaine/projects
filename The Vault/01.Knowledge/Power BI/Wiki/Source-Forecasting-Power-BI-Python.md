---
created: 2026-08-04
source: "My Favorite Way to Forecast in Power BI.md"
source_url: "https://medium.com/the-bi-corner/my-favorite-way-to-forecast-in-power-bi-634d1221df24"
note_type: source
tags: [powerbi, power-query, python, forecasting, holt-winters, exponential-smoothing, statsmodels, time-series, seasonal, ki-data-science]
---

# My Favorite Way to Forecast in Power BI

A Power Query + Python pattern that runs Holt-Winters Exponential Smoothing inside Power Query — producing a data table (historical + 12-month forecast, per department) that can be visualised with **any** Power BI native visual, not just the built-in Forecasting line chart. Uses `statsmodels.tsa.holtwinters.ExponentialSmoothing` with additive trend and seasonal components.

> **Type:** article
> **Author:** [[Author-Isabelle-Bittar|Isabelle Bittar]] (KI Data Science)
> **Published:** 2025-06-25
> **Routed to:** Power BI

## Summary

Power BI's built-in Forecasting visual is convenient but inflexible — it only works on the line chart, exposes no underlying forecast values, and provides no confidence intervals for further analysis. The author bypasses it entirely by running a Python script inside Power Query: a per-department Holt-Winters model produces 12 months of forecast values, tagged with a `Forecast` flag (`True`/`False`) so Power BI can distinguish actuals from predictions. The result is a clean table that feeds any visual, enables DAX-based actual-vs-forecast comparisons, and scales to any KPI.

## Key Claims

1. Python in Power Query can house the entire forecasting pipeline — no Premium capacity, no external scheduling, no Python visual required.
2. A `Forecast` boolean column enables visual-level toggling (show actuals only, forecast only, or both) without changing the underlying data.
3. Holt-Winters with `seasonal_periods=12` and additive trend/seasonality is well-suited to HR/headcount/turnover data (monthly, seasonal, moderate trend).
4. Grouping by a dimension column (`Department`) inside the Python loop lets one script handle multiple series at once — avoiding the need for separate models per department.
5. The `Forecast=True` flag is critical for DAX: `[Actual vs Forecast] = IF(MAX(Turnover[Forecast]), "Forecast", "Actual")` lets DAX itself colour, label, or filter by actual vs predicted.

## Notable Details

- **`seasonal_periods=12`**: monthly data with yearly seasonality — 12 data points per seasonal cycle. If the data is weekly or quarterly, adjust accordingly (52 for weekly, 4 for quarterly).
- **Minimum 12 months required** (`if len(temp) >= 12`) before fitting — Holt-Winters needs at least one full seasonal cycle.
- **`trend='add'`, `seasonal='add'`**: additive (linear) trend and additive seasonal component. For data with accelerating growth or multiplicative seasonality (e.g., e-commerce with % growth rates), use `trend='mul'` and `seasonal='mul'`.
- **Output columns**: `Date`, `TurnoverRate`, `Department`, `Forecast` (bool), `Headcount` (null for forecast rows), `Terminations` (null for forecast rows).
- **Alternative algorithms** mentioned: ARIMA, Prophet, machine-learning regressors — Bittar chose Holt-Winters for simplicity and suitability for smaller department-level datasets.
- **The Python Visual vs Python in Power Query distinction**: the existing note [[python-forecasting-in-power-bi-sklearn]] uses the Python *Visual* (sklearn LinearRegression displayed inside Power BI). This article uses Python *inside Power Query* to pre-compute the forecast table before visualisation — different layers, complementary.
- A downloadable PBIX is offered at the end of the original article (Google Drive link, not archived here).

## Extracted Notes

- [[Holt-Winters-Forecasting-in-Power-Query]] — the core pattern note
- [[ets-exponential-smoothing-model]] — extended with a "Python in Power Query implementation" section contrasting this approach with the built-in Power BI Forecasting visual
- [[python-script-in-power-query]] (Power Query KB) — extended with Holt-Winters as a notable ETL variation

## Metadata

| Field | Value |
|-------|-------|
| Source file | My Favorite Way to Forecast in Power BI.md |
| Archived at | (not yet archived — file remains in `00.Inbox/`) |
| Ingestion date | 2026-08-04 |
| Word count | ~1,350 |
