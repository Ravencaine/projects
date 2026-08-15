---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[scd-type-1]]"
target_node: "[[role-playing-dimension]]"
weight: 1
---

# SCD Type 1 (Overwrite) exemplifies Role-Playing Dimension

<!-- Role-playing dimensions (OrderDate, ShipDate, DueDate all pointing to the same Date dimension) are a separate pattern from SCD; both can coexist in the same model. -->

## Edge

`[[scd-type-1]]` -- **exemplifies** -> `[[role-playing-dimension]]`

## Evidence

Role-playing dimensions (OrderDate, ShipDate, DueDate all pointing to the same Date dimension) are a separate pattern from SCD; both can coexist in the same model.


## Related

- [[scd-type-1]]
- [[role-playing-dimension]]
