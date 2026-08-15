---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[snowflake-schema]]"
target_node: "[[dimension-table]]"
weight: 1
---

# Snowflake Schema builds_on Dimension Table

<!-- Snowflake Schema normalises dimension tables into hierarchies (Region, Manager, Director) stored as separate related tables, increasing join depth. -->

## Edge

`[[snowflake-schema]]` -- **builds_on** -> `[[dimension-table]]`

## Evidence

Snowflake Schema normalises dimension tables into hierarchies (Region, Manager, Director) stored as separate related tables, increasing join depth.


## Related

- [[snowflake-schema]]
- [[dimension-table]]
