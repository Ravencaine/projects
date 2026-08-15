---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[list-columns-not-index-parallel]]"
target_node: "[[bridge-table]]"
weight: 1
---

# List Columns in Same Row Are Not Index-Parallel exemplifies Bridge Table

<!-- Real-world data shows comma-separated list columns in the same row are often independent, not index-aligned, making bridge tables necessary to avoid silent errors. -->

## Edge

`[[list-columns-not-index-parallel]]` -- **exemplifies** -> `[[bridge-table]]`

## Evidence

Real-world data shows comma-separated list columns in the same row are often independent, not index-aligned, making bridge tables necessary to avoid silent errors.


## Related

- [[list-columns-not-index-parallel]]
- [[bridge-table]]
