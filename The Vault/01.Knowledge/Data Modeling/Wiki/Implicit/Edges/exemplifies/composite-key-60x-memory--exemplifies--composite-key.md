---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[composite-key-60x-memory]]"
target_node: "[[composite-key]]"
weight: 1
---

# Composite Keys Consume ~60x More Memory Than Surrogate Keys exemplifies Composite Key

<!-- A 6-column NVARCHAR composite key at 20 characters per column consumes ~240 bytes per row vs 4 bytes for an integer surrogate key. -->

## Edge

`[[composite-key-60x-memory]]` -- **exemplifies** -> `[[composite-key]]`

## Evidence

A 6-column NVARCHAR composite key at 20 characters per column consumes ~240 bytes per row vs 4 bytes for an integer surrogate key.


## Related

- [[composite-key-60x-memory]]
- [[composite-key]]
