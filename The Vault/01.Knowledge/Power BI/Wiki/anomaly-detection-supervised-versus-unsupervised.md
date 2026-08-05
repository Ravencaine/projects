---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [anomaly-detection, supervised, unsupervised, supervised-versus-unsupervised]
---

# Anomaly Detection — Supervised vs Unsupervised

Supervised anomaly detection uses labeled examples of normal vs anomalous data. Unsupervised anomaly detection finds outliers without any labels.

## Definition

| Approach | Definition | Requires | Power BI approach |
|---------|-----------|---------|------------------|
| **Supervised** | Classifier trained on labeled normal + anomalous examples | Labeled dataset | Azure ML / Custom model |
| **Unsupervised** | Model learns what "normal" looks like; flags deviations | No labels | Power BI Anomaly Detection visual (SR-CNN) |
| **Semi-supervised** | Model trained only on normal data; flags deviations from normal | Only normal examples | One-class SVM |

## Key Points

- Power BI's Anomaly Detection is **unsupervised**: no need to label anomalies in advance
- SR-CNN (Spectral Residual-Convolutional Neural Network) learns the "normal" pattern from your time series and flags deviations
- Works on time-series data with a date field and a numeric measure
- Best for detecting unexpected spikes, drops, and pattern breaks

## Related

- [[sr-cnn-spectral-residual-convolutional-neural-network]]
- [[anomaly-detection-visual]]
- [[supervised-versus-unsupervised-learning]]
