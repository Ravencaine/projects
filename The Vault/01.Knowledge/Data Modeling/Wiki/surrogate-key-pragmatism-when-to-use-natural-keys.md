---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: pattern
tags: [data-warehouse, dimensional-modeling, surrogate-key, natural-key, performance, kimball]
---

# Surrogate Key Pragmatism — When to Use Natural Keys

Classic Kimball recommends surrogate keys for all fact table foreign keys. A pragmatic approach: use surrogate keys only where they add value — low-cardinality dimensions — and use natural keys directly for high-volume, frequently-joined tables.

## Definition

- **Surrogate key:** artificial, system-generated key (integer sequence, UUID) with no business meaning
- **Natural key:** a key that exists in the source data (UUID, composite natural key)

## Pragmatic Rule

| Table type | Recommendation |
|-----------|---------------|
| Low-cardinality dimensions (status, priority, category) | Surrogate key — small lookup table, benefit outweighs cost |
| High-volume fact tables | Natural key (source UUID) — avoids unnecessary surrogate key generation and join lookup overhead |

## When Surrogate Keys Matter

- Historical tracking (Type 2 SCD) is needed — the surrogate key persists through attribute changes
- The natural key can change over time (rare but possible)
- The dimension is reused across multiple fact tables (conformed dimension)

## When Natural Keys Are Fine

- High-volume fact table with a stable source UUID
- The source key has good cardinality and won't change
- No Type 2 historical tracking requirements

## Notes

Using natural keys for fact tables reduces one join during ETL (no surrogate key lookup) and avoids the overhead of generating and maintaining a parallel key system. The tradeoff is that dimensional model consumers need to understand the source system's key convention.

## Related

- [[medallion-architecture-raw-cleansed-dimensional]] — where this decision fits in the medallion layers
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
