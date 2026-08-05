---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Dimensional Modeling for Retail Product Variants"
source_url: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382"
note_type: atomic
tags: [d365, retail, product-dimension, variants]
---

# The Variant Complexity Problem (D365 F&O)

The challenge of building a unified product dimension when a single master product spawns dozens of SKUs across colour, style, size, and configuration combinations — each with its own pricing and barcode.

## Definition

D365 F&O has no single `Products` table. Product data spans 12+ interconnected tables (EcoResProduct, EcoResProductTranslation, InventDimCombination, InventDim, PriceDiscTable, InventItemBarcode, etc.). A single item like "Graphic T-Shirt" can generate 48 SKUs across 3 colours × 4 styles × 4 sizes. Pricing lives at variant level, not product level. Building a usable product dimension requires reconciling all of this.

## Key Points

- Product name → EcoResProductTranslation
- Item ID → InventTable
- Variant combinations (Red/Large/Classic) → InventDimCombination
- Dimensional attributes per variant → InventDim
- Pricing per variant → PriceDiscTable (filtered by module: 1=Sales, 2=Purchase)
- Barcodes per variant → InventItemBarcode
- Which variant attributes apply → EcoResProductDimensionGroup (defines the dimension group per product)

The join logic must be **dynamic based on dimension group**: join on too many attributes and prices are missed; join on too few and duplicates appear.

## Examples

A business analyst asks: "Give me a list of all products with cost and retail price."

The reality:
- The product name is in EcoResProductTranslation
- The item ID is in InventTable
- But variant combinations are in InventDimCombination
- Each variant's dimensional attributes are in InventDim
- Pricing is in PriceDiscTable, filtered by module

## Related

- [[simple-vs-variant-products]] — the two product types this problem spans
- [[composite-key-strategy-itemkey]] — the solution to unified fact-dimension joins
