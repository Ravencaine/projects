---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [custom-vision, evaluation-metrics, precision, recall, ap, average-precision]
---

# Custom Vision Evaluation Metrics — Precision, Recall, AP

Three metrics for evaluating a Custom Vision model's accuracy: Precision, Recall, and Average Precision (AP).

## Quick Reference

| Metric | Definition | Formula | Interpretation |
|--------|-----------|---------|---------------|
| **Precision** | Of images predicted as X, how many actually are X | TP / (TP + FP) | Low precision = many false positives |
| **Recall** | Of images that are actually X, how many did the model find | TP / (TP + FN) | Low recall = many false negatives |
| **AP** (Average Precision) | Summary of precision-recall across all confidence thresholds | Area under PR curve | Overall model quality; higher = better |

## Confusion Matrix

| | Actual Positive | Actual Negative |
|--|--|--|
| **Predicted Positive** | TP (True Positive) | FP (False Positive) |
| **Predicted Negative** | FN (False Negative) | TN (True Negative) |

## Decision Guide

| Situation | What to fix |
|---------|-----------|
| High Precision, Low Recall | Increase model sensitivity; add more training images |
| Low Precision, High Recall | Increase classification threshold or retrain with harder negatives |
| Both Low | Add more training data; improve image quality |

## Related

- [[azure-custom-vision]]
- [[automl-evaluation-metrics-cheatsheet]]
