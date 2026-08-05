---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [regression, classification, clustering, machine-learning-task-types]
---

# Regression, Classification, and Clustering

Three fundamental ML task types: predicting a number, predicting a category, and grouping data.

## Definition

| Task | Type | Output | Example |
|------|------|--------|---------|
| **Regression** | Supervised | Continuous numerical value | Predicting energy consumption, house prices |
| **Classification** | Supervised | Discrete category label | Churn/no-churn, fraud/legitimate |
| **Clustering** | Unsupervised | Group membership | Customer segmentation |

## Key Points

- **Regression**: output is a number. Evaluation metrics: RMSE, MAE, R². Used in Azure ML Designer and AutoML.
- **Classification**: output is a class label. Binary (two classes) or multi-class. Metrics: accuracy, precision, recall, AUC.
- **Clustering**: output is a cluster ID. No ground truth — evaluated by domain relevance, not accuracy.
- All three are supported in Azure ML: AutoML can auto-select the best algorithm for each task type.

## Examples

- Regression: predicting total monthly tourists in the Netherlands based on historical data (AutoML forecasting)
- Classification: predicting whether a customer will leave a telecom provider
- Clustering: grouping World Happiness Report countries by life expectancy and GDP to discover well-being clusters

## Related

- [[supervised-versus-unsupervised-learning]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[automl-tasks-regression-classification-forecasting]]
- [[train-evaluate-regression-model-designer]]
