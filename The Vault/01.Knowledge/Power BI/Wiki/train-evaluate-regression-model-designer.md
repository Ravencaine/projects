---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [azure-ml-designer, train-model, evaluate-model, regression, pipeline]
---

# Train and Evaluate Regression Model in Azure ML Designer

The complete training pipeline: split → clean → normalise → train → score → evaluate.

## Pipeline Components

```
Dataset → Clean Missing Data → Normalize Data → Split Data
                                            ├── Train Model → Score Model → Evaluate Model
                                            └── (test output)
```

## Steps

1. **Load dataset** → drag from Datasets or Data Input category
2. **Clean Missing Data** → connect → configure Replace with Median for numeric columns
3. **Normalize Data** → connect → configure MinMax scaling
4. **Split Data** → connect → set Fraction = 0.75 (75% train, 25% test), set random seed
5. **Train Model** → connect clean output + Split Data training output:
   - Click Train Model → Launch column selector → select the target (y) column
   - Select an algorithm (e.g., **Linear Regression**, **Decision Forest Regression**)
6. **Score Model** → connect trained model + test output from Split Data
7. **Evaluate Model** → connect scored output

## Evaluating Regression Output

The Evaluate Model component returns:

| Metric | What it measures |
|--------|-----------------|
| **Mean Absolute Error (MAE)** | Average absolute prediction error |
| **Root Mean Squared Error (RMSE)** | Penalises large errors more than MAE |
| **Relative Absolute Error (RAE)** | MAE relative to baseline prediction |
| **Relative Squared Error (RSE)** | RMSE relative to baseline |
| **Coefficient of Determination (R²)** | % of variance explained (0–1, higher = better) |

## Decision Thresholds

| R² | Interpretation |
|----|--------------|
| > 0.7 | Good model |
| 0.5–0.7 | Moderate — may need feature engineering |
| < 0.5 | Poor model — review features and data quality |

## Related

- [[split-data-train-test-designer]]
- [[clean-missing-data-replace-median-designer]]
- [[normalise-data-designer]]
