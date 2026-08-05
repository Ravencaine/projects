---
title: "Advanced Dimensional Modeling for Retail Product Variants"
source: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-b4e6c1743382"
author:
  - "[[Jesse Ruiz (she/they)]]"
published: 2026-04-27
created: 2026-07-27
description: "Part 1: Product Dimensions and the Variant Complexity Problem"
Processed: "Unprocessed"
---
## Part 1: Product Dimensions and the Variant Complexity Problem

A conversational technical guide to building production-grade retail product dimensions

![](99.System/Attachments/0!6nT4Pi8gtIbkurOL.webp)

Photo by Nathália Rosa on Unsplash

## The Problem: Product Data That Doesn’t Fit in a Single Table

If you’ve ever tried to build a product dimension for a retail organization using D365 F&O data, you’ve probably discovered something uncomfortable: there’s no “Products” table you can just SELECT \* FROM.

Instead, you find yourself staring at 12+ interconnected tables, trying to figure out how a single item called “Graphic T-Shirt” turns into 48 different SKUs when you consider all the color/style/size combinations.

Here’s what a typical product analyst request looks like:

“Can you give me a list of all products with their cost and retail price?”

Sounds simple. Then you discover:

\- The product name is in EcoResProductTranslation

\- The item ID is in InventTable

\- But variant combinations (Red/Large/Classic) are in InventDimCombination

\- Each variant’s dimensional attributes are in InventDim

\- Pricing is in PriceDiscTable, but you need to filter by module (1=Sales, 2=Purchase)

\- Oh, and different products use different combinations of Color/Style/Size/Config

## The Business Context: Why Product Variants Exist

Retail product hierarchies in D365 F&O are non-trivial because the real world is non-trivial:

Simple products: Single SKU with no variants (e.g., “Desk Lamp”, “Gift Card”)

Variant products: Master product with multiple configurations:

\- Color: Red, Blue, Green

\- Style: Classic, Modern, Vintage

\- Size: S, M, L, XL

\- Config: Bundle configurations

A single product dimension must unify both types, resolve pricing per variant, handle barcodes, and maintain referential integrity across 10+ D365 tables.

## The Dimension Group Challenge

Here’s where it gets interesting. Different products use different combinations of variant attributes, defined by their dimension group:

| Dimension Group | Variant Attributes |

| — — — — — — — — -| — — — — — — — — — -|

| Group 1| Color + Style + Size |

| GroupNS | Color + Style |

| GroupS | Style only |

| Retail Kit | Config only |

When you join to pricing tables, you must match on exactly the right combination of attributes. Join on too many, you miss prices. Join on too few, you get duplicate matches.

The join logic must be dynamic based on dimension group.

## The D365 Product Data Model

Before we look at code, let’s understand the table relationships:

\`\`\`

EcoResProduct (Master Product)

├─> EcoResProductTranslation (Product Name)

├─> EcoResProductDimensionGroup (Dimension Group: “Donated”, “DonatedNS”, etc.)

└─> InventDimCombination (Variant Combinations)

├─> InventDim (Actual Color/Style/Size/Config values)

├─> PriceDiscTable (Pricing by variant or simple product)

└─> InventItemBarcode (Barcodes per variant)

\`\`\`

### Key Tables:

InventDimCombination: All valid product × variant combinations

InventDim: Dimensional attributes (color, style, size, config)

EcoResProductDimensionGroup: Defines which dimensions apply to a product

PriceDiscTable: Pricing (module 1=Sales, module 2=Purchase)

InventItemBarcode: Barcode assignments per variant

— -

### Source Code Context

[The code](https://github.com/jessejinnaruiz/comp_source_code_examples/blob/main/sqlqueries_optimized_Retail_New_DeltaLake.sql) in this lesson comes from a production product dimension view:

\`\`\`

codebase\_copy/sqlqueries\_optimized\_Retail\_New\_DeltaLake.sql

Lines 4–222: DIM\_AllItems view

\`\`\`

This view handles 70,000+ products across simple products, variant products, and four different dimension group types.

### The Core Challenge: Simple vs. Variant Products

The fundamental tension in product dimension design is that you need one unified dimension that handles both:

### Simple products: One row per item, pricing at item level

\`\`\`

ItemKey ItemName RetailPrice

USMF\_LAMP001 Desk Lamp 19.99

USMF\_GC100 Gift Card 0

\`\`\`

### Variant products: One row per variant combination, pricing at variant level

\`\`\`

ItemKey ItemName Color Size RetailPrice

USMF\_TSHIRT001\_RED\_S Graphic Tee Red S 19.99

USMF\_TSHIRT001\_RED\_M Graphic Tee Red M 19.99

USMF\_TSHIRT001\_BLUE\_L Graphic Tee Blue L 22.99

\`\`\`

The ItemKey must be unique across both types. Simple products get a key like \`USMF\_LAMP001\`. Variant products get a composite key like \`USMF\_TSHIRT001\_RED\_CLASSIC\_M\`.

## The Composite Key Strategy

The key design is critical. Here’s the pattern:

```sh
- Variant product key (includes all dimensions)
CONCAT(dataareaid, '_', itemid, color, style, size, config)
 - Example: "USMF_T00123_RED_CLASSIC_M_"
 - Simple product key (no variants)
CONCAT(dataareaid, '_', itemid)
 - Example: "USMF_D00456"
```

Why this works:

1\. Unique across all products (simple + variants)

2\. Fact tables can join on ItemKey without knowing if product has variants

3\. Empty strings for unused variant attributes maintain pattern consistency

## What’s Coming in Part 2

In Part 2, we’ll dive into the actual SQL code and explore:

\- CTE patterns for purchase and sales pricing

\- Conditional joins based on dimension group

\- ROW\_NUMBER for price deduplication

\- The UNION ALL pattern for combining simple and variant products

Continue to [Part 2: Conditional Joins and Price Resolution](https://medium.com/@jjr8888/efd14c680c3c)

## Summary

In this introduction to retail dimensional modeling, we covered:

✅ Why product data is complex: 12+ tables, variant combinations, dimension groups

✅ Business context: Simple products vs. variant products with Color/Style/Size/Config

✅ The dimension group problem: Different products use different variant attributes

✅ D365 table relationships: EcoResProduct → InventDimCombination → InventDim → PriceDiscTable

✅ Composite key strategy: Unified key pattern for simple and variant products

The product dimension is often the most complex dimension in a retail star schema. Understanding the data model is essential before writing any code.

## Additional Resources

\- Full view SQL: [sqlqueries\_optimized\_Retail\_New\_DeltaLake.sql](https://github.com/jessejinnaruiz/comp_source_code_examples/blob/main/sqlqueries_optimized_Retail_New_DeltaLake.sql)

\- D365 F&O product dimensions: [https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-dimensions](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-dimensions)

\- Kimball dimensional modeling techniques: [https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)

\- EcoResProduct table reference: [https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/entity-ecoresproduct](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/entity-ecoresproduct)