---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[snowflake-schema]]"
target_node: "[[star-schema]]"
weight: 1
---

# Snowflake Schema contradicts Star Schema

<!-- Snowflake Schema uses normalised multi-hop joins whereas Star Schema uses single-hop joins, making Snowflake approximately 4x slower for Power BI queries. -->

## Edge

`[[snowflake-schema]]` -- **contradicts** -> `[[star-schema]]`

## Evidence

Snowflake Schema uses normalised multi-hop joins whereas Star Schema uses single-hop joins, making Snowflake approximately 4x slower for Power BI queries.


## Related

- [[snowflake-schema]]
- [[star-schema]]
