---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: relationship
edge_type: builds_on
tags: [Data Modeling, implicit-edge, builds_on]
source_node: "[[excel-to-postgres-migration]]"
target_node: "[[postgres-constraints]]"
weight: 1
---

# Excel to Postgres Migration Workflow builds_on Postgres Constraints

<!-- The migration workflow uses Postgres constraints in Step 4 to catch bad data after cleaning in Step 3. -->

## Edge

`[[excel-to-postgres-migration]]` -- **builds_on** -> `[[postgres-constraints]]`

## Evidence

The migration workflow uses Postgres constraints in Step 4 to catch bad data after cleaning in Step 3.


## Related

- [[excel-to-postgres-migration]]
- [[postgres-constraints]]
