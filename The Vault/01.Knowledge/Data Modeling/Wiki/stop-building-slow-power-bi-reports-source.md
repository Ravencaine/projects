---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: source
tags: [power-bi, performance, checklist]
---

# Stop Building Slow Power BI Reports: A Data Pro's Checklist

A Medium article by Bill Donofrio presenting a 10-point checklist of Power BI performance mistakes — from star schema basics through surrogate keys, granularity, many-to-many joins, DirectQuery vs Import, incremental refresh, and column pruning.

> **Type:** article
> **Author:** Bill Donofrio
> **Published:** 2026-07-20
> **URL:** https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c
> **Routed to:** Data Modeling / Power BI

## Summary

A practitioner's checklist of Power BI performance anti-patterns, organised from most severe to least. Each item is illustrated with a real rebuild story. Key themes: star schema is non-negotiable, integer surrogate keys are essential, correct granularity prevents expensive in-memory recalculation, bridge tables solve many-to-many safely, and Bravo for Power BI helps identify unused columns for pruning.

## Key Claims

- Star schema is mandatory — importing 10 Excel files and letting Power BI auto-join them causes cascading performance collapse
- Composite keys (multi-column string joins) are slow; surrogate integer keys are 4 bytes vs multi-byte strings, a massive memory saving at scale
- SLOWLY CHANGING DIMENSIONS at wrong granularity (joining fact tables to type-2 SCD tables) causes full table recalculation in memory — the fix is a surrogate key on every record so inactive SCD rows are never in the fact table
- Many-to-many relationships in Power BI should be avoided; bridge tables keep respondent-to-answer counts clean
- Pre-built date hierarchies should be replaced with a custom dim_date table for flexibility and single-table control
- DirectQuery is slower than Import (reading from disk vs memory); use Import for most models
- Incremental refresh is a game changer for append-only data (GA4, daily feeds)
- Bravo for Power BI highlights unused columns for pruning
- Pivoting answer columns into rows in SQL before import reduces fact table count
- Benchmarks first: use Power BI's Performance Analyzer before tuning

## Notable Details

- BRAVO for Power BI: open-source tool for identifying unused columns
- dim_date DAX: CALENDAR + ADDCOLUMNS pattern for a complete date dimension
- Memory comparison: tinyint = 1 byte, smallint = 2 bytes, int = 4 bytes, bigint = 8 bytes vs VARCHAR 1 byte/char, NVARCHAR 2 bytes/char

## Extracted Notes

Links to notes derived from this source:

- [[star-schema-vs-snowflake-schema]] — extended with mandatory checklist context
- [[surrogate-keys-vs-composite-keys]] — `pattern` — integer surrogate key design
- [[power-bi-correct-granularity-and-scd]] — `atomic` — SCD at wrong granularity kills performance
- [[many-to-many-bridge-table-pattern]] — `pattern` — bridge tables for many-to-many
- [[dim-date-dax-calendar]] — `reference` — dim_date DAX implementation
- [[import-vs-directquery-performance]] — `comparison` — when to use each
- [[incremental-refresh-pattern]] — `pattern` — append-only incremental refresh
- [[column-pruning-bravo]] — `workflow` — pruning unused columns with Bravo
- [[power-bi-visual-performance]] — `atomic` — visualisation simplicity checklist

## Metadata

| Field | Value |
|-------|-------|
| Source file | Stop Building Slow Power BI Reports: A Data Pro's Checklist.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,200 |
