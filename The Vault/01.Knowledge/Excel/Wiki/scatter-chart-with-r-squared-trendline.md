---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [excel, scatter-chart, regression, r-squared, trendline]
---

# Scatter Chart with R-Squared Trendline in Excel

A scatter chart (X/Y plot) shows the relationship between two numeric variables. Adding a trendline with an R² display quantifies how well a linear regression fits the data.

## Purpose

Use a scatter chart to answer: "Does variable X correlate with variable Y, and how strongly?" The R² value tells you what percentage of Y's variance is explained by X.

## Components

- Two numeric columns (X = independent variable, Y = dependent variable)
- Excel Insert → Scatter (X, Y)
- Right-click → Add Trendline
- Format Trendline pane: Display R² value and/or the regression equation

## Structure

```
1. Select both columns (X in one column, Y in adjacent column)
2. Insert → Scatter (X, Y) → Scatter (first option)
3. + sign → check Axis Titles → label the X axis and Y axis
4. Right-click a data point → Add Trendline
5. Format Trendline pane:
   - Linear (default)
   - ☑ Display R² value on chart
   - ☑ Display equation on chart (optional)
6. The chart shows the regression line, R², and the formula
```

## Example

Ch10 grade-absence relationship:
- X (horizontal): Number of class absences
- Y (vertical): Numeric grade (1 = lowest, 4 = highest)
- Result: R² = 0.9603 — meaning 96% of grade variation is explained by absences
- Negative relationship: more absences → lower grades
- Formula shown: `y = -0.0648x + 3.36` — slope of -0.0648 means each absence reduces the grade by ~0.065 points

## R² Interpretation

| R² Value | Interpretation |
|----------|---------------|
| 1.0 | Perfect fit — X explains 100% of Y's variance |
| 0.9–0.99 | Excellent fit |
| 0.7–0.89 | Good fit |
| 0.5–0.69 | Moderate fit |
| < 0.5 | Weak fit — X is not a good predictor of Y |
| 0 | No linear relationship |

**Important:** Correlation ≠ causation. A high R² does not prove that X causes Y.

## Variations

- **Logarithmic trendline:** Use when the relationship is diminishing (e.g., learning curves)
- **Polynomial trendline:** Use when there is a peak or valley (e.g., optimal price point)
- **Exponential trendline:** Use for growth/decay curves
- **Multiple scatter series:** Plot different groups as separate colored series on the same chart

## Notes

- Always label both axes with meaningful names — the default "X axis" and "Y axis" are meaningless
- R² displayed in decimal form (0.9603) = 96.03% of variance explained
- For prediction: plug an X value into the regression equation to predict Y

## Related

- [[descriptive-statistics-mean-median-mode-variance-stddev]] — the underlying statistical concepts
- [[dax-68-95-99-rule]] — standard deviation and the normal distribution
- [[excel-analysis-toolpak-descriptive-statistics-histogram]] — the Analysis ToolPak for descriptive statistics
