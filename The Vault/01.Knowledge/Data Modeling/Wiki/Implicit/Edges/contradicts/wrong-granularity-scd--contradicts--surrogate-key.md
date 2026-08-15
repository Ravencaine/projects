---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[wrong-granularity-scd]]"
target_node: "[[surrogate-key]]"
weight: 1
---

# Wrong Granularity SCD Causes Full Fact Recalculation contradicts Surrogate Key

<!-- Wrong granularity SCD occurs when a fact table lacks a point-in-time surrogate key; the correct fix is assigning a surrogate key to every SCD version. -->

## Edge

`[[wrong-granularity-scd]]` -- **contradicts** -> `[[surrogate-key]]`

## Evidence

Wrong granularity SCD occurs when a fact table lacks a point-in-time surrogate key; the correct fix is assigning a surrogate key to every SCD version.


## Related

- [[wrong-granularity-scd]]
- [[surrogate-key]]
