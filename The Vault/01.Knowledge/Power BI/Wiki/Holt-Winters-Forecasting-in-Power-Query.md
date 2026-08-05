---
created: 2026-08-04
updated: 2026-08-05
source: "My Favorite Way to Forecast in Power BI.md"
note_type: pattern
tags: [python, power-query, statsmodels, holt-winters, exponential-smoothing, forecasting, time-series, seasonal, additive-trend, per-department-loop]
related: [ets-exponential-smoothing-model, python-script-in-power-query, python-forecasting-in-power-bi-sklearn, forecasting-visual-power-bi, forecast-actual-flag-pattern]
---

# Holt-Winters Forecasting in Power Query (Python + statsmodels)

Run a **Holt-Winters Exponential Smoothing** model inside Power Query — a per-segment loop fits one model per category (department, region, SKU, etc.), forecasts N periods ahead, tags each row as `Forecast=True/False`, and returns the combined historical + forecast table to Power BI. The result is a clean data table ready for any native visual — bypassing the built-in Power BI Forecasting visual entirely.

## Purpose

Power BI's built-in Forecasting visual is convenient but inflexible: it only works on a line chart, hides the underlying forecast values, and provides no confidence intervals for further analysis. Putting the forecasting model inside Power Query (as a Python script step) gives you:

- **Full access to forecast values** for DAX-driven actual-vs-forecast comparisons, custom KPIs, anomaly flags.
- **Any visual** — bar, area, table, matrix — not just line charts.
- **Multiple series in one script** — loop per category, one output table.
- **No Premium required** — only a Python runtime + `statsmodels` on the local machine.
- **Refreshes with the data** — re-running the script on each refresh generates fresh forecasts.

## Components

- **Data table** with at minimum: `Date`, a numeric metric to forecast (e.g. `TurnoverRate`), and a grouping column (e.g. `Department`).
- **`statsmodels.tsa.holtwinters.ExponentialSmoothing`** — the model. Add `trend='add'` and `seasonal='add'` for the typical HR/retail monthly setup.
- **Pandas loop** — one model per group, then concatenate original + forecast into a single DataFrame.
- **`Forecast` flag column** — boolean, `True` for forecast rows, `False` for historical. This is the linchpin that lets DAX differentiate actual vs predicted.
- **Power Query "Run Python script" step** — the integration glue. The table passes in as `dataset`; the script returns a single DataFrame.

## Structure

```python
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = dataset.copy()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

forecast_frames = []

for grp in df['GroupCol'].unique():
    temp = df[df['GroupCol'] == grp].sort_values('Date')

    if len(temp) >= 12:                                      # need ≥ 1 seasonal cycle
        model = ExponentialSmoothing(
            temp['Metric'],
            trend='add',
            seasonal='add',
            seasonal_periods=12
        )
        fit = model.fit()
        forecast = fit.forecast(12)
        future_dates = pd.date_range(
            temp['Date'].max() + pd.DateOffset(months=1),
            periods=12, freq='M'
        )

        forecast_df = pd.DataFrame({
            'Date':    future_dates,
            'Metric':  forecast.values,
            'GroupCol': grp,
            'Forecast': True
        })
        # Pad other columns with None where forecast rows don't have values
        forecast_df['OtherCol1'] = None
        forecast_df['OtherCol2'] = None

        original = temp[['Date', 'Metric', 'GroupCol', 'OtherCol1', 'OtherCol2']].copy()
        original['Forecast'] = False

        all_df = pd.concat([original, forecast_df])
        forecast_frames.append(all_df)

result = pd.concat(forecast_frames)
```

Then in Power Query:

1. **Expand** the Python output table → select `Date`, `Metric`, `GroupCol`, `Forecast`, `OtherCol1`, `OtherCol2`.
2. **Set data types** (DateType, DecimalType, etc.).
3. **Remove** the helper `"Name"` column Power Query sometimes auto-injects.
4. **Close & Apply** → the table loads into the Power BI model.

## Example

Bittar's HR example:

- Dataset: monthly `Headcount` and `Terminations` per department, with a computed `TurnoverRate = Terminations / Headcount`.
- Per-department Holt-Winters model with `seasonal_periods=12` (monthly data, yearly seasonality).
- 12-month forecast horizon.
- Output table with `Date`, `TurnoverRate`, `Department`, `Forecast`, `Headcount`, `Terminations`.

Three report views built on top of the loaded table:

