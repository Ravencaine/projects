---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: atomic
tags: [dax, concept, column-oriented]
---

# DAX Is Column-Oriented — Unlike Excel Cell Formulas

DAX formulas operate on entire columns at once, not individual cells. This fundamental difference from Excel's cell-based formula model is the key to understanding DAX's behaviour and power.

## Definition

- **Excel formulas:** Applied to individual cells; each cell has its own formula. When you copy a formula, cell references update relatively or absolutely.
- **DAX formulas:** Applied to an entire column at once. A DAX formula references a column (e.g., `[TotalSales]`) and the expression evaluates for every row in that column simultaneously. There are no cell addresses.

Dunlop (Ch7): "DAX formulas differ from regular Excel formulas, which are cell-based, in that DAX formulas apply to all rows in the specified columns."

## Key Points

- DAX column reference syntax: `TableName[ColumnName]` or just `[ColumnName]` when already in the correct table context
- Fully qualified column names include the table name: `dbo_FactSales[TotalSales]`
- If a table name has a space, enclose it in single quotes: `'Order Details'[UnitPrice]`
- Up to 64 levels of function nesting are supported in a single DAX expression
- DAX is evaluated in two contexts simultaneously: **filter context** (what's currently filtered) and **row context** (which row is being evaluated)
- Excel's AutoSum in DAX defaults to referencing the entire column — no range selection needed

## Examples

```dax
-- DAX: references the entire TotalSales column
Total Sales := SUM(dbo_FactSales[TotalSales])

-- Excel equivalent: each cell has a SUM formula pointing to a specific range
=SUM(Sheet1!$D$2:$D$50000)
```

## Related

- [[calculated-column-vs-calculated-field]] — the two contexts where DAX formulas live
- [[dax-calculate-function]] — how filter context overrides affect DAX evaluation
- [[dax-sumx-function]] — row context and iteration
