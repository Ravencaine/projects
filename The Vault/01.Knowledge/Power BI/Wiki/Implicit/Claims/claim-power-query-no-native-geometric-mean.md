---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, power-bi, Power BI]
---

# Power Query has no built-in geometric mean function

<!-- Power Query (M) does not include a native geometric mean function. It must be implemented in two steps: (1) compute the product of all values in a group using List.Product, then (2) raise to power 1/n using Number.Power. -->

## Claim

Power Query (M) does not include a native geometric mean function. It must be implemented in two steps: (1) compute the product of all values in a group using List.Product, then (2) raise to power 1/n using Number.Power.

## Evidence

- Stated in [[Geometric-Mean-Power-Query]] — Implementation Steps
