---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[snowflake-slower-4x]]"
target_node: "[[snowflake-schema]]"
weight: 1
---

# Snowflake Schema is ~4x Slower Than Star Schema exemplifies Snowflake Schema

<!-- Snowflake Schema with 4-hop join chains (Region to Manager to Director) produces approximately 4x slower query performance than Star Schema's single hop. -->

## Edge

`[[snowflake-slower-4x]]` -- **exemplifies** -> `[[snowflake-schema]]`

## Evidence

Snowflake Schema with 4-hop join chains (Region to Manager to Director) produces approximately 4x slower query performance than Star Schema's single hop.


## Related

- [[snowflake-slower-4x]]
- [[snowflake-schema]]
