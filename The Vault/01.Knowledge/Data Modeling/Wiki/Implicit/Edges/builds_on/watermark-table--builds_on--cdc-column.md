---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[watermark-table]]"
target_node: "[[cdc-column]]"
weight: 1
---

# Watermark Table builds_on CDC Column

<!-- A watermark table depends on a well-chosen CDC column to track progress across incremental loads. -->

## Edge

`[[watermark-table]]` -- **builds_on** -> `[[cdc-column]]`

## Evidence

A watermark table depends on a well-chosen CDC column to track progress across incremental loads.


## Related

- [[watermark-table]]
- [[cdc-column]]
