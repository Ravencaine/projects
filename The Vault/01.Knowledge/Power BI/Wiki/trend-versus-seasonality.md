---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [trend, seasonality, time-series, components]
---

# Trend vs Seasonality — Two Time-Series Components

Trend = long-term direction. Seasonality = repeating pattern at a fixed period.

## Definition

| Component | Definition | Example |
|-----------|-----------|---------|
| **Trend** | Long-term increase or decrease in the series | Hotel bookings rising 3% per year |
| **Seasonality** | Repeating pattern at a fixed period | Summer peaks, winter troughs in tourism |
| **Residual/Noise** | Random, unpredictable variation | Daily fluctuation not explained by trend or season |

## Why Both Matter

- A model that captures only trend will miss seasonal peaks and troughs
- A model that captures only seasonality will miss the long-term direction
- Most real-world time series contain both

## Power BI Implications

- The **Forecasting visual** detects trend automatically
- For seasonality, ensure the date granularity matches the seasonal period (monthly data captures yearly seasonality; weekly data captures weekly patterns)
- The **ETS model** in Power BI uses exponential smoothing that weights recent observations more heavily

## Related

- [[time-series-data-requirements]]
- [[ets-exponential-smoothing-model]]
- [[forecasting-visual-power-bi]]
