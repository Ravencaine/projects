---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[wrong-granularity-scd]]"
target_node: "[[scd-type-2]]"
weight: 1
---

# Wrong Granularity SCD Causes Full Fact Recalculation exemplifies SCD Type 2

<!-- The wrong granularity mistake is specific to SCD Type 2 where fact rows must join to a specific historical version, not the current dimension row. -->

## Edge

`[[wrong-granularity-scd]]` -- **exemplifies** -> `[[scd-type-2]]`

## Evidence

The wrong granularity mistake is specific to SCD Type 2 where fact rows must join to a specific historical version, not the current dimension row.


## Related

- [[wrong-granularity-scd]]
- [[scd-type-2]]
