---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: reference
tags: [cdc, data-warehouse, etl, elt, change-data-capture, watermark]
---

# CDC Column Selection — Created vs Updated vs ETL Date

Choosing the right column to detect changed records is one of the most critical architectural decisions in a data warehouse. The wrong choice leads to either unnecessarily rescanning entire tables or silently missing updates.

## Quick Reference

| Column | What it captures | When to use |
|--------|-----------------|-------------|
| **ETL run date** | When the load process ran | Never — has no business meaning |
| **Created date** | When a record was first created | Insert-only tables |
| **Updated date** | When a record last changed | Upsert tables (records can be updated) |

## Notes

- **ETL run date** only shows when data arrived in the system — it has no business meaning. It changes every load regardless of whether the data actually changed. Never use it as a CDC column.
- **Created date** catches new records but misses subsequent updates. Use for tables where records are written once and never changed (insert-only behavior).
- **Updated date** captures the business event of a record changing. Use for upsert behavior where records can be modified over time.
- A **watermark table** (control table) tracks the last successfully loaded value of the chosen CDC column for each source table — the load picks up from where it left off.

## Practical Rule

> For upsert tables: use the updated date. For insert-only tables: use the created date.

If unsure which behavior applies, ask the source system team — this decision propagates into every downstream load and cannot be easily changed retroactively.

## Related

- [[medallion-architecture-raw-cleansed-dimensional]] — where CDC fits in the medallion layers
- [[multi-source-merge-archive-priority-load-sequencing]] — load sequencing that respects CDC
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
