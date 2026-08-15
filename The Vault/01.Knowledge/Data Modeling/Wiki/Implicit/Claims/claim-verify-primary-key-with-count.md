---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, verification, Data Modeling]
---

# Always verify primary key with COUNT(*) = COUNT(DISTINCT)

<!-- Source systems frequently misidentify primary keys. The only reliable verification is comparing total row count against distinct count of the candidate column. -->

## Claim

Source systems frequently misidentify primary keys. The only reliable verification is comparing total row count against distinct count of the candidate column.
