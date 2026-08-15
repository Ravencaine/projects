---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: entity
tags: [entity, etl, Data Modeling]
---

# Multi-Source Merge Pattern

<!-- A data warehouse load pattern for merging the same entity from multiple source tables where archive always takes priority. Requires a three-step load sequence: upsert archive first, delete stale active rows, upsert remaining active. Prevents double-counting. -->

## Definition

A data warehouse load pattern for merging the same entity from multiple source tables where archive always takes priority. Requires a three-step load sequence: upsert archive first, delete stale active rows, upsert remaining active. Prevents double-counting.
