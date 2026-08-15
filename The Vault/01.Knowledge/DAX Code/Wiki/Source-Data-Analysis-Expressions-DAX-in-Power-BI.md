---
created: 2026-08-09
updated: 2026-08-09
source: "Data Analysis Expressions (DAX) in Power BI.md"
source_url: https://medium.com/@dibyanshusharma16/data-analysis-expressions-dax-in-power-bi-968ecef4335b
note_type: source
tags: [dax, power-bi, beginner, vertipaq, context, aggregators, iterator, time-intelligence, reference]
---

# Data Analysis Expressions (DAX) in Power BI

A beginner-to-intermediate DAX overview covering VertiPaq engine architecture, evaluation contexts, aggregators, iterators, CALCULATE, time intelligence, and optimization.

> **Type:** article
> **Author:** Dibyanshu Sharma
> **Published:** 2025-12-21
> **URL:** https://medium.com/@dibyanshusharma16/data-analysis-expressions-dax-in-power-bi-968ecef4335b
> **Routed to:** DAX Code

## Summary

DAX is a functional language for Power BI, Azure Analysis Services, and Power Pivot. Unlike SQL (declarative), DAX is designed to calculate scalar values and tables dynamically based on user-interaction contexts. Power BI uses the VertiPaq in-memory columnar engine which compresses data and enables fast aggregation. The article covers evaluation contexts (row, filter, context transition), aggregation and iterator functions, CALCULATE and filter modifiers, time intelligence, relational functions, virtual tables, parent-child hierarchies, and optimization.

## Key Claims

- DAX recalculates dynamically based on filter context from slicers, visuals, cross-highlighting, and CALCULATE
- VertiPaq stores columns, not rows — aggregators are fast because they scan compressed columns directly
- Iterators (SUMX etc.) materialize row context and are slower than pure aggregators
- CALCULATE: copy filter context → apply modifications → evaluate expression
- FILTER scans the table it is applied to — filter dimension tables, not fact tables
- Time Intelligence requires a contiguous Date table marked as a Date Table
- Virtual table functions can be debugged by creating them as physical calculated tables
- Variables (VAR) calculate once and store in memory — use them for performance and debugging
- Bi-directional relationships cause performance issues — prefer CROSSFILTER in specific measures
- High cardinality columns (timestamps, GUIDs) compress poorly — split DateTime into Date + Time

## Extracted Notes

- [[FILTER-Dimension-Not-Fact-Performance]] — `atomic` — always filter the smallest table possible; dimension over fact
- [[Virtual-Table-Debugging-via-Calculated-Tables]] — `atomic` — create physical calculated table to inspect virtual table output

## Metadata

| Field | Value |
|-------|-------|
| Source file | Data Analysis Expressions (DAX) in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~2,500 |
| Images | 15 (function reference tables) |
