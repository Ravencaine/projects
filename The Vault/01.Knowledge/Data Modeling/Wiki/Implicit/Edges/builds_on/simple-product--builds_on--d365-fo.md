---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[simple-product]]"
target_node: "[[d365-fo]]"
weight: 1
---

# Simple Product builds_on D365 F&O (Dynamics 365 Finance & Operations)

<!-- Simple product data in D365 F&O lives in InventTable while variant product data lives in InventDimCombination, requiring reconciliation to build a unified dimension. -->

## Edge

`[[simple-product]]` -- **builds_on** -> `[[d365-fo]]`

## Evidence

Simple product data in D365 F&O lives in InventTable while variant product data lives in InventDimCombination, requiring reconciliation to build a unified dimension.


## Related

- [[simple-product]]
- [[d365-fo]]
