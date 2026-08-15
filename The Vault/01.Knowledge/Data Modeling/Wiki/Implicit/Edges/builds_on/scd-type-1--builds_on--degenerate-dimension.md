---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[scd-type-1]]"
target_node: "[[degenerate-dimension]]"
weight: 1
---

# SCD Type 1 (Overwrite) builds_on Degenerate Dimension

<!-- In D365 F&O, RetailPrice is a Type 1 SCD attribute stored in the product dimension; pricing history lives in PriceDiscTable as a separate fact-like structure, not in the dimension itself. -->

## Edge

`[[scd-type-1]]` -- **builds_on** -> `[[degenerate-dimension]]`

## Evidence

In D365 F&O, RetailPrice is a Type 1 SCD attribute stored in the product dimension; pricing history lives in PriceDiscTable as a separate fact-like structure, not in the dimension itself.


## Related

- [[scd-type-1]]
- [[degenerate-dimension]]
