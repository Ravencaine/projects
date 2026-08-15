---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[data-modeling-mistake-missing-date-table]]"
target_node: "[[advanced-dimensional-modeling-retail-product-variants-source]]"
weight: 1
---

# Data Modeling Mistake: No Dedicated Date Table contradicts Advanced Dimensional Modeling for Retail Product Variants (Parts 1-3)

<!-- The Date Table pattern advocates a dedicated dimension joined via a single key; the retail product variants series shows that some D365 F&O dimensions require composite/CONCAT keys instead of single surrogate keys. -->

## Edge

`[[data-modeling-mistake-missing-date-table]]` -- **contradicts** -> `[[advanced-dimensional-modeling-retail-product-variants-source]]`

## Evidence

The Date Table pattern advocates a dedicated dimension joined via a single key; the retail product variants series shows that some D365 F&O dimensions require composite/CONCAT keys instead of single surrogate keys.


## Related

- [[data-modeling-mistake-missing-date-table]]
- [[advanced-dimensional-modeling-retail-product-variants-source]]
