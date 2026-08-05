---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [sr-cnn, spectral-residual, convolutional-neural-network, anomaly-detection, deep-learning]
---

# SR-CNN — Spectral Residual-Convolutional Neural Network

Power BI's Anomaly Detection algorithm: a deep learning model that learns the "normal" pattern of a time series and flags deviations.

## Definition

SR-CNN = **Spectral Residual** + **Convolutional Neural Network**

The algorithm has two stages:
1. **Spectral Residual (SR)**: Decomposes the time series into spectral (frequency) components. Removes predictable components (trend, seasonality). Keeps the residual — the unpredictable part.
2. **Convolutional Neural Network (CNN)**: Learns what the residual looks like when the series is "normal." Flags observations where the residual is unexpectedly large.

## Key Points

- **No labeled anomalies needed**: it learns what "normal" looks like from the data itself
- Works on **time-series data** with a sufficient number of data points
- Suitable for detecting **contextual anomalies** (spikes or drops relative to the local pattern)
- The CNN is pretrained on the specific time series in your report — no external model required

## What It Detects

- Unexpected spikes (e.g., viral social media post driving 10× normal traffic)
- Unexpected drops (e.g., payment processor outage causing 0 transactions)
- Pattern breaks (e.g., seasonal pattern shifting unexpectedly)

## Related

- [[anomaly-detection-supervised-versus-unsupervised]]
- [[anomaly-detection-visual]]
- [[anomaly-correlations-require-domain-expertise]]
