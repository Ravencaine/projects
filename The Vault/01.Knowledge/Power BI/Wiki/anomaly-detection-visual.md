---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [anomaly-detection, power-bi, find-anomalies, visual]
---

# Anomaly Detection Visual — Find Anomalies

Power BI's built-in visual that uses SR-CNN to detect unexpected spikes, drops, and pattern breaks in time-series data.

## Signature

Power BI: Line Chart visual + Analytics pane → Find Anomalies

## Parameters (Analytics Pane)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| Find Anomalies | toggle | Off | Enable anomaly detection |
| Sensitivity | slider 1–100 | Auto | Higher = more anomalies flagged (more false positives); lower = fewer anomalies flagged (more false negatives) |
| Anomaly range | dropdown | 95% | Confidence threshold for flagging |

## Returns

A line chart with:
- Anomaly **red dots** overlaid on points that deviate from expected values
- A **confidence band** (optional) showing the expected range
- Tooltip showing: anomaly date, actual value, expected value, deviation

## Steps

1. Create a Line Chart (Axis: Date, Values: Numeric measure)
2. Analytics pane → Find Anomalies → On
3. Adjust Sensitivity slider if needed
4. Hover over red anomaly dots to see details
5. Use the **Anomalies Pane** to investigate further

## Related

- [[sr-cnn-spectral-residual-convolutional-neural-network]]
- [[anomalies-pane-explain-with-attributes]]
- [[anomaly-detection-data-requirements]]
