---
created: 2026-08-02
updated: 2026-08-02
source: Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md
note_type: pattern
tags: [power-query, pattern, custom-column, workflow]
---

# Power Query Custom Column Workflow

End-to-end workflow for adding, expanding, and managing Custom Columns in Power Query — from the Add Column tab through to Close & Apply.

## Add Custom Column

1. Select the source query/table in the Queries pane
2. Go to Add Column → Custom Column
3. Enter a column name (no spaces — Power Query replaces them with underscores)
4. Enter the M expression in the formula field
5. Click OK

## Common Patterns

### Simple calculation
```m
[Profit] - [Sales]
```

### Record literal (multiple outputs)
```m
[
    Cost      = [Sales] - [Profit],
    ProfitPct = [Profit] / [Sales],
    Comm      = 0.1 * [Profit]
]
```

### Conditional logic
```m
if [Sales] > 12000 then "High"
else if [Sales] > 10000 then "Medium"
else "Low"
```

## Expand Record Column

After creating a record-valued column:

1. Click the expand icon (two arrows) on the right side of the column header
2. Check the sub-columns to include
3. Uncheck "Use original column name as prefix" if you want clean names
4. Optionally remove the source record column after expansion

## Remove the Source Column

After expansion, right-click the record column → Remove to clean up.

## Close & Apply

- Click Close & Apply in the Home tab to load the transformed table into the data model
- The new columns appear in the Data pane as part of the table
- In the model view, the table shows as `Invoked Function` if created via the record expansion approach

## Related

- [[single-formula-multiple-columns-power-query]] — `pattern`
- [[five-benefits-single-formula-design]] — `atomic`
- [[invoked-function-table-power-bi]] — `pattern`
