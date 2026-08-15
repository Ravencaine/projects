---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, performance, Data Modeling]
---

# Column clustering reduces I/O by ~40%

<!-- Pre-sorting fact table rows by frequently filtered columns (customer_id, transaction_id) reduces disk I/O by approximately 40% on range queries. -->

## Claim

Pre-sorting fact table rows by frequently filtered columns (customer_id, transaction_id) reduces disk I/O by approximately 40% on range queries.
