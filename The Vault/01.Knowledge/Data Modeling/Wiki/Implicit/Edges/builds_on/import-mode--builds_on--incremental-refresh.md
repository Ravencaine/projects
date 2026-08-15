---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[import-mode]]"
target_node: "[[incremental-refresh]]"
weight: 1
---

# Import Mode builds_on Incremental Refresh

<!-- Import mode is required for incremental refresh, which partitions tables to reduce refresh scope. -->

## Edge

`[[import-mode]]` -- **builds_on** -> `[[incremental-refresh]]`

## Evidence

Import mode is required for incremental refresh, which partitions tables to reduce refresh scope.


## Related

- [[import-mode]]
- [[incremental-refresh]]
