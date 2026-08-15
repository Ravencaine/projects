---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: workflow
tags: [powerbi, dax, correlation, matrix, scatter-chart, tooltip, visualization]
---

# DAX Correlation Matrix in Power BI

Build a fully dynamic, interactive correlation matrix in Power BI using only DAX — no external tools or Python required. The matrix responds to report filters and includes an interactive scatter chart tooltip.

## Prerequisites

- Power BI Desktop
- A fact table with numeric columns (e.g., HR Data with Performance Rating, Training Hours, Overtime Hours, etc.)
- One row per observation/entity in the fact table (e.g., one row per employee)

## Steps

### 1. Create the variable axis tables

Create two identical `DATATABLE` calculated tables listing all numeric variables to include in the matrix:

```c
VariablesX = DATATABLE ( "Variable", STRING, { { "Performance Rating" }, { "Training Hours Completed" }, ... } )
VariablesY = DATATABLE ( "Variable", STRING, { { "Performance Rating" }, { "Training Hours Completed" }, ... } )
```

See [[variablesx-variablesy-tables]].

### 2. Build the core Correlation measure

The `Correlation` measure computes the Pearson coefficient between the variables selected in the matrix rows and columns. See [[pearson-correlation-measure]] for the full formula.

### 3. Build the Lower Triangle measure

Replace `Correlation` in the Matrix Values with `Correlation (Lower Triangle, No Diagonal)` to hide the diagonal and upper triangle. See [[lower-triangle-no-diagonal-correlation]].

### 4. Create color bucket measures

Define a color palette and two color measures for cell background and font color. See [[correlation-color-buckets]].

### 5. Build the Matrix visual

1. Add a **Matrix** visual.
2. Add `VariablesX[Variable]` to **Rows**.
3. Add `VariablesY[Variable]` to **Columns**.
4. Add `Correlation (Lower Triangle, No Diagonal)` to **Values**.
5. Apply formatting: Style preset "None", remove row/column subtotals, white borders, adjust row padding.
6. Apply conditional formatting: **Cell elements → Field value → Background** = `Correlation Color (Buckets)`, **Font color** = `Correlation Font Color`.

### 6. Create the scatter tooltip page

1. Add a new report page → **Page Type** = **Tooltip**.
2. Resize to ~400px × 500px.
3. Add `X Value`, `Y Value`, and `Employee ID` from the fact table to a **Scatter chart** (X Axis, Y Axis, Details respectively).
4. Add **Trend line** under Analysis pane.
5. Create a dynamic title: `Scatter Title = [Selected X Name] & " vs " & [Selected Y Name]`.
6. Add the HTML subtitle measure for the correlation badge and plain-language explanation. See [[html-scatter-subtitle-badge]].
7. Assign this page as the tooltip page for the correlation matrix.

### 7. Add final enhancements

- **Color legend** on the report page.
- **Info tooltip** explaining how to read the matrix.
- **Visual-level slicer** for department or role filtering.

## Key Takeaways

- **100% DAX:** no Python, R, or external services.
- **Fully interactive:** responds to all report filters and slicers.
- **Interactive tooltip:** scatter plot with trend line shows individual observations behind each correlation.
- **Scalable:** add/remove variables by editing the DATATABLE entries.
- **Context-aware:** colors remain meaningful under filtered contexts because bucket thresholds are fixed, not gradient-based.

## Related

- [[pearson-correlation-coefficient]]
- [[variablesx-variablesy-tables]]
- [[pearson-correlation-measure]]
- [[lower-triangle-no-diagonal-correlation]]
- [[correlation-color-buckets]]
- [[scatter-tooltip-x-y-value-measures]]
- [[html-scatter-subtitle-badge]]
