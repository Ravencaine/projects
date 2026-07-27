---
title: "Advanced Dimensional Modeling for Retail Product Variants Pt 2"
source: "https://medium.com/@jjr8888/advanced-dimensional-modeling-for-retail-product-variants-pt-2-efd14c680c3c"
author:
  - "[[Jesse Ruiz (she/they)]]"
published: 2026-05-11
created: 2026-07-27
description: "Part 2: Conditional Joins and Price Resolution"
Processed: "Unprocessed"
---
## Part 2: Conditional Joins and Price Resolution

A conversational technical guide to building dynamic join logic for variant products

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*0SewuhFRwLKJ92F3)

Photo by nrd on Unsplash

## The Problem: Join Conditions That Change Based on Data

In Part 1, we established that different products use different variant dimensions based on their dimension group:

| Dimension Group | Required Match Columns |

| — — — — — — — — -| — — — — — — — — — — — |

| Group 1| Color + Style + Size |

| GroupNS | Color + Style |

| GroupS | Style only |

| Retail Kit | Config only |

Now we need to write SQL that handles this. You can’t just write a standard LEFT JOIN because the join condition changes based on the product.

This is where conditional joins come in.

## Source Code Context

Code can be found [here](https://github.com/jessejinnaruiz/comp_source_code_examples/blob/main/sqlqueries_optimized_Retail_New_DeltaLake.sql).

\`\`\`

codebase\_copy/sqlqueries\_optimized\_Retail\_New\_DeltaLake.sql

Lines 4–222: DIM\_AllItems view

\`\`\`

## Code Block 7A: Pricing CTEs with ROW\_NUMBER

Before we can join to prices, we need to prepare the pricing data. The PriceDiscTable can have multiple price records per item (price history, overlapping agreements). We need to pick one.

```sh
- =====================================================
 - CTE 1: PURCHASE PRICING (Cost)
 - Purpose: Get one active cost per item/variant
 - =====================================================
WITH pricediscpurch AS (
SELECT
pricediscpurch.*,
 - ROW_NUMBER: Handle multiple price records per item
ROW_NUMBER() OVER (
PARTITION BY CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation)
ORDER BY pricediscpurch.fromdate
) AS seqnum,
 - Extract variant dimensions from price table
ISNULL(id.inventcolorid, '') AS inventcolorid,
ISNULL(id.inventstyleid, '') AS inventstyleid,
ISNULL(id.inventsizeid, '') AS inventsizeid,
ISNULL(id.configid, '') AS configid
FROM [dataverse_company_prod…].[dbo].pricedisctable pricediscpurch
LEFT JOIN [dataverse_company_prod…].[dbo].inventdim id
ON id.inventdimid = pricediscpurch.inventdimid
AND id.dataareaid = pricediscpurch.dataareaid
WHERE
module = 2 - Purchase prices (cost)
AND (todate = '1900–01–01' OR todate > GETDATE()) - Active prices only
AND fromdate <= GETDATE()
),
 - =====================================================
 - CTE 2: SALES PRICING (Retail Price)
 - Same pattern as purchase, module = 1
 - =====================================================
PriceDiscSales AS (
SELECT
PriceDiscSales.*,
ROW_NUMBER() OVER (
PARTITION BY CONCAT(PriceDiscSales.dataareaid, PriceDiscSales.itemrelation)
ORDER BY PriceDiscSales.fromdate
) AS seqnum,
ISNULL(id.inventcolorid, '') AS inventcolorid,
ISNULL(id.inventstyleid, '') AS inventstyleid,
ISNULL(id.inventsizeid, '') AS inventsizeid,
ISNULL(id.configid, '') AS configid
FROM [dataverse_company_prod…].[dbo].pricedisctable PriceDiscSales
LEFT JOIN [dataverse_company_prod…].[dbo].inventdim id
ON id.dataareaid = PriceDiscSales.dataareaid
AND id.inventdimid = PriceDiscSales.inventdimid
WHERE
module = 1 - Sales prices (retail)
AND (todate = '1900–01–01' OR todate > GETDATE())
AND fromdate <= GETDATE()
)
```

## ROW\_NUMBER for Deduplication

Why do we need ROW\_NUMBER? Because the same item can have multiple price records:

```sh
- Example: Item has three price records
ItemID | FromDate | ToDate | Amount
T00123 | 2024–01–01 | 2024–06–30 | 19.99
T00123 | 2024–07–01 | 2024–12–31 | 22.99
T00123 | 2025–01–01 | 1900–01–01 | 24.99 - No end date (1900 = forever)
```

We partition by item and order by fromdate to get a deterministic pick. Then in the final query, we can filter to seqnum = 1 if needed.

## Code Block 7B: The Conditional Join Pattern

This is the core technique. We use CASE expressions in the join condition to match the right combination of variant dimensions based on the product’s dimension group:

```sh
- =====================================================
 - CONDITIONAL JOIN: Pricing varies by dimension group
 - =====================================================
