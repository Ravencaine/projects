---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [anomaly-detection, requirements, time-series, minimum-data-points]
---

# Anomaly Detection — Data Requirements

Power BI's Anomaly Detection requires time-series data with enough data points for the model to learn the normal pattern.

## Definition

| Requirement | Specification |
|------------|--------------|
| **Data type** | Time-series (date column + numeric measure) |
| **Granularity** | Daily, weekly, monthly, quarterly, yearly — must be consistent |
| **Minimum data points** | Sufficient to establish a pattern — typically at least 2 seasonal cycles |
| **No missing series** | All series to analyse must have overlapping time periods |
| **Numeric values** | The measure must be numeric — anomaly detection operates on the value, not the date |

## Key Points

- **Minimum 12 data points** for monthly seasonality detection (1 year minimum)
- **60+ data points** preferred for complex seasonal patterns
- With insufficient data, the model cannot reliably establish what "normal" looks like
- Irregular intervals degrade performance — interpolate to regular intervals first
- High-cardinality dimensions (too many series at once) reduce sensitivity

## Related

- [[anomaly-detection-visual]]
- [[time-series-data-requirements]]
- [[sr-cnn-spectral-residual-convolutional-neural-network]]
