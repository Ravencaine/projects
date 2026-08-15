---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: atomic
tags: [power-bi, dax, quick-queries, column-statistics, distinct-count, atomic]
---

# Quick Queries Column Statistics Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

Show Column Statistics (via Quick Queries) provides per-column statistics for an entire table with a single right-click. Useful for data profiling — surfaces cardinality, nulls, and distribution before writing measures.

## What it returns

| Statistic | What it shows |
|-----------|--------------|
| Distinct values count | How many unique values in the column |
| Total rows | Row count in the column |
| Min / Max | For numeric and date columns |
| Distribution flags | Null presence, empty strings |

## Use cases

- **Before modeling**: identify high-cardinality columns that may cause performance issues
- **Data quality audit**: find columns with unexpected nulls or single dominant values
- **Choosing slicer candidates**: columns with 2-20 distinct values make good slicers

## Related

- [[quick-queries-right-click-templates]] — how to access Show Column Statistics
- [[quick-queries-workflow]] — full Quick Queries workflow
