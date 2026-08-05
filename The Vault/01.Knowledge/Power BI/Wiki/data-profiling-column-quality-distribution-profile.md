---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [data-profiling, column-quality, column-distribution, column-profile, power-query]
---

# Data Profiling: Column Quality, Distribution, and Profile

Three built-in Power Query Editor tools that surface data quality issues before they reach your model.

## Prerequisites

- Power BI Desktop
- A query loaded in Power Query Editor (Transform Data)

## Steps

1. Open Power Query Editor
2. Go to the **View** tab
3. Check the boxes for the profiling tools you need:
   - ☑ Column quality
   - ☑ Column distribution
   - ☑ Column profile
4. (Optional) Change profiling base: click the status bar at the bottom → select **Column profiling based on entire dataset** instead of 1000 rows

### Column Quality

Shows three bars per column: **Valid** (%), **Error** (%), **Empty** (%).

- **Valid**: rows that loaded successfully
- **Error**: rows Power BI could not parse (wrong type, malformed value)
- **Empty**: rows with no data at all (null/blank)

Use to quickly spot columns with missing data or parse errors.

### Column Distribution

Shows a histogram per column and the distinct/unique value counts.

- **Distinct**: total number of different values
- **Unique**: values that appear only once (useful for spotting identifiers like email addresses)

Use to understand cardinality and distribution shape before choosing a visualisation.

### Column Profile

The most detailed view: shows all summary statistics for the selected column.

Includes: Type, Count, Non-Null Count, Null Count, Min, Max, Mean, Median, Standard Deviation, Variance, and the value distribution histogram.

## Common Errors

- Missing Column Profile results → column profiling set to 1000 rows only; check the status bar
- Empty rows in a numeric column → check Column Quality for high Empty %; decide whether to filter or impute

## Related

- [[exploratory-data-analysis-eda-workflow]]
- [[column-profiling-default-1000-row-cap]]
- [[summary-statistics-power-bi]]
