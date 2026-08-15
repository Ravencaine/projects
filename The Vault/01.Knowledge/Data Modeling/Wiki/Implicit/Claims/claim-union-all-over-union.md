---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, etl, Data Modeling]
---

# UNION ALL is Faster Than UNION for ETL

<!-- UNION ALL combines result sets without deduplication sorting, making it significantly faster than UNION which removes duplicates. When ETL logic already guarantees no overlap, UNION ALL is always the correct choice. -->

## Claim

UNION ALL combines result sets without deduplication sorting, making it significantly faster than UNION which removes duplicates. When ETL logic already guarantees no overlap, UNION ALL is always the correct choice.
