---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[bridge-table]]"
target_node: "[[star-schema]]"
weight: 1
---

# Bridge Table builds_on Star Schema

<!-- Bridge tables extend star schema to handle many-to-many relationships while preserving the one-to-many relationship structure required for efficient COUNTX. -->

## Edge

`[[bridge-table]]` -- **builds_on** -> `[[star-schema]]`

## Evidence

Bridge tables extend star schema to handle many-to-many relationships while preserving the one-to-many relationship structure required for efficient COUNTX.


## Related

- [[bridge-table]]
- [[star-schema]]
