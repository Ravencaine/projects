---
created: 2026-07-27
updated: 2026-08-02
source: "Iterators in DAX: SUMX, AVERAGEX, RANKX and How They Use Row & Filter Context"
source_url: "https://medium.com/write-your-world/iterators-in-dax-sumx-averagex-rankx-and-how-they-use-row-filter-context-711bfa11297a"
note_type: source
tags: [dax, iterators, sumx, averagex, rankx, row-context, filter-context]
---

# Iterators in DAX: SUMX, AVERAGEX, RANKX

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-09-26
> **URL:** https://medium.com/write-your-world/iterators-in-dax-sumx-averagex-rankx-and-how-they-use-row-filter-context-711bfa11297a
> **Routed to:** DAX Code

## Summary

DAX iterators (SUMX, AVERAGEX, RANKX) loop row-by-row over a table, creating row context and optionally triggering context transition when CALCULATE is involved. Aggregators (SUM, AVERAGE) work on a column directly; iterators evaluate an expression per row then aggregate.

## Key Claims

- Iterators end in X (SUMX, AVERAGEX, RANKX, MAXX, MINX) and create row context
- Iterators trigger context transition when CALCULATE is used inside them
- RANKX without ALL() causes all items to rank as "1" (each item only sees itself)
- Use aggregators (SUM, AVERAGE) whenever possible; only use iterators when row-level logic is required

## Extracted Notes

- [[sumx]] — function
- [[averagex]] — function
- [[rankx]] — function
- [[iterator-vs-aggregator-comparison]] — comparison

## Metadata

| Field | Value |
|-------|-------|
| Source file | Iterators in DAX SUMX, AVERAGEX, RANKX and How They Use Row & Filter Context 1.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~750 |
