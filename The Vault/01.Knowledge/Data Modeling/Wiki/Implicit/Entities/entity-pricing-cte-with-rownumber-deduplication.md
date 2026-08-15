---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: entity
tags: [entity, pricing, Data Modeling]
---

# Pricing CTE with ROW_NUMBER Deduplication

<!-- A SQL CTE pattern that partitions PriceDiscTable rows by item and uses ROW_NUMBER ordered by fromdate to pick the latest applicable price deterministically. -->

## Definition

A SQL CTE pattern that partitions PriceDiscTable rows by item and uses ROW_NUMBER ordered by fromdate to pick the latest applicable price deterministically.
