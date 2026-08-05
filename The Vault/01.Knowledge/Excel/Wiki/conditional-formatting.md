---
created: 2026-07-26
updated: 2026-08-02
source: "Beyond VLOOKUP: Unleashing Excel's True Data Power for Business Analysis"
source_url: https://medium.com/@harsh1995hg/beyond-vlookup-unleashing-excels-true-data-power-for-business-analysis-33e9c54a66c4
note_type: pattern
tags: [excel, conditional-formatting, visualisation, data-analysis]
---

# Conditional Formatting Pattern

Apply visual rules to data so patterns, outliers, and threshold breaches are immediately visible without scanning numbers manually.

## Purpose

Transform raw numeric or categorical data into a visual layer — colour scales, icon sets, data bars, or threshold-based fills — that surfaces what matters at a glance.

## Components

1. **Colour scales**: Gradient fill from low (one colour) to high (another colour) across a range.
2. **Data bars**: Horizontal bars proportional to the cell value within the range.
3. **Icon sets**: Shapes, arrows, or traffic-light symbols assigned by rule thresholds.
4. **Threshold rules**: Specific rules triggered by a condition (e.g., value > 1000, text = "Overdue").

## Structure

```
Home → Conditional Formatting → New Rule
```

Choose a rule type:

| Rule type | Use when |
|-----------|--------|
| Format all cells based on their values | Colour scales, data bars |
| Format only cells that contain | Threshold rules on values, dates, text |
| Format only top or bottom ranked values | Highlight top 10%, bottom 5, etc. |
| Format only values that are above or below average | One-standard-deviation reads |
| Format only unique or duplicate values | Deduplication checks |
| Use a formula to determine which cells to format | Custom dynamic rules |

Apply the desired format, set the range (typically the full column of data), and confirm.

## Example

**Highlight overdue invoices:**
1. Select the "Status" column.
2. Home → Conditional Formatting → New Rule → "Format only cells that contain."
3. Cell Value → equal to → `"Overdue"`.
4. Set fill colour to red, font to white bold.
5. All overdue rows highlight instantly.

**Traffic-light KPI indicators on a Pivot Table:**
1. Select the Values area of the pivot.
2. Conditional Formatting → Icon Sets → 3 Traffic Lights (Uncyclic).
3. Manage Rules → Edit Rule → set thresholds (e.g., Red < 70%, Amber 70–85%, Green > 85%).

## Variations

- **Two-colour scale**: Min = red, Max = green — useful for error rates (lower is better).
- **Formula-based rules**: Apply to entire rows based on a value in one column: `=$D2="Overdue"` applied to the full row range.
- **Bar-only**: Data bars without number display: `Conditional Formatting → Data Bars → Show Bar Only` — clean dashboard look.

## Related

- [[pivot-tables]] — commonly the data source for conditional formatting dashboards
- [[excel-as-bi-tool]] — visual insight as part of the Excel BI toolkit