ProductVariants AS (
SELECT
CONCAT(
id.dataareaid, '_',
idc.itemid,
id.inventcolorid,
id.inventstyleid,
id.inventsizeid,
id.configid
) AS ItemKey,
idc.itemid AS itemid,
idc.dataareaid AS dataareaid,
ISNULL(producttrans.name, '') AS ItemName,
ISNULL(CAST(PriceDiscSales.amount AS NUMERIC(10,2)), 0) AS RetailPrice,
ISNULL(CAST(pricediscpurch.amount AS NUMERIC(10,2)), 0) AS CostPerPiece,
 - Variant dimensions
ISNULL(id.inventcolorid, '') AS Color,
ISNULL(id.inventstyleid, '') AS Style,
ISNULL(id.inventsizeid, '') AS Size,
ISNULL(id.configid, '') AS Config
FROM [dataverse_company_prod…].[dbo].inventdimcombination idc
LEFT JOIN [dataverse_company_prod…].[dbo].inventdim id
ON id.inventdimid = idc.inventdimid
AND id.dataareaid = idc.dataareaid
LEFT JOIN [dataverse_company_prod…].[dbo].ecoresproducttranslation producttrans
ON producttrans.languageid = 'en-US'
AND producttrans.product = idc.distinctproductvariant
LEFT JOIN [dataverse_company_prod…].[dbo].ecoresproduct prod
ON prod.displayproductnumber = idc.itemid
 - Get dimension group to know which attributes matter
LEFT JOIN [dataverse_company_prod…].[dbo].ecoresproductdimensiongroupproduct dimprod
ON dimprod.product = prod.recid
LEFT JOIN [dataverse_company_prod…].[dbo].ecoresproductdimensiongroup prodgroup
ON prodgroup.recid = dimprod.productdimensiongroup
 - CONDITIONAL JOIN TO PURCHASE PRICING
LEFT JOIN pricediscpurch ON (
CASE
 - DonatedNS: Match on Color + Style only
WHEN prodgroup.name IN ('DonatedNS') THEN
CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
pricediscpurch.inventstyleid, pricediscpurch.inventcolorid)
 - Donated: Match on Color + Style + Size
WHEN prodgroup.name IN ('Donated') THEN
CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
pricediscpurch.inventcolorid, pricediscpurch.inventstyleid,
pricediscpurch.inventsizeid)
 - DonatedS: Match on Style only
WHEN prodgroup.name IN ('DonatedS') THEN
CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation,
pricediscpurch.inventstyleid)
 - Retail Kit: Match on Config only
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
 - Same conditional logic for sales pricing
LEFT JOIN PriceDiscSales ON (
 - Similar CASE structure as above
…
)
)
```

## Why CONCAT-Based Matching?

We concatenate values into a single string for comparison because:

1\. SQL doesn’t allow dynamic column lists in JOIN conditions

2\. CASE expressions return a single scalar value

3\. CONCAT handles NULLs gracefully (returns empty string)

4\. String comparison is deterministic across all engines

The UNION ALL Pattern for Simple + Variant Products

The final step combines variant products (from the CTE) with simple products (no variants):

```sh
SELECT DISTINCT
t1.*,
GETDATE() AS RefreshDate
FROM (
 - Branch 1: Variant Products
SELECT
ItemKey, itemid, dataareaid, ItemName, RetailPrice, CostPerPiece,
[Type], SubType, Color, Style, Size, Config, Multiples, Stopped, Barcode
FROM ProductVariants
UNION ALL
 - Branch 2: Simple Products
SELECT
CONCAT(t1.dataareaid, '_', t1.itemid) AS ItemKey,
t1.itemid,
t1.dataareaid,
ISNULL(producttrans.name, '') AS ItemName,
 - Pricing: If item has variants, set to 0 (price is on variant level)
CASE
WHEN t1.itemid IN (SELECT itemid FROM ProductVariants) THEN 0
ELSE (
SELECT TOP 1 amount
FROM [dataverse_company_prod…].[dbo].pricedisctable
WHERE itemrelation = t1.itemid
AND module = 1
AND (todate = '1900–01–01' OR todate > GETDATE())
)
END AS RetailPrice,
'' AS Color, - Simple products have no variants
'' AS Style,
'' AS Size,
'' AS Config,
…
FROM [dataverse_company_prod…].[dbo].inventtable t1
…
) t1;
```

## UNION ALL vs UNION

Why UNION ALL?

\- UNION removes duplicates (expensive sort operation)

\- UNION ALL is faster (no deduplication)

\- We already guarantee no overlap via the subquery filter

## What’s Coming in Part 3

Now that you’ve built a complete product dimension with correct pricing, you’ll face the next challenge: making it fast enough for production.

In [Part 3: Performance Optimization and Common Issues](https://medium.com/@jjr8888/d02abbc97319), we’ll cover:

\- Materialized views vs. regular views: When to pre-compute your dimension

\- Distribution strategies: Replicated tables and their trade-offs

\- Common debugging scenarios: Missing prices, duplicate barcodes, and performance degradation

\- Production optimization patterns: CETAS, filtered indexes, and early filtering

## Summary

In this article, we covered:

✅ Pricing CTEs: Separate CTEs for purchase and sales pricing with ROW\_NUMBER deduplication

✅ Conditional joins: CASE expressions to match different variant dimensions based on dimension group

✅ CONCAT matching: String concatenation for dynamic join criteria

✅ UNION ALL pattern: Combining variant and simple products efficiently

The conditional join is the heart of the product dimension. Get this right, and your prices will resolve correctly for every product type.

## Additional Resources

\- Full view SQL: [sqlqueries\_optimized\_Retail\_New\_DeltaLake.sql](https://github.com/jessejinnaruiz/comp_source_code_examples/blob/main/sqlqueries_optimized_Retail_New_DeltaLake.sql)

\- D365 F&O product dimensions: [https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-dimensions](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-dimensions)

\- PriceDiscTable entity reference: [https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/entity-pricedisctable](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/entity-pricedisctable)

\- SQL Server ROW\_NUMBER function: [https://learn.microsoft.com/en-us/sql/t-sql/functions/row-number-transact-sql](https://learn.microsoft.com/en-us/sql/t-sql/functions/row-number-transact-sql)