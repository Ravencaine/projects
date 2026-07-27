---
created: 2026-07-27
source: "Advanced Dimensional Modeling for Retail Product Variants"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382"
note_type: atomic
tags: [product-dimension, simple-product, variant-product, sku]
---

# Simple vs Variant Products

The two fundamental product types in a retail dimension — each requiring different join and pricing logic.

## Definition

A **simple product** has a single SKU with no variant attributes (e.g., "Desk Lamp", "Gift Card"). Pricing lives at the item level. A **variant product** has a master product with multiple configurations across Colour, Style, Size, and/or Config — each combination is a distinct SKU with its own pricing and barcode.

## Key Points

**Simple products:**
- One row in InventTable; no entries in InventDimCombination
- Pricing resolved by joining directly on itemid + dataareaid
- ItemKey: `CONCAT(dataareaid, '_', itemid)` → e.g., `USMF_LAMP001`

**Variant products:**
- One row in InventDimCombination per valid combination
- Each variant has its own pricing in PriceDiscTable (variant-level pricing)
- ItemKey: `CONCAT(dataareaid, '_', itemid, color, style, size, config)` → e.g., `USMF_T00123_RED_CLASSIC_M_`

**The fundamental tension:**
A product dimension must handle **both types** with one unified key. Fact tables then join on ItemKey without needing to know whether the product has variants.

## Examples

| Type | ItemKey | Colour | Style | Size | RetailPrice |
|------|---------|--------|-------|------|-------------|
| Simple | USMF_D00456 | — | — | — | 19.99 |
| Variant | USMF_T00123_RED_CLASSIC_M_ | Red | Classic | M | 19.99 |
| Variant | USMF_T00123_BLUE_MODERN_L_ | Blue | Modern | L | 22.99 |

## Related

- [[composite-key-strategy-itemkey]] — the key pattern that unifies both types
- [[variant-complexity-problem-d365-fo]] — why this distinction matters in D365 F&O
