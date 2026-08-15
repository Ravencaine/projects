---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, data-modeling, Data Modeling]
---

# Duplicated Dimensions Per Fact Table Anti-Pattern

<!-- Creating separate dimension tables for each fact table bloats model size, slows refresh, creates confusion for report authors, and breaks cross-fact reporting because there is no single shared dimension to slice by. -->

## Claim

Creating separate dimension tables for each fact table bloats model size, slows refresh, creates confusion for report authors, and breaks cross-fact reporting because there is no single shared dimension to slice by.
