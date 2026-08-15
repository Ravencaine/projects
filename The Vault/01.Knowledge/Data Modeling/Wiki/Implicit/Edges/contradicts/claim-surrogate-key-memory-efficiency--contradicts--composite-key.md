---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[claim-surrogate-key-memory-efficiency]]"
target_node: "[[composite-key]]"
weight: 1
---

# Surrogate Keys Outperform Composite Keys at Scale contradicts Composite Key

<!-- The memory efficiency claim contradicts composite key design, which consumes multi-bytes-per-character versus 4 bytes for an integer surrogate key. -->

## Edge

`[[claim-surrogate-key-memory-efficiency]]` -- **contradicts** -> `[[composite-key]]`

## Evidence

The memory efficiency claim contradicts composite key design, which consumes multi-bytes-per-character versus 4 bytes for an integer surrogate key.


## Related

- [[claim-surrogate-key-memory-efficiency]]
- [[composite-key]]
