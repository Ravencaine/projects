---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, data-quality, Data Modeling]
---

# COUNTROWS vs DISTINCTCOUNT Reveals Duplicates

<!-- If COUNTROWS exceeds DISTINCTCOUNT of a key column, duplicate records exist in the table; this DAX-based QA measure is a reliable pre-publish duplicate detection technique. -->

## Claim

If COUNTROWS exceeds DISTINCTCOUNT of a key column, duplicate records exist in the table; this DAX-based QA measure is a reliable pre-publish duplicate detection technique.
