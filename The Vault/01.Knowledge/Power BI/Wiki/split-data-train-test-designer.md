---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [azure-ml-designer, split-data, train-test, stratified, random-split]
---

# Split Data — Train/Test Split in Azure ML Designer

Split a dataset into training and test subsets for model evaluation.

## Purpose

The model is trained on training data and evaluated on test data (data the model has never seen). A good train/test split is essential for honest evaluation.

## Component

Azure ML Designer → Data Transformation → Sample and Split → Split Data

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| Splitting mode | dropdown | Split rows | Random, Stratified, Recommender split |
| Fraction of rows in first output | float | 0.7 | % of data in training set |
| Stratified split | toggle | Off | Maintain class proportions |
| Random seed | integer | 0 | Reproducible split |

## Splitting Modes

| Mode | Use when |
|------|---------|
| **Split rows** (random) | Most cases; regression or balanced classification |
| **Stratified split** | Imbalanced classification — maintains class proportions in both sets |
| **Recommender split** | Collaborative filtering / recommendation systems |

## Recommended Split

| Task | Training | Test |
|------|---------|------|
| Standard ML | 75% | 25% |
| Small datasets (<10K rows) | 80% | 20% |
| Very large datasets (>1M rows) | 95% | 5% |

## Notes

- Always set a **random seed** for reproducible splits (same split on re-run)
- Use **stratified split** for binary classification with imbalanced classes (e.g., 95% normal, 5% fraud)

## Related

- [[train-evaluate-regression-model-designer]]
- [[azure-ml-designer-pipeline-components]]
