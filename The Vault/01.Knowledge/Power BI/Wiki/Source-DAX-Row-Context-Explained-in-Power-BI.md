---
created: 2026-08-09
updated: 2026-08-09
source: "DAX Row Context Explained in Power BI.md"
source_url: https://databear.com/dax-row-context-power-bi/
note_type: source
tags: [dax, row-context, iterator, filter-context, selectcolumns, summarize, boniface-muchendu]
---

# DAX Row Context Explained in Power BI

DAX row context exists when a calculation iterates row by row over a table. Created by iterator functions (SUMX, AVERAGEX, ADDCOLUMNS) and calculated columns.

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2026-03-13
> **URL:** https://databear.com/dax-row-context-power-bi/
> **Routed to:** Power BI

## Summary

Row context is the "current row" during iteration. It enables column references inside iterators. The article explains: how row context is visualized as a single-row table, the two scenarios where it exists (iterators + calculated columns), how row context and filter context combine, using SELECTEDVALUE inside iterators, and how table expression cardinality affects iteration results (SELECTCOLUMNS keeps rows, SUMMARIZE can reduce them).

## Key Claims

- Row context = current row during iteration; iterator creates it, calculated columns have it automatically
- Column references (Table[Column]) require row context to be meaningful
- Filter context limits which rows are visible; row context iterates over them
- SELECTEDVALUE inside an iterator reads from filter context (slicer selection) — retrieve before iteration for cleanliness
- SELECTCOLUMNS keeps the same row count; SUMMARIZE can collapse duplicates and change iteration cardinality
- Always verify the cardinality of the table expression passed to an iterator

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Row Context Explained in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~900 |
