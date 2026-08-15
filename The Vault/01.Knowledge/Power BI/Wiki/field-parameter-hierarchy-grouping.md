---
created: 2026-08-11
updated: 2026-08-11
source: "5-Power-BI-Slicer-Tricks-Goodly-Transcript.md"
note_type: pattern
tags: [power-bi, field-parameters, kpi]
---

# Fields Parameter Hierarchies — Grouping Measures in Slicers

Fields parameters create a slicer from column values. Extend this by adding a custom column to the parameter's hidden table to group values into hierarchies.

## How It Works

1. Create a Field Parameter with measures or columns
2. Power BI creates a hidden helper table with columns: `Parameter`, `Parameter Order`, and optionally `Parameter Fields`
3. Add a custom column to that table (e.g., `Tag`) categorizing items:

```
Parameter         | Parameter Order | Tag
Total Sales      | 1              | Sales
Pseudo Sales     | 2              | Sales
Commissions      | 3              | Earnings
More Commission  | 4              | Earnings
```

4. Put `Tag` above `Parameter` in the slicer field well → creates a hierarchy slicer with groupings
5. Users expand/collapse groups in the slicer

## Use Case

KPI slicer: group measures under "Sales" and "Earnings" headings — cleaner than a flat list.

## Related

- [[field-parameter-show-values-trick]] — show values of selected field
- [[field-parameters-dynamic-axis]] — dynamic measure/dimension switching
