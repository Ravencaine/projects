---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[star-schema]]"
target_node: "[[direct-lake-mode]]"
weight: 1
---

# Star Schema builds_on Direct Lake Mode

<!-- Power BI connects to the Fabric Gold layer star schema via Direct Lake mode, reading fact and dimension tables from OneLake. -->

## Edge

`[[star-schema]]` -- **builds_on** -> `[[direct-lake-mode]]`

## Evidence

Power BI connects to the Fabric Gold layer star schema via Direct Lake mode, reading fact and dimension tables from OneLake.


## Related

- [[star-schema]]
- [[direct-lake-mode]]
