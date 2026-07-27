---
created: 2026-07-27
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: workflow
tags: [column-pruning, bravo, power-bi, performance, unused-columns]
---

# Column Pruning with Bravo for Power BI

The process of removing unused columns from a Power BI model to reduce memory footprint and improve query performance — using the open-source Bravo for Power BI tool.

## Purpose

Power BI models often accumulate columns that are never used in any visual, measure, or calculated column. These columns consume memory and add to the model's processing overhead. Identifying and removing them is called **column pruning**.

## Workflow

1. **Install Bravo for Power BI** — open-source tool available at microsoft.github.io/Bravo-for-Power-BI
2. **Open your .pbix file** in Bravo
3. **Run the Column Usage analyser** — Bravo highlights every field not used in any visual, measure, or calculated column
4. **Review exceptions** — Surrogate keys and technical columns are typically flagged but are needed for joins; note these before removing
5. **Remove flagged columns** in Power Query Editor or at source
6. **Re-measure** — re-run Bravo to confirm size reduction and query performance improvement

## Common Unused Column Types

| Type | Often Unused? | Reason |
|------|-------------|--------|
| Surrogate keys | No | Required for relationships (Bravo flags but should be kept) |
| Raw GUIDs / IDs | Sometimes | Only needed if used in relationships |
| Intermediate calculation columns | Sometimes | Built for debugging, left in model |
| Source system metadata | Often | Import-all habits from ETL |

## One Caution

Bravo flags surrogate keys as unused — they are needed for relationships even if they never appear in a visual. Before removing a flagged column, confirm it is not used in any relationship.

## Related

- [[surrogate-keys-vs-composite-keys]] — why surrogate keys are worth keeping despite Bravo flagging them
- [[incremental-refresh-pattern]] — prune before enabling incremental refresh
- [[import-vs-directquery-performance]] — model size is the key reason to prune
