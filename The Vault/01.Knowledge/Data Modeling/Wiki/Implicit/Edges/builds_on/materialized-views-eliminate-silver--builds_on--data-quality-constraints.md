---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[materialized-views-eliminate-silver]]"
target_node: "[[data-quality-constraints]]"
weight: 1
---

# Materialized Views Can Eliminate Silver Layer builds_on Data Quality Constraints

<!-- Materialized views enforce data quality constraints (NOT NULL, positive values, required fields) directly in the Curated layer. -->

## Edge

`[[materialized-views-eliminate-silver]]` -- **builds_on** -> `[[data-quality-constraints]]`

## Evidence

Materialized views enforce data quality constraints (NOT NULL, positive values, required fields) directly in the Curated layer.


## Related

- [[materialized-views-eliminate-silver]]
- [[data-quality-constraints]]
