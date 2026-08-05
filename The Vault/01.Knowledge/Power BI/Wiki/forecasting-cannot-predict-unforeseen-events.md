---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [forecasting, limitations, unforeseen-events, black-swan]
---

# Power BI Forecasting Cannot Predict Unforeseen Events

Forecasting models extrapolate from historical patterns. Any event outside those patterns — a pandemic, a policy change, a viral moment — is invisible to the model.

## Expected Behaviour

Power BI's forecasting visual produces a confidence interval that captures the expected range based on historical trend and seasonality.

## Actual Behaviour

The confidence interval only accounts for predictable variability. A genuine disruption — COVID-19, a new competitor, a regulatory change — lies completely outside the historical data and cannot be forecast from it.

## Why It Happens

Forecasting models assume the future resembles the past in structure (trend, seasonality). When the underlying system changes fundamentally, historical patterns are no longer a valid basis for prediction.

## How to Handle It

- Use **domain knowledge** alongside the forecast — the analyst's role
- Add **known future events** manually (e.g., flag "COVID lockdown" periods)
- **Validate the forecast** using Ignore Last before trusting it
- **Communicate limitations**: always note that the forecast assumes no major disruptions
- Consider **scenario analysis** (best case / worst case / base case) rather than a single forecast line

## Related

- [[forecasting-visual-power-bi]]
- [[validate-forecast-with-ignore-last]]
- [[garbage-in-garbage-out]]
