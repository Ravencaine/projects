---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [forecasting, reference, cheatsheet, parameters, power-bi]
---

# Forecasting Configuration — Quick Reference

All four configuration options for the Power BI Forecasting visual at a glance.

## Quick Reference Table

| Option | Values | When to change |
|--------|--------|---------------|
| **Forecast periods** | Integer (e.g., 12) | Increase for longer horizon; decrease if uncertainty grows |
| **Ignore Last** | Integer (e.g., 6) | Always enable for validation — withhold known data |
| **Confidence Level** | 90%, 95%, 99% | 95% is standard; wider for high-stakes decisions |
| **Seasonality** | Auto or integer | Auto for unknown patterns; explicit integer when period is known |
| **Confidence interval** | On/Off | Always show for transparency |

## Decision Guide

| Question | Answer | Setting |
|---------|--------|---------|
| How far ahead do I need to forecast? | 3 months | Forecast periods = 3 |
| Is my forecast accurate? | — | Enable Ignore Last; compare dotted line to actual data |
| How uncertain is my forecast? | — | Check confidence interval width |
| Does my data have a seasonal pattern? | Yes, yearly | Seasonality = 12 (for monthly data) |
| Do I want to be conservative? | Yes | Use 99% confidence level |

## Common Pitfalls

- Forecasting too far beyond the data horizon — confidence intervals explode
- Ignoring the Ignore Last validation — never trust a forecast you haven't validated
- Using monthly data with Seasonality = 12 — yearly seasonality requires at least 2 years of data to detect

## Related

- [[forecasting-visual-power-bi]]
- [[validate-forecast-with-ignore-last]]
- [[ets-exponential-smoothing-model]]
