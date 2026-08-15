---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, type-1, Data Modeling]
---

# SCD Type 1 Overwrites Price Without Preserving History

<!-- In SCD Type 1, when RetailPrice changes the value is overwritten in place. Historical prices are not preserved in the dimension; pricing history lives in the source transaction table or PriceDiscTable. -->

## Claim

In SCD Type 1, when RetailPrice changes the value is overwritten in place. Historical prices are not preserved in the dimension; pricing history lives in the source transaction table or PriceDiscTable.
