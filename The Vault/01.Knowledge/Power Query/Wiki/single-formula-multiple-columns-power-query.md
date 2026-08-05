---
created: 2026-08-02
updated: 2026-08-02
source: Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md
note_type: pattern
tags: [power-query, pattern, custom-column, m, record-syntax]
---

# Single Formula → Multiple Columns in Power Query

Use Power Query's record literal syntax inside a Custom Column to define multiple calculations in one formula, then expand them into separate columns. This eliminates repeated Add Custom Column steps and enforces a single shared logic path for all derived outputs.

## Purpose

Replaces N separate Custom Column steps with one step that produces N output columns. All calculations derive from the same row context and share the same formula expression, so logic is consistent and the step count stays low.

## M Code

```m
[
    Cost     = [Sales] - [Profit],
    ProfitPct = [Profit] / [Sales],
    Comm     = 0.1 * [Profit]
]
```

Paste this into the Custom Column Formula field. Name the column (e.g., `Multiple_Columns`). The result is a record-valued column where each key becomes a sub-column after expansion.

## Steps

1. Open Power Query: Home → Transform Data
2. Select the source table
3. Add Column → Custom Column
4. Name the column (e.g., `Multiple_Columns`)
5. Enter the record literal formula above, substituting column names for your own
6. Click the expand icon (two arrows) on the right side of the column header
7. Select the sub-columns to keep (Cost, ProfitPct, Comm)
8. Close & Apply

## Benefits

- **Efficiency**: one step instead of N steps
- **Consistency**: all calculations share the same row context and formula structure
- **Scalability**: add new outputs by adding key/value pairs to the record literal
- **Auditability**: the single formula step documents all derived columns at once

## Notes

- The formula must return a record. Each key in the record becomes a column name after expansion.
- The record is evaluated per row — no row context shift.
- Column names used inside the formula must exactly match existing column names (case-sensitive in M).
- After expansion, the original `Multiple_Columns` record column can be removed.

## Related

- [[power-query-custom-column-workflow]] — `pattern`
- [[five-benefits-single-formula-design]] — `atomic`
- [[invoked-function-table-power-bi]] — `pattern`
