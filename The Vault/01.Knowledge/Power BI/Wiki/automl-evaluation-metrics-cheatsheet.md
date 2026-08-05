---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [automl, evaluation-metrics, auc, ap, tn-fp-fn-tp, confusion-matrix]
---

# AutoML Evaluation Metrics — Quick Reference

All metrics used to evaluate ML model quality, organised by task type.

## Classification Metrics

| Metric | Formula | When to use |
|--------|---------|------------|
| **Accuracy** | (TP+TN) / (TP+TN+FP+FN) | Balanced classes |
| **Precision** | TP / (TP+FP) | Minimize false alarms |
| **Recall (Sensitivity)** | TP / (TP+FN) | Find all positives |
| **F1 Score** | 2 × (P×R) / (P+R) | Balance precision and recall |
| **AUC-ROC** | Area under ROC curve | Overall discrimination |
| **AUC-PR (AP)** | Area under Precision-Recall curve | Imbalanced data |

## Confusion Matrix

| | Actual Positive | Actual Negative |
|--|--|--|
| **Predicted Positive** | TP | FP |
| **Predicted Negative** | FN | TN |

## Regression Metrics

| Metric | Formula | Best for |
|--------|---------|---------|
| **MAE** | Mean | Errors in same units |
| **RMSE** | √(Mean of squared errors) | Penalise large errors |
| **R²** | Variance explained | How well model fits |

## Metric Selection Guide

| Problem | Primary metric | Secondary |
|---------|--------------|----------|
| Balanced classification | AUC-ROC | Accuracy |
| Imbalanced classification | AUC-PR (AP) | F1 |
| Fraud detection | Recall | AUC-PR |
| Spam detection | Precision | F1 |
| Regression (general) | R² | RMSE |

## Related

- [[custom-vision-evaluation-metrics]]
- [[train-evaluate-regression-model-designer]]
