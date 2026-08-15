---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[unified-product-dimension]]"
target_node: "[[composite-key]]"
weight: 1
---

# Unified Product Dimension builds_on Composite Key

<!-- The unified product dimension uses a composite ItemKey (CONCAT of dataareaid and itemid) to identify simple products, generated identically on both UNION ALL branches. -->

## Edge

`[[unified-product-dimension]]` -- **builds_on** -> `[[composite-key]]`

## Evidence

The unified product dimension uses a composite ItemKey (CONCAT of dataareaid and itemid) to identify simple products, generated identically on both UNION ALL branches.


## Related

- [[unified-product-dimension]]
- [[composite-key]]
