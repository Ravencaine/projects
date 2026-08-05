---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [automl, automated-machine-learning, feature-engineering, model-selection, azure-ml]
---

# AutoML — Automating Feature Engineering and Model Selection

AutoML automates the most time-consuming parts of ML: trying many algorithms, feature engineering combinations, and hyperparameter settings to find the best model.

## Definition

AutoML = Automated Machine Learning. Given a dataset and a target variable, AutoML:
1. Automatically engineers features from raw data
2. Tries many candidate algorithms
3. Evaluates using cross-validation
4. Selects the best-performing model
5. Returns a deployed endpoint

## What AutoML Automates

| Task | AutoML action |
|------|-------------|
| Feature engineering | Creates interaction features, encodes categoricals, handles missing values |
| Algorithm selection | Tries logistic regression, random forest, gradient boosting, neural nets |
| Hyperparameter tuning | Runs Bayesian optimisation across parameter spaces |
| Evaluation | Cross-validation on multiple metrics (AUC, RMSE, MAE, etc.) |

## What AutoML Does NOT Automate

- Defining the business problem correctly
- Evaluating whether the model is fit for purpose
- Understanding model outputs and limitations
- Responsible AI considerations (fairness, bias, transparency)

## Power BI Integration

AutoML models trained in Azure ML are called from Power BI via Azure ML model integration — returning scored predictions in your reports.

## Related

- [[automl-tasks-regression-classification-forecasting]]
- [[automl-run-configuration]]
- [[azure-ml-model-integration-power-bi]]
