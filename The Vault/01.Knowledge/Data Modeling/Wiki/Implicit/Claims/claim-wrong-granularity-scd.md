---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, power-bi, Data Modeling]
---

# Wrong Granularity SCD Causes Full Fact Recalculation

<!-- Joining a fact table to a slowly changing dimension at the wrong granularity forces Power BI to recalculate the entire fact table in memory on every query, because no surrogate key on the fact points to the correct SCD version. -->

## Claim

Joining a fact table to a slowly changing dimension at the wrong granularity forces Power BI to recalculate the entire fact table in memory on every query, because no surrogate key on the fact points to the correct SCD version.
