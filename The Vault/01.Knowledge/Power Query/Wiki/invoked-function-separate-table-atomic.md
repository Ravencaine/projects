---
created: 2026-08-09
updated: 2026-08-09
source: "Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md"
note_type: atomic
tags: [power-query, invoked-function, data-pane, table, atomic]
---

# Invoked Function Separate Table Atomic

**Type:** Atomic · **KB:** Power Query · **Source:** [[Source-Multiple-Calculations-Single-Formula-Power-Query]]

After expanding a record-returning Custom Column and clicking Close & Apply, the expanded columns appear in the Power BI **Data pane under the same query-named table:** not as a separate table. The transformation is internally referred to as an "Invoked Function" in the M layer.

## What happens

1. Custom Column returns a record
2. Record is expanded in Power Query Editor
3. Close & Apply is clicked
4. In the Data pane: the query-named table (`Multiple_Columns`) now contains both original and expanded columns

The "Invoked Function" label refers to the underlying M call; visually the columns are part of the source table.

## Key properties

- Columns are in the same semantic model table as the original query
- No separate relationship needed
- Usable in visuals alongside original columns
- Refresh is automatic

## Related

- [[single-formula-multiple-columns-power-query]] — the record syntax
- [[power-query-custom-column-workflow]] — the workflow
