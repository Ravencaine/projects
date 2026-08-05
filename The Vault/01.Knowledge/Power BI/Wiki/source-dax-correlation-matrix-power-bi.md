---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: source
tags: [powerbi, dax, correlation, matrix, scatter-chart, tutorial]
---

# Source: How to Build a Correlation Matrix in Power BI Using Only DAX

> Author: Isabelle Bittar
> Published: 2025-08-24
> URL: https://medium.com/microsoft-power-bi/how-to-build-a-correlation-matrix-in-power-bi-using-only-dax-ab611a19a194
> Level: Beginner | Category: Data Visualization, DAX

## Introduction

Build a fully dynamic, interactive correlation matrix in Power BI using only DAX — no Python, R, or external tools. The matrix responds to report filters and slicers and includes an interactive scatter chart tooltip showing individual data points behind each correlation.

Use case: tactical HR dashboard where advisors identify relationships between Engagement, Performance, Overtime hours, and other HR indicators.

## Correlation Matrix

### Pearson Correlation Coefficient

Each cell shows the Pearson correlation coefficient (r) between two variables, ranging from -1 to +1:
- **+1**: perfect positive correlation
- **0**: no linear relationship
- **-1**: perfect negative correlation

Formula:
$$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2} \cdot \sqrt{\sum(y_i - \bar{y})^2}}$$

### Variable Axis Tables

Two identical DATATABLE calculated tables (`VariablesX`, `VariablesY`) list the 6 variables in the matrix.

### Core Correlation Measure

Uses SUMMARIZE to collapse to one row per employee (respecting all report filters), ADDCOLUMNS + SWITCH to map variable names to numeric columns, then computes numerator and denominator of Pearson formula.

### Lower Triangle Variant

Wraps the core measure to hide the upper triangle and diagonal (XName <= YName → BLANK), leaving only the lower triangle visible.

### Color Buckets

DAX measures for cell background and font color using fixed thresholds (not Power BI's built-in gradient) so colors remain accurate under filtered contexts.

### Interactive Tooltip

Tooltip page with scatter chart (X Value / Y Value measures mapped via SWITCH) showing individual employee data points. Includes HTML-based subtitle with colored correlation badge and plain-language explanation of direction.

### Key Features

- 100% DAX — no external tools
- Fully interactive with report filters
- Scatter plot tooltip showing raw data behind each correlation
- Color legend and info tooltip for non-technical users

## PBIX Download

[[Correlation Matrix.pbix]]
