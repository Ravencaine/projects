---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [missing-data, imputation, mean, median, mode, power-query, azure-ml-designer]
---

# Handling Missing Data — Imputation Strategies

Four common approaches to filling or removing missing values before model training.

## Purpose

ML algorithms typically cannot handle null values. Missing data must be resolved before using features in models or AI Insights.

## Strategies

| Strategy | When to use | How |
|---------|-------------|-----|
| **Delete rows** | Missing data is rare (<5%) and random | Filter out nulls in Power Query |
| **Mean imputation** | Normal distribution, numeric data | Fill nulls with column mean |
| **Median imputation** | Skewed distributions, numeric data | Fill nulls with column median |
| **Mode / Most Frequent** | Categorical data | Fill nulls with most common category |
| **Predictive imputation** | Structured missingness | Train a mini-model to predict missing values |

## Key Points

- For **right-skewed** data: median is better than mean (mean is pulled by outliers)
- For **left-skewed** data: median is also preferred
- For **categorical** data: mode or "Unknown" category
- **Azure ML Designer** has a Clean Missing Data component with Replace with Median option
- In Power Query: use Fill → Down/Up or Replace Values

## Power Query Steps

1. Identify missing columns: Column Quality shows Empty %
2. For mean/median: Add Column → Custom Column with `List.Average([Column])` or `List.Median([Column])`
3. Or use Replace Values after computing the value manually

## Related

- [[clean-missing-data-replace-median-designer]]
- [[garbage-in-garbage-out]]
- [[distribution-shapes-normal-right-skewed-left-skewed]]
