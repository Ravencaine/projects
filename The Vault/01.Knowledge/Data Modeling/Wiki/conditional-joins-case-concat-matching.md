---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants Pt 2"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-2-efd14c680c3c"
note_type: pattern
tags: [conditional-join, case-expression, concat, dimension-group, d365, pricing]
---

# Conditional Joins via CASE/CONCAT Matching

A SQL join pattern that applies different matching column sets to different rows based on a dimension group value — the heart of resolving variant-level pricing correctly.

## Purpose

Standard SQL JOIN conditions are fixed at query compile time. But in D365 F&O, the required match columns vary by dimension group (Colour+Style+Size, Colour+Style only, Style only, Config only). The CASE/CONCAT pattern works around SQL's lack of dynamic column lists by concatenating the required columns into a single string comparison on both sides of the join.

## Components

- `ecoresproductdimensiongroup` — contains `prodgroup.name` (e.g., 'Donated', 'DonatedNS', 'DonatedS', 'Retail Kit')
- `CONCAT(...)` — builds the match key on both sides of the join
- `CASE WHEN ... THEN ... END` — selects the correct CONCAT expression per dimension group
- LEFT JOIN — price is optional; null prices are acceptable

## Structure

```sql
LEFT JOIN pricediscpurch ON (
  CASE
    WHEN prodgroup.name IN ('DonatedNS') THEN
      CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
             pricediscpurch.inventstyleid, pricediscpurch.inventcolorid)
    WHEN prodgroup.name IN ('Donated') THEN
      CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
             pricediscpurch.inventcolorid, pricediscpurch.inventstyleid,
             pricediscpurch.inventsizeid)
    WHEN prodgroup.name IN ('DonatedS') THEN
      CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
             pricediscpurch.inventstyleid)
    WHEN prodgroup.name IN ('Retail Kit') THEN
      CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
             pricediscpurch.configid)
  END
) = (
  CASE
    WHEN prodgroup.name IN ('DonatedNS') THEN
      CONCAT(idc.dataareaid, idc.itemid, id.inventstyleid, id.inventcolorid)
    WHEN prodgroup.name IN ('Donated') THEN
      CONCAT(idc.dataareaid, idc.itemid, id.inventcolorid,
             id.inventstyleid, id.inventsizeid)
    WHEN prodgroup.name IN ('DonatedS') THEN
      CONCAT(idc.dataareaid, idc.itemid, id.inventcolorid, id.inventstyleid)
    WHEN prodgroup.name IN ('Retail Kit') THEN
      CONCAT(idc.dataareaid, idc.itemid, id.configid)
  END
)
```

The same CASE/CONCAT pattern is duplicated for both the purchase price join and the sales price join.

## Why CONCAT-Based Matching?

1. SQL does not allow dynamic column lists in JOIN conditions
2. CASE expressions return a single scalar value — suitable for comparison
3. CONCAT handles NULLs gracefully (returns empty string; no NULL propagation in comparisons)
4. String comparison is deterministic across all SQL engines

## Related

- [[dimension-groups-color-style-size-config]] — the dimension groups that drive this logic
- [[pricing-cte-with-row-number-deduplication]] — the CTE that feeds deduplicated prices into this join
