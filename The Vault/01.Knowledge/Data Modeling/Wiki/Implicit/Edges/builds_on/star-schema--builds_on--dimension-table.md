---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[star-schema]]"
target_node: "[[dimension-table]]"
weight: 1
---

# Star Schema builds_on Dimension Table

<!-- Star Schema uses flat dimension tables with all attributes at the same level, rather than normalised sub-tables as in Snowflake Schema. -->

## Edge

`[[star-schema]]` -- **builds_on** -> `[[dimension-table]]`

## Evidence

Star Schema uses flat dimension tables with all attributes at the same level, rather than normalised sub-tables as in Snowflake Schema.


## Related

- [[star-schema]]
- [[dimension-table]]
