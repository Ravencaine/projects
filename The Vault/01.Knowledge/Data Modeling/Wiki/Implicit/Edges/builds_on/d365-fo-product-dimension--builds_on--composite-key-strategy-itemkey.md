---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[d365-fo-product-dimension]]"
target_node: "[[composite-key-strategy-itemkey]]"
weight: 1
---

# D365 F&O Product Dimension Complexity builds_on Composite Key Strategy (CONCAT-based ItemKey)

<!-- The composite CONCAT-based ItemKey strategy is the design response to D365 F&O's lack of a unified product table and the need to unify simple and variant products. -->

## Edge

`[[d365-fo-product-dimension]]` -- **builds_on** -> `[[composite-key-strategy-itemkey]]`

## Evidence

The composite CONCAT-based ItemKey strategy is the design response to D365 F&O's lack of a unified product table and the need to unify simple and variant products.


## Related

- [[d365-fo-product-dimension]]
- [[composite-key-strategy-itemkey]]
