---
created: 2026-08-02
updated: 2026-08-02
source: Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md
note_type: pattern
tags: [power-bi, pattern, invoked-function, data-model, custom-column]
---

# Invoked Function Table in Power BI

After expanding a record-valued Custom Column in Power Query, Power BI creates a separate table in the data model called "Invoked Function." This table contains the expanded sub-columns and is linked to the source table.

## What It Is

When you use a record literal in a Custom Column and expand it, Power Query converts the record column into a separate table. In the Power BI data model, this appears as:

- A new table (named after the Custom Column, e.g., `Multiple_Columns`)
- A one-to-many relationship from the source table to the new table
- Sub-columns: each key in the record literal becomes a column in the new table

## Model View Appearance

```
[Source Table] ──1:many──> [Invoked Function Table]
  Sales                            Cost
  Profit                           ProfitPct
  ...                              Comm
```

## Using the Expanded Columns

1. Go to Report view
2. In the Data pane, expand the Invoked Function table
3. Drag columns from this table into visuals like any other column
4. The relationship to the source table means the expanded columns filter correctly by the source row context

## Notes

- The Invoked Function table behaves like any other dimension/fact table in the model — it can be used in visuals, relationships, and DAX measures.
- If you only need the columns in the context of the source table (not as a separate table), a different approach (e.g., `ADDCOLUMNS` in DAX) may be preferable.
- The relationship is automatically created by Power Query when the record column is expanded.
- PBIX files with this pattern can be downloaded from the author's provided links.

## Related

- [[single-formula-multiple-columns-power-query]] — `pattern`
- [[power-query-custom-column-workflow]] — `pattern`
