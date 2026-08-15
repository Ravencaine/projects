---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: contradicts
tags: [Data Modeling, implicit-edge, contradicts]
source_node: "[[etl-run-date]]"
target_node: "[[cdc-column]]"
weight: 1
---

# ETL Run Date contradicts CDC Column

<!-- ETL run date is identified as an anti-pattern for CDC: it has no business meaning and changes every load regardless of whether data changed. -->

## Edge

`[[etl-run-date]]` -- **contradicts** -> `[[cdc-column]]`

## Evidence

ETL run date is identified as an anti-pattern for CDC: it has no business meaning and changes every load regardless of whether data changed.


## Related

- [[etl-run-date]]
- [[cdc-column]]
