---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [azure-ml-designer, components, palette, categories]
---

# Azure ML Designer Pipeline Components

The Designer palette contains five categories of components for building ML pipelines.

## Categories

| Category | Components | Purpose |
|----------|-----------|---------|
| **Data Input & Output** | Web URL, Dataset, Datastore, Import Data | Load data from Blob Storage, DB, Web |
| **Data Transformation** | Select Columns, Clean Missing Data, Normalize, Split Data, Join Data | Prepare data for modelling |
| **Machine Learning** | Train Model, Score Model, Evaluate Model | Core ML operations |
| **Python / R** | Execute Python Script, Execute R Script | Custom transformations or visualisation |
| **Feature Engineering** | Normalize Data, Clip Values, Add Columns | Create features from raw data |

## Key Components Used in the Book

| Component | Purpose |
|----------|--------|
| **Clean Missing Data** | Replace nulls with mean, median, mode, or custom value |
| **Normalize Data** | Scale numeric columns to 0–1 or Z-score |
| **Split Data** | Random or stratified split into train/test sets |
| **Train Model** | Takes algorithm + training data; produces trained model |
| **Score Model** | Applies trained model to test data |
| **Evaluate Model** | Computes metrics (RMSE, AUC, etc.) |

## Notes

- Components have configurable parameters in the right panel when selected
- Right-click output port → Visualise to inspect intermediate results
- The pipeline must have a **Submit** button to execute

## Related

- [[azure-ml-designer]]
- [[clean-missing-data-replace-median-designer]]
- [[split-data-train-test-designer]]
