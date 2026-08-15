---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, debug, Data Modeling]
---

# Missing Prices Error Pattern

<!-- Symptom: variant row exists in dimension but RetailPrice equals 0 or NULL because no matching price record exists in PriceDiscTable. Common causes are item-level prices without variant-level matches, dimension group mismatches, expired prices, or wrong module values. -->

## Claim

Symptom: variant row exists in dimension but RetailPrice equals 0 or NULL because no matching price record exists in PriceDiscTable. Common causes are item-level prices without variant-level matches, dimension group mismatches, expired prices, or wrong module values.
