---
created: 2026-08-15
source: implicit-extraction:Power BI
note_type: claim
tags: [claim, technique, Power BI]
---

# X-axis bounds must be wired to measures rather than set manually to maintain visual alignment

<!-- Setting axis bounds manually (e.g., fixed dates) breaks when data changes. Binding both stacked visuals to the same bound measures (Min Calendar Date, Max Project Date) ensures the two charts stay synchronized. -->

## Claim

Setting axis bounds manually (e.g., fixed dates) breaks when data changes. Binding both stacked visuals to the same bound measures (Min Calendar Date, Max Project Date) ensures the two charts stay synchronized.

## Evidence

- Stated in [[Chart-Alignment-Between-Stacked-Visuals-Gotcha]] — How to Handle It
