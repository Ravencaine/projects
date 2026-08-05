---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling!.md"
source_url: "https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-0410bdb8c080"
note_type: source
tags: [power-bi, data-modeling, beginner, star-schema, snowflake, relationships, fact-table, dimension-table]
---

# Data Modeling Part 1 — Janvi Gupta

> **Type:** tutorial / beginner guide
> **Author:** Janvi Gupta
> **Published:** 2025-12-15
> **URL:** https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-0410bdb8c080
> **Routed to:** Power BI
> **KB:** Power BI

## Summary

Part 1 of the data modeling series. Covers why flat-table Excel approaches break in Power BI, the concept of relationships as invisible bridges, four relationship types (one-to-many, many-to-one, many-to-many, one-to-one), fact vs dimension tables, and star schema vs snowflake schema. Core insight: the most common Power BI mistake is a relationship problem that inflates every number by duplicating rows across many-to-many connections.

## Key Insight

Power BI multiplies every measure when relationships form a loop or use many-to-many cardinality. A $4.7M source total showing as $47M is almost always a relationship problem — not a DAX problem.

## Extracted Notes

- [[excel-flat-table-problems]] — `atomic` — flat tables: duplication, update nightmares, file bloat; Power BI's split-and-connect approach
- [[relationship-types-one-to-many-many-to-many]] — `atomic` — 1:Many (standard), Many:Many (bridge table needed), 1:1 (merge instead); bidirectional filter dangers
- [[fact-table-vs-dimension-table]] — `atomic` — fact tables answer "what happened" (events, transactions); dimension tables answer "who/what/when/where" (descriptive attributes)
- [[star-schema-vs-snowflake-schema]] — `atomic` — star schema: one fact, dimension tables directly connected; snowflake: normalised dimensions; star is faster

## Metadata

| Field | Value |
|-------|-------|
| Source file | Master Power BI Introduction to Data Modeling!.md |
| Ingestion date | 2026-08-01 |
| Word count | ~3,500 |
| Level | Beginner |
| Category | Data Model |
