---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[surrogate-key]]"
target_node: "[[composite-key]]"
weight: 1
---

# Surrogate Key builds_on Composite Key

<!-- The surrogate key is assigned at ETL time to replace the original composite business key used for source system joins. -->

## Edge

`[[surrogate-key]]` -- **builds_on** -> `[[composite-key]]`

## Evidence

The surrogate key is assigned at ETL time to replace the original composite business key used for source system joins.


## Related

- [[surrogate-key]]
- [[composite-key]]
