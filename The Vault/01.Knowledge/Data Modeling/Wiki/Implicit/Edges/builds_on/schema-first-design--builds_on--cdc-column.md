---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[schema-first-design]]"
target_node: "[[cdc-column]]"
weight: 1
---

# Schema-First Design builds_on CDC Column

<!-- Schema-first design requires knowing the source table behavior (insert-only vs upsert) to select the correct CDC column. -->

## Edge

`[[schema-first-design]]` -- **builds_on** -> `[[cdc-column]]`

## Evidence

Schema-first design requires knowing the source table behavior (insert-only vs upsert) to select the correct CDC column.


## Related

- [[schema-first-design]]
- [[cdc-column]]
