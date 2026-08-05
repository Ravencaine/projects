---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: comparison
tags: [directquery, import, power-bi, storage-mode, performance]
---

# Import vs DirectQuery Performance

## Summary

Import reads data from memory and is faster for most models. DirectQuery queries the source database on every interaction and is slower but necessary for very large or frequently-changing datasets.

## Import Mode

### Pros
- Reads from RAM — orders of magnitude faster than disk queries
- Full DAX expressiveness — no formula restrictions
- Works fully offline

### Cons
- Model size limited by Power BI capacity (100 MB – 50 GB depending on Pro/Premium/Per-User)
- Data refresh required to pick up source changes
- Not suitable for real-time data

## DirectQuery Mode

### Pros
- No model size limit (data stays in source)
- Always live to the latest source data
- Suitable for very large or frequently-changing datasets

### Cons
- Every visual interaction fires a query against the source database
- Performance entirely dependent on source query speed
- Many DAX restrictions apply
- Many-to-many relationships have more complexity

## When to Use Each

| Scenario | Recommended Mode |
|----------|----------------|
| Model under 1 GB, data updates on schedule | Import |
| Data over 10 GB | DirectQuery or Aggregations |
| Append-only large tables (GA4, daily feeds) | Import + Incremental Refresh |
| Near-real-time requirements | DirectQuery or Composite Model |
| Enterprise DW (Synapse, Snowflake) | Import (preferred if model fits) |

## Related

- [[incremental-refresh-pattern]] — companion to Import for append-only large tables
- [[star-schema-vs-snowflake-schema]] — schema design that supports fast Import models
