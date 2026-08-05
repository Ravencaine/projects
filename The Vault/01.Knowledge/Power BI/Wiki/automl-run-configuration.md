---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [automl, configuration, target-column, forecast-horizon, frequency, cross-validation]
---

# AutoML Run Configuration — Key Settings

Five critical settings when configuring an AutoML experiment in Azure ML Studio.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| **Select task type** | dropdown | Regression / Classification / Time-Series Forecasting |
| **Select dataset** | dataset | The registered dataset to use |
| **Target column** | column selector | The column to predict (y variable) |
| **Primary metric** | dropdown | Optimisation target (AUC, RMSE, accuracy, etc.) |
| **Training compute** | compute cluster | The compute cluster to run on |

### Time-Series Forecasting (additional)

| Parameter | Type | Description |
|-----------|------|-------------|
| **Time column** | column selector | The date/time column |
| **Forecast horizon** | integer | How many periods ahead to predict |
| **Frequency** | dropdown | Dataset time grain (Daily, Weekly, Monthly, etc.) |
| **Group by** | column selector | (Optional) Forecast independently for each group |
| **Cross-validation** | integer or None | Number of CV folds for validation |

## Primary Metrics by Task

| Task | Recommended primary metric |
|------|--------------------------|
| Regression | RMSE (Root Mean Squared Error) |
| Classification | AUC_weighted or Accuracy |
| Time-Series Forecasting | SMAPE (Symmetric Mean Absolute Percentage Error) |

## Cross-Validation

- Default: 5-fold cross-validation (data split into 5 parts; model trained 5 times)
- More folds = more accurate evaluation but longer training time
- Required for time-series: use **Time Series Cross-Validation** (respects temporal order)

## Related

- [[automl-overview]]
- [[automl-tasks-regression-classification-forecasting]]
