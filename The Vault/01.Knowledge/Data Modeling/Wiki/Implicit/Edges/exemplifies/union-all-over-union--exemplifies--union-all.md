---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: exemplifies
tags: [Data Modeling, implicit-edge, exemplifies]
source_node: "[[union-all-over-union]]"
target_node: "[[union-all]]"
weight: 1
---

# UNION ALL is Faster Than UNION for ETL exemplifies UNION ALL

<!-- UNION ALL is faster than UNION in ETL because the ETL logic already guarantees no overlap between variant and simple product branches. -->

## Edge

`[[union-all-over-union]]` -- **exemplifies** -> `[[union-all]]`

## Evidence

UNION ALL is faster than UNION in ETL because the ETL logic already guarantees no overlap between variant and simple product branches.


## Related

- [[union-all-over-union]]
- [[union-all]]
