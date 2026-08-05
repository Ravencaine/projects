---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [azure-ml-designer, clean-missing-data, imputation, median, replace]
---

# Clean Missing Data — Replace with Median in Azure ML Designer

Replace null values in numeric columns with the median — the recommended imputation strategy for skewed distributions.

## Purpose

ML algorithms require complete data. Missing values in numeric columns are replaced before training. For skewed distributions, median is preferred over mean.

## Component

Azure ML Designer → Data Transformation → Clean Missing Data

## Parameters

| Parameter | Value |
|-----------|-------|
| Columns to clean | Select numeric columns |
| Minimum / Maximum value | (Optional) Clip outliers before cleaning |
| Cleaning mode | Replace with Median |
| Custom replacement value | (Optional) Override with fixed value |

## When to Use Median vs Mean

| Distribution | Best imputation | Reason |
|------------|---------------|--------|
| Normal / symmetrical | Mean or Median | Both work; mean is marginally better |
| Skewed (right or left) | **Median** | Mean is pulled by extreme values; median is robust |

## Steps

1. Drag **Clean Missing Data** component to canvas
2. Connect dataset to the input port
3. Select the component → right panel → Columns to clean → select columns
4. Cleaning mode → Replace with Median
5. Connect output to the next component (e.g., Train Model)

## Related

- [[handling-missing-data-strategies]]
- [[distribution-shapes-normal-right-skewed-left-skewed]]
- [[azure-ml-designer-pipeline-components]]