1. **Last 3 months + next 12 months** — focused turn-around chart with recent history + forecast.
2. **All historical values** — long-window trend analysis.
3. **Year-end summary** — per-department anticipated turnover + expected headcount.

## Variations

### Multiplicative trend/seasonality

For data with accelerating growth or multiplicative seasonality (e.g., e-commerce revenue):

```python
model = ExponentialSmoothing(
    temp['Metric'],
    trend='mul',                  # multiplicative trend
    seasonal='mul',               # multiplicative seasonality
    seasonal_periods=12
)
```

### Non-12 seasonality

Weekly data → `seasonal_periods=52`; quarterly data → `seasonal_periods=4`. Always set this to the number of observations per cycle.

### Confidence intervals

`statsmodels` can return confidence intervals alongside point forecasts:

```python
forecast = fit.forecast(12)
forecast_ci = fit.get_forecast(12).conf_int(alpha=0.05)   # 95% CI

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Metric': forecast.values,
    'Metric_Lower': forecast_ci.iloc[:, 0].values,
    'Metric_Upper': forecast_ci.iloc[:, 1].values,
    'GroupCol': grp,
    'Forecast': True
})
```

The resulting `Metric_Lower` / `Metric_Upper` columns enable shaded ribbon visuals (see [[Error-Band-as-White-Out-Mask]] for the white-out version, or use a real area chart with lower/upper as a stacked band).

### ARIMA / Prophet / XGBoost

Same shape, swap the model:

```python
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(temp['Metric'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
fit = model.fit()
forecast = fit.forecast(12)
```

```python
from prophet import Prophet
df_prophet = temp.rename(columns={'Date': 'ds', 'Metric': 'y'})
m = Prophet(yearly_seasonality=True).fit(df_prophet)
future = m.make_future_dataframe(periods=12, freq='M')
forecast = m.predict(future)
```

Each returns a different output schema — adapt the column names downstream.

### Hold-out validation

Before shipping, hide the last N periods from training, fit, compare forecast to actuals:

```python
train = temp.iloc[:-3]          # hide last 3 months
test  = temp.iloc[-3:]
fit = ExponentialSmoothing(train['Metric'], trend='add', seasonal='add', seasonal_periods=12).fit()
forecast = fit.forecast(3)
mae = (forecast.values - test['Metric'].values).mean()
```

Use the MAE / MAPE as a quality report shared with stakeholders.

## Notes

- **`Forecast` flag is the linchpin.** Without it, downstream DAX can't distinguish actuals from forecasts. Keep it as a boolean column, not a string.
- **Sort dates chronologically** before fitting (`sort_values('Date')`) — `statsmodels` assumes ordered time series.
- **`dropna(subset=['Date'])`** strips rows where Power Query's date parser failed. Without this, exceptions can occur downstream.
- **Padding null columns** (`'OtherCol': None`) preserves schema alignment across historical and forecast rows — DAX measures that aggregate across columns (e.g., `SUM(Turnover[Headcount])`) won't break where forecast rows have no headcount.
- **`pd.DateOffset(months=1)`** is the safest way to step forward — `timedelta` only works in days. For quarterly steps, use `months=3`.
- **Refresh cadence matters.** Holt-Winters refits on every refresh. If the data refreshes daily but has monthly seasonality, the model is refit every day — wasted compute and unstable forecasts. Cache the result or refresh at the forecast cadence.
- **Different from the [[python-forecasting-in-power-bi-sklearn]] technique.** That note uses Python **Visuals** in Power BI (sklearn inside a chart visual). This note uses Python **inside Power Query** (pre-compute the table before visualisation). The two are complementary; you would use one **or** the other, not both.
- **Different from the built-in Forecasting visual.** The built-in visual (Analytics pane → Forecast) uses a simpler ETS internally and binds tightly to the line chart. The Python-in-Power-Query path gives you all the underlying values and the freedom to use any visual.

## Related

- [[ets-exponential-smoothing-model]] — the algorithm itself; conceptual reference
- [[python-script-in-power-query]] — the broader Python-in-Power-Query workflow this pattern wraps
- [[python-forecasting-in-power-bi-sklearn]] — alternative approach (Python Visual + sklearn)
- [[forecasting-visual-power-bi]] — the built-in Power BI Forecasting visual (simple cases)
- [[forecast-actual-flag-pattern]] — the DAX-side pattern that consumes the `Forecast` boolean column
- [[trend-versus-seasonality]] — when to pick additive vs multiplicative
- [[time-series-data-requirements]] — data shape requirements for forecasting
