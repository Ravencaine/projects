---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[data-lake]]"
target_node: "[[data-warehouse]]"
weight: 1
---

# Data Lake builds_on Data Warehouse

<!-- Modern architectures feed raw data into a data lake first, then transform and curate business-level datasets into a data warehouse for fast analytical queries. -->

## Edge

`[[data-lake]]` -- **builds_on** -> `[[data-warehouse]]`

## Evidence

Modern architectures feed raw data into a data lake first, then transform and curate business-level datasets into a data warehouse for fast analytical queries.


## Related

- [[data-lake]]
- [[data-warehouse]]
