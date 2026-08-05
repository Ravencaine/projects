---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382"
note_type: atomic
tags: [dimension-group, d365, product-dimension, color, style, size, config]
---

# Dimension Groups (Color / Style / Size / Config)

The D365 F&O concept that defines which variant attributes apply to a product — determining the exact set of columns that must be matched when joining to pricing.

## Definition

A **dimension group** is a D365 F&O concept that defines which variant dimensions (Colour, Style, Size, Config) apply to a given product. Products in different dimension groups require different join conditions to PriceDiscTable. EcoResProductDimensionGroup stores the mapping; prodgroup.name contains the group name (e.g., 'Donated', 'DonatedNS', 'DonatedS', 'Retail Kit').

## Key Points

| Dimension Group | Variant Attributes Required | Match Columns |
|----------------|---------------------------|---------------|
| Donated | Colour + Style + Size | all three |
| DonatedNS | Colour + Style | colour + style only |
| DonatedS | Style only | style only |
| Retail Kit | Config only | config only |

When joining to pricing, the condition must match **exactly the attributes defined by the product's dimension group**. Mismatching the attribute set (e.g., joining on all four when only Style applies) causes prices to be missed or duplicates to appear.

The join logic must be **conditional based on dimgroup.name**: typically via CASE expressions in the join predicate.

## Examples

A product in `DonatedNS` group:
```
Price match key = CONCAT(dataareaid, itemid, inventstyleid, inventcolorid)
-- Size and Config are NULL/empty for this group; do NOT include them
```

A product in `Retail Kit` group:
```
Price match key = CONCAT(dataareaid, itemid, configid)
-- Colour, Style, Size are NULL/empty; match on configid only
```

## Related

- [[conditional-joins-case-concat-matching]] — the SQL pattern for handling dynamic dimension groups
- [[variant-complexity-problem-d365-fo]] — the problem this creates
