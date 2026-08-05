---
created: 2026-07-28
updated: 2026-08-04
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [ets, exponential-smoothing, forecasting, algorithm, time-series, holt-winters, statsmodels, python-power-query]
---

# ETS — Exponential Smoothing Model

ETS (Error, Trend, Seasonality) is Power BI's built-in forecasting algorithm — it weights recent observations more heavily than distant ones.

## Definition

ETS is a family of time-series forecasting models that produce forecasts by computing a weighted average of past observations, where the weights decay exponentially for older observations. The model has three configurable components:

| Component | Options | What it controls |
|-----------|---------|-----------------|
| **E**rror | A (additive), M (multiplicative) | How variance scales with the series |
| **T**rend | N (none), A (additive), Ad (additive damped) | Long-term direction |
| **S**easonality | N (none), A (additive), M (multiplicative) | Repeating patterns |

## Key Points

- Power BI's Forecasting visual uses ETS internally — no configuration required, options in the Analytics pane control behaviour
- **Damped trend** (Ad) prevents unrealistic long-term extrapolations by gradually flattening the trend
- ETS is appropriate when the series has a clear trend and/or seasonality
- For data with no trend or seasonality, simpler models may perform equally well

## Implementation via Python in Power Query (Holt-Winters)

When the built-in Forecasting visual is too restrictive (no underlying values, no confidence intervals, visual-locked to a line chart), the same algorithm family can be invoked from Power Query via `statsmodels.tsa.holtwinters.ExponentialSmoothing`. This is the **Holt-Winters** family — a subset of ETS that includes trend + additive seasonality.

```python
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

for grp in df['GroupCol'].unique():
    temp = df[df['GroupCol'] == grp].sort_values('Date')
    if len(temp) >= 12:                                       # ≥ 1 seasonal cycle
        model = ExponentialSmoothing(
            temp['Metric'],
            trend='add',
            seasonal='add',
            seasonal_periods=12
        )
        fit = model.fit()
        forecast = fit.forecast(12)
        # ... merge forecast rows with original, tag Forecast=True/False
```

**Why use Python-in-Power-Query instead of the built-in visual:**

| Need | Built-in Forecasting visual | Python in Power Query |
| ---- | ---------------------------- | --------------------- |
| Underlying forecast values | Only as a visual | Full data table |
| Confidence intervals | Hidden | Available via `get_forecast().conf_int()` |
| Use any visual (bar, table, matrix) | No — line chart only | Yes |
| Multiple series (per category) | One model per visual | One loop, one script |
| Hold-out / validation | No | Easy with `iloc[:-N]` |
| Refresh behaviour | Refits on every interaction | Refits only on model refresh |

See [[Holt-Winters-Forecasting-in-Power-Query]] for the complete pattern.

## Related

- [[forecasting-visual-power-bi]]
- [[Holt-Winters-Forecasting-in-Power-Query]]
- [[python-script-in-power-query]]
- [[trend-versus-seasonality]]
- [[time-series-data-requirements]]
