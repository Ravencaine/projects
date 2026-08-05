---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [forecasting, validation, ignore-last, holdout, accuracy]
---

# Validate Forecast with Ignore Last

Always withhold the last N known data points before forecasting, then compare the forecast against the held-out data to assess accuracy.

## Purpose

A forecast that looks good on paper may be completely wrong. Validating against known-but-withheld data is the only way to assess real accuracy before committing to the forecast.

## How It Works

1. Set **Ignore Last = N** in the Analytics pane (e.g., 6 for 6 months)
2. Power BI produces a forecast that stops before the withheld period
3. The **withheld section is shown as a dotted line** (actual known data)
4. Compare the forecast line to the dotted line visually
5. If they are close → model is reliable. If they diverge significantly → model needs adjustment.

## Example

Netherlands monthly tourism forecast:

1. Monthly data from Jan 2018 to Dec 2019
2. Set Ignore Last = 6
3. Forecast from Jul 2019 (withholding Jul–Dec 2019)
4. Compare Jul–Dec 2019 forecast against actual Jul–Dec 2019 data
5. If forecast and actual diverge significantly, the ETS model may not be appropriate

## Key Points

- Always validate before trusting a forecast
- Ignore Last is not just for validation — it also improves the model by withholding noisy recent data
- The withheld period should match your business cycle (e.g., 12 months for yearly seasonality)

## Related

- [[forecasting-visual-power-bi]]
- [[forecasting-configuration-cheatsheet]]
