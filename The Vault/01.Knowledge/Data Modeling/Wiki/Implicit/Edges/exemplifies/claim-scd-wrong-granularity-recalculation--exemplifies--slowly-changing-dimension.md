---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[claim-scd-wrong-granularity-recalculation]]"
target_node: "[[slowly-changing-dimension]]"
weight: 1
---

# SCD at Wrong Granularity Causes Full In-Memory Recalculation exemplifies Slowly Changing Dimension (SCD)

<!-- SCDs exemplify the performance risk when dimension tables are joined at wrong granularity, causing full in-memory recalculation. -->

## Edge

`[[claim-scd-wrong-granularity-recalculation]]` -- **exemplifies** -> `[[slowly-changing-dimension]]`

## Evidence

SCDs exemplify the performance risk when dimension tables are joined at wrong granularity, causing full in-memory recalculation.


## Related

- [[claim-scd-wrong-granularity-recalculation]]
- [[slowly-changing-dimension]]
