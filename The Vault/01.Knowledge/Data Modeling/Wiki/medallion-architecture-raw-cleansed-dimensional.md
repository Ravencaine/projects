---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: reference
tags: [data-warehouse, medallion, elt, cdc, bronze, silver, gold, architecture]
---

# Medallion Architecture: Raw / Cleansed / Dimensional Layers

Three-layer data warehouse architecture adapted from the medallion pattern (bronze/silver/gold). Separates concerns: what arrived, what is correct, and how to analyze it.

## Quick Reference

| Layer | Alias | Purpose |
|-------|-------|---------|
| **Raw** | Bronze | Exact copy of source data — no transformations |
| **Cleansed** | Silver | Standardized column names, removed junk, CDC established |
| **Dimensional** | Gold | Kimball fact/dimension model — queried by BI tool |

## Raw Layer

Stores source system data exactly as-is. Acts as a safety net: if something goes wrong at the source, the raw layer answers "what actually came in?" No data is ever modified at this layer.

## Cleansed Layer

Applies the first meaningful transformation pass:

- Standardize column names across sources
- Remove unnecessary columns
- Establish CDC (Change Data Capture) mechanism
- Resolve data quality issues before they reach the dimensional model

This layer answers: "what is correct and reliable?"

## Dimensional Layer

Kimball fact and dimension tables. This layer focuses solely on modeling decisions (grain, relationships, conformed dimensions) without simultaneously wrestling with dirty data.

Answers: "how should this be analyzed?"

## Why Three Layers, Not Two

- **Easier debugging** — isolate whether an error is in the source, transformation logic, or modeling decision
- **Flexibility to reprocess** — can rebuild the dimensional layer from scratch without returning to source systems
- **Separation of concerns** — each layer changes at a different rate and requires different expertise

## ELT Pattern

Transform data inside the target system (SQL) rather than in a separate processing layer. Modern databases handle transformation efficiently; a dedicated transformation cluster may not justify the cost.

## Related

- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
- [[cdc-column-selection-created-vs-updated-vs-etl-date]] — CDC discipline
- [[surrogate-key-pragmatism-when-to-use-natural-keys]] — measured surrogate key usage in this architecture
