---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [azure-ml-designer, normalize-data, scaling, minmax, z-score]
---

# Normalize Data — Scaling Numeric Columns in Azure ML Designer

Scale numeric columns to a standard range so features contribute proportionally to the model.

## Purpose

Features with large numeric ranges (e.g., income in dollars vs age in years) can dominate ML models. Normalisation brings all features to a comparable scale.

## Normalisation Methods

| Method | Formula | Best for |
|--------|---------|---------|
| **MinMax** | (x − min) / (max − min) | Bounded data, unknown distribution |
| **ZScore** | (x − μ) / σ | Normal distribution, outliers present |
| **Log** | log(x) | Right-skewed data (log transform) |

## Component

Azure ML Designer → Feature Engineering → Normalize Data

## Parameters

| Parameter | Value |
|-----------|-------|
| Columns to transform | Select numeric columns |
| Transformation method | MinMax or ZScore |
| Use 0 for constant columns | Yes (avoids division by zero) |

## When to Use

- Use **MinMax** for bounded data (percentages, ratings 0–10) or when the range is known
- Use **ZScore** when data is normally distributed and outliers are present
- **Do NOT** normalise categorical columns or binary flags
- **Do NOT** normalise the target variable unless specifically required by the algorithm

## Related

- [[azure-ml-designer-pipeline-components]]
- [[clean-missing-data-replace-median-designer]]
