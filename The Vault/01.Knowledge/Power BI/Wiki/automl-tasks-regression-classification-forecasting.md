---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [automl, tasks, regression, classification, forecasting, time-series]
---

# AutoML Tasks — Regression, Classification, and Time-Series Forecasting

Azure ML AutoML supports three primary ML task types: regression, binary/multi-class classification, and time-series forecasting.

## Definition

| Task | Output | Example |
|------|--------|---------|
| **Regression** | Continuous numerical value | Predict energy consumption, house prices, revenue |
| **Classification** | Category label (binary or multi-class) | Churn/no-churn, fraud/legitimate, product category |
| **Time-Series Forecasting** | Future values of a time series | Monthly tourists, daily sales, quarterly revenue |

## Regression

- Target: a continuous number (e.g., 45.3, 127000)
- Metrics: RMSE, MAE, R²
- Use when: predicting a quantity (how much, how many, how long)

## Classification

- Binary: one of two categories (yes/no, fraud/legitimate)
- Multi-class: one of N categories (product category, customer segment)
- Metrics: AUC, Accuracy, Precision, Recall, F1
- Use when: predicting which group an observation belongs to

## Time-Series Forecasting

- Specialised regression on temporal data
- Handles seasonality and trend automatically
- Requires: date column, numeric target, time granularity
- Metrics: SMAPE (Symmetric Mean Absolute Percentage Error)

## Key Points

- The task type determines which algorithms AutoML tries and which metrics it evaluates
- Choosing the wrong task type is a critical error — regression on a classification problem produces nonsense
- Time-Series Forecasting is configured differently from standard regression (requires horizon, grain, target column)

## Related

- [[automl-overview]]
- [[automl-run-configuration]]
- [[train-evaluate-regression-model-designer]]
