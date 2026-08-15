---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, measure-table, organization]
note_type: pattern

---

# Measure Tables in Power BI

Creating a central hidden table to organize and display measures in Power BI.

## Purpose

Measures are not stored in tables — they float in the model namespace. A measure table provides a visual container in the Fields pane, making it easier to find and organize measures by category.

## How to Create

In Power Query Editor:
1. Home tab → Get data → Blank query
2. Rename query to `Calculations`
3. Close & Apply

This creates an empty table that holds no data but provides a namespace for measures.

Alternative methods:
- **Enter data:** create a single-row table with `Calculations = { "" }`
- **DAX calculated table:** `Calculations = { "" }`

Hide the table in the report view.

## Structure

```dax
-- Calculated table approach
Calculations = { "" }
```

Assign measures to this table by editing each measure's properties.

## Benefits

- Logical grouping of measures by domain (Sales, Finance, HR, etc.)
- Clean Fields pane — no measures cluttering data tables
- Easier navigation for report authors

## Related

- [[date-table-creation-in-dax]]
- [[no-calculate-dax-pattern]]
