---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [eda, exploratory-data-analysis, power-bi, data-exploration]
---

# Exploratory Data Analysis (EDA) Workflow

A structured process for understanding your dataset before applying any AI feature.

## Prerequisites

- Power BI Desktop installed
- Dataset imported into Power BI (CSV, Excel, database, web)
- Optional: Python runtime installed for Python visuals

## Steps

1. **Import the dataset** into Power BI via Get Data
2. **Open Power Query Editor** (Transform Data)
3. **Enable data profiling tools** in the View tab:
   - Column Quality (validity)
   - Column Distribution (histogram + distinct/unique counts)
   - Column Profile (detailed statistics per column)
4. **Review Column Quality**: check for empty rows and errors
5. **Review Column Distribution**: look for skewed data, unexpected values
6. **Inspect Column Profile** on selected columns — min, max, mean, median, nulls
7. **Identify missing data** and decide on a handling strategy (mean imputation, deletion, etc.)
8. **Identify high-cardinality columns**: customer IDs, email addresses — these don't add predictive value
9. **Return to the canvas** and create visualisations to explore relationships:
   - Line charts for time-series
   - Histograms for distribution
   - Scatter plots for correlations
10. **Add a trend line** to scatter plots to assess correlation direction
11. **Create a box plot** to visualise the six summary statistics and identify outliers
12. **Document findings**: known data quality issues, columns to exclude, distributions observed

## Variations

- **Large datasets**: profile on full dataset only if compute allows; use the 1000-row preview for speed
- **Python-assisted EDA**: use the Python visual with pandas/matplotlib for custom histograms and box plots beyond Power BI's built-in visuals

## Related

- [[data-profiling-column-quality-distribution-profile]]
- [[summary-statistics-power-bi]]
- [[outlier-detection-box-plot]]
- [[scatter-plot-trend-line-correlation]]
