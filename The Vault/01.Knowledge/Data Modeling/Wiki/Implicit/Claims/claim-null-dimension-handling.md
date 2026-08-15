---
created: 2026-08-15
source: implicit-extraction:Data Modeling
note_type: claim
tags: [claim, sql, Data Modeling]
---

# ISNULL Converts NULL Dimensions to Empty Strings

<!-- PriceDiscTable may have NULL inventdimid for item-level (non-variant) prices; LEFT JOIN with ISNULL prevents NULL propagation and keeps CONCAT keys consistent. -->

## Claim

PriceDiscTable may have NULL inventdimid for item-level (non-variant) prices; LEFT JOIN with ISNULL prevents NULL propagation and keeps CONCAT keys consistent.
