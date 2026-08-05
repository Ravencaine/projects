---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
source_url: "https://medium.com/towards-artificial-intelligence/my-power-bi-report-took-14-seconds-to-load-heres-everything-i-did-to-get-it-under-2-7ef5de8f5214"
note_type: source
tags: [power-bi, performance, optimization, star-schema, vertipaq, dax, direct-lake]
---

# Power BI Performance Optimization — Sheth Priyanka

> **Type:** case study / performance guide
> **Author:** Sheth Priyanka
> **Published:** 2026-07-24
> **URL:** https://medium.com/towards-artificial-intelligence/my-power-bi-report-took-14-seconds-to-load-heres-everything-i-did-to-get-it-under-2-7ef5de8f5214
> **Routed to:** Power BI
> **KB:** Power BI

## Summary

Real-world case study: 14s → 1.8s on same hardware, no Premium. Seven fixes, ordered by impact. Results: 86% faster load, worst visual DAX query 8.9s → 0.6s, model 210MB → 129MB. Core message: slow reports are almost always a data model problem, not a hardware problem.

## Extracted Notes

- [[performance-analyzer-workflow]] — `atomic` — Performance Analyzer: DAX query vs visual display vs other; find slow visual before touching anything
- [[star-schema-performance-impact]] — `atomic` — flat table → star schema: fact + dimensions; single-direction relationships; biggest single win (~50% reduction)
- [[vertipaq-column-cardinality]] — `atomic` — VertiPaq compresses column-by-column; cardinality drives size more than row count; remove unused and high-cardinality columns
- [[auto-date-time-disable]] — `atomic` — turn off Auto Date/Time; split DateTime into Date + Time; build one shared DimDate
- [[dax-measure-optimization-patterns]] — `atomic` — push heavy math upstream; SUM over SUMX where possible; precompute in Power Query; measure branching
- [[visual-canvas-reduction]] — `atomic` — fewer visuals, fewer slicers, edit interactions to disable cross-filtering; each visual = one query
- [[direct-lake-vs-import]] — `atomic` — Direct Lake reads Delta tables from OneLake; avoids import refresh; not a substitute for good modeling; incremental refresh for large models

## Metadata

| Field | Value |
|-------|-------|
| Source file | My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md |
| Ingestion date | 2026-08-01 |
| Word count | ~3,000 |
| Level | Intermediate |
| Category | Performance |
