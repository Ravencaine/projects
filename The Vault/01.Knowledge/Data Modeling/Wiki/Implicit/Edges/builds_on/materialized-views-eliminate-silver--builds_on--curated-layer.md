---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[materialized-views-eliminate-silver]]"
target_node: "[[curated-layer]]"
weight: 1
---

# Materialized Views Can Eliminate Silver Layer builds_on Curated Layer

<!-- Materialized views in Fabric can enforce data quality directly in the Curated layer, potentially eliminating a separate Silver layer. -->

## Edge

`[[materialized-views-eliminate-silver]]` -- **builds_on** -> `[[curated-layer]]`

## Evidence

Materialized views in Fabric can enforce data quality directly in the Curated layer, potentially eliminating a separate Silver layer.


## Related

- [[materialized-views-eliminate-silver]]
- [[curated-layer]]
