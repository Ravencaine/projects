---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring the New DAX Query View in Power BI.md"
note_type: atomic
tags: [power-bi, dax, quick-queries, right-click, template, atomic]
---

# Quick Queries Right Click Templates Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-dax-query-view-power-bi]]

Quick Queries are predefined DAX query templates accessible by right-clicking any table, column, or measure in the Data Pane. They generate ready-to-run DAX without manual coding — ideal for fast data exploration.

## How to access

1. In the DAX Query View, locate the **Data Pane** (right side)
2. Right-click any **table, column, or measure**
3. Select **Quick Queries** from the context menu

## Available templates

| Template | What it does | DAX generated |
|----------|-------------|---------------|
| **Show Top 100 Rows** | Returns first 100 rows of selected table | `EVALUATE TOPN(100, Table)` |
| **Show Column Statistics** | Key stats per column: distinct count, total rows | Internal DAX statistics query |

## Typical workflow

1. Right-click table → Quick Queries → **Show Top 100 Rows**
2. Query auto-executes; results appear in Results pane
3. Edit the generated DAX (change row count, add FILTER, ORDER BY)
4. Save as a new Query Page for reuse

## Edit and save

After running a Quick Query, the generated DAX can be edited. Save the modified query as a new Query Page within the .pbix — it persists across sessions.

## Related

- [[quick-queries-column-statistics]] — what Show Column Statistics reveals
- [[evaluate-basic-query-run-workflow]] — running and editing generated queries
- [[quick-queries-workflow]] — full Quick Queries workflow
