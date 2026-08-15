---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[scd-type1-overwrites-price]]"
target_node: "[[scd-type-1]]"
weight: 1
---

# SCD Type 1 Overwrites Price Without Preserving History exemplifies SCD Type 1 (Overwrite)

<!-- In SCD Type 1, when RetailPrice changes the value is overwritten in place with no historical row added; pricing history is stored separately in PriceDiscTable. -->

## Edge

`[[scd-type1-overwrites-price]]` -- **exemplifies** -> `[[scd-type-1]]`

## Evidence

In SCD Type 1, when RetailPrice changes the value is overwritten in place with no historical row added; pricing history is stored separately in PriceDiscTable.


## Related

- [[scd-type1-overwrites-price]]
- [[scd-type-1]]
