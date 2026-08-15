-- =====================================================
-- DIMENSIONAL MODELING: Product Dimension with Variants
-- Purpose: Complex product dimension handling simple products
--          and variant products (Color/Style/Size/Config)
-- Source: D365 F&O Retail module tables
-- =====================================================

-- =====================================================
-- DIM_AllItems VIEW
-- Handles: Simple products + 4 dimension group types
-- Pattern: Conditional joins based on product dimension group
-- =====================================================

CREATE VIEW [Delta].[DIM_AllItems] AS 

-- =====================================================
-- CTE 1: PURCHASE PRICING (Cost)
-- Purpose: Get active purchase prices with variant dimensions
-- =====================================================
WITH pricediscpurch AS (
    SELECT 
        pricediscpurch.*,
        -- ROW_NUMBER: Handle multiple price records per item
        ROW_NUMBER() OVER (
            PARTITION BY CONCAT(pricediscpurch.dataareaid, pricediscpurch.itemrelation)
            ORDER BY pricediscpurch.fromdate
        ) AS seqnum,
        
        -- Extract variant dimensions from price table
        ISNULL(id.inventcolorid, '') AS inventcolorid,
        ISNULL(id.inventstyleid, '') AS inventstyleid,
        ISNULL(id.inventsizeid, '') AS inventsizeid,
        ISNULL(id.configid, '') AS configid
        
    FROM [dataverse_company_prod].[dbo].pricedisctable pricediscpurch
    
    LEFT JOIN [dataverse_company_prod].[dbo].inventdim id 
        ON id.inventdimid = pricediscpurch.inventdimid
        AND id.dataareaid = pricediscpurch.dataareaid
    
    WHERE 
        module = 2                                        -- Purchase prices (cost)
        AND (todate = '1900-01-01' OR todate > GETDATE()) -- Active prices only
        AND fromdate <= GETDATE()
),

-- =====================================================
-- CTE 2: SALES PRICING (Retail Price)
-- Purpose: Get active sales prices with variant dimensions
-- =====================================================
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
        
    FROM [dataverse_company_prod].[dbo].pricedisctable PriceDiscSales
    
    LEFT JOIN [dataverse_company_prod].[dbo].inventdim id 
        ON id.dataareaid = PriceDiscSales.dataareaid
        AND id.inventdimid = PriceDiscSales.inventdimid
    
    WHERE 
        module = 1                                        -- Sales prices (retail)
        AND (todate = '1900-01-01' OR todate > GETDATE())
        AND fromdate <= GETDATE()
),

-- =====================================================
-- CTE 3: PRODUCT VARIANTS
-- Purpose: All variant combinations with conditional pricing joins
-- Key Pattern: CASE-based join conditions vary by dimension group
-- =====================================================
ProductVariants AS (
    SELECT 
        -- Composite key: dataareaid_itemid_color_style_size_config
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
        '' AS Category,
        ISNULL(producttrans.name, '') AS ItemName,
        ISNULL(CAST(PriceDiscSales.amount AS NUMERIC(10,2)), 0) AS RetailPrice,
        '' AS BuyerGroup,
        ISNULL(CAST(pricediscpurch.amount AS NUMERIC(10,2)), 0) AS CostPerPiece,
        '' AS ItemGroup,
        '' AS CategoryHierarchy,
        
        -- Custom type fields (from InventTable)
        ISNULL((
            SELECT TOP 1 itemtype 
            FROM [dataverse_company_prod].[dbo].inventtable
            WHERE itemid = idc.itemid
        ), '') AS [Type],
        
        ISNULL((
            SELECT TOP 1 itemsubtype 
            FROM [dataverse_company_prod].[dbo].inventtable
            WHERE itemid = idc.itemid
        ), '') AS SubType,
        
        -- Variant dimensions
        ISNULL(id.inventcolorid, '') AS Color,
        ISNULL(id.inventstyleid, '') AS Style,
        ISNULL(id.inventsizeid, '') AS Size,
        ISNULL(id.configid, '') AS Config,
        
        -- Purchasing metadata
        CAST(purchset.multipleqty AS NUMERIC(10,2)) AS Multiples,
        CASE WHEN purchset.stopped = 1 THEN 'Yes' ELSE 'No' END AS Stopped,
        
        -- Barcode
        ISNULL(bar.itembarcode, '') AS Barcode
        
    FROM [dataverse_company_prod].[dbo].inventdimcombination idc
    
    -- Join 1: Variant attributes
    LEFT JOIN [dataverse_company_prod].[dbo].inventdim id 
        ON id.inventdimid = idc.inventdimid
        AND id.dataareaid = idc.dataareaid
    
    -- Join 2: Product translation (name)
    LEFT JOIN [dataverse_company_prod].[dbo].ecoresproducttranslation producttrans 
        ON producttrans.languageid = 'en-US'
        AND producttrans.product = idc.distinctproductvariant
    
    -- Join 3: Product master record
    LEFT JOIN [dataverse_company_prod].[dbo].ecoresproduct prod 
        ON prod.displayproductnumber = idc.itemid
    
    -- Join 4: Dimension group (determines which dimensions apply)
    LEFT JOIN [dataverse_company_prod].[dbo].ecoresproductdimensiongroupproduct dimprod 
        ON dimprod.product = prod.recid
    
    LEFT JOIN [dataverse_company_prod].[dbo].ecoresproductdimensiongroup prodgroup 
        ON prodgroup.recid = dimprod.productdimensiongroup
    
    -- Join 5: Purchase setup (multiples, stopped status)
    LEFT JOIN [dataverse_company_prod].[dbo].inventitempurchsetup purchset 
        ON purchset.itemid = idc.itemid
        AND purchset.dataareaid = idc.dataareaid
    
    -- Join 6: Barcode
    LEFT JOIN [dataverse_company_prod].[dbo].inventitembarcode bar 
        ON bar.retailvariantid = idc.retailvariantid
        AND idc.dataareaid = bar.dataareaid
        AND bar.retailshowforitem = 1                     -- Primary barcode only
    
    -- =====================================================
    -- CONDITIONAL JOIN: Purchase pricing varies by dimension group
    -- DonatedNS: Color + Style only
    -- Donated: Color + Style + Size
    -- DonatedS: Style only
    -- Retail Kit: Config only
    -- =====================================================
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
    
    -- Conditional join for sales pricing (same pattern)
    LEFT JOIN PriceDiscSales ON (
        CASE
            WHEN prodgroup.name IN ('DonatedNS') THEN 
                CONCAT(PriceDiscSales.dataareaid, PriceDiscSales.itemrelation, 
                       PriceDiscSales.inventcolorid, PriceDiscSales.inventstyleid)
            WHEN prodgroup.name IN ('Donated') THEN 
                CONCAT(PriceDiscSales.dataareaid, PriceDiscSales.itemrelation, 
                       PriceDiscSales.inventcolorid, PriceDiscSales.inventstyleid, 
                       PriceDiscSales.inventsizeid)
            WHEN prodgroup.name IN ('DonatedS') THEN 
                CONCAT(PriceDiscSales.dataareaid, PriceDiscSales.itemrelation, 
                       PriceDiscSales.inventstyleid)
            WHEN prodgroup.name IN ('Retail Kit') THEN 
                CONCAT(PriceDiscSales.dataareaid, PriceDiscSales.itemrelation, 
                       PriceDiscSales.configid)
        END
    ) = (
        CASE
            WHEN prodgroup.name IN ('DonatedNS') THEN 
                CONCAT(idc.dataareaid, idc.itemid, id.inventcolorid, id.inventstyleid)
            WHEN prodgroup.name IN ('Donated') THEN 
                CONCAT(idc.dataareaid, idc.itemid, id.inventcolorid, 
                       id.inventstyleid, id.inventsizeid)
            WHEN prodgroup.name IN ('DonatedS') THEN 
                CONCAT(idc.dataareaid, idc.itemid, id.inventcolorid, id.inventstyleid)
            WHEN prodgroup.name IN ('Retail Kit') THEN 
                CONCAT(idc.dataareaid, idc.itemid, id.configid)
        END
    )
)

-- =====================================================
-- FINAL SELECT: Union of Simple + Variant Products
-- =====================================================
SELECT DISTINCT 
    t1.*,
    GETDATE() AS RefreshDate
FROM (
    -- Branch 1: Simple Products (no variants)
    SELECT 
        CONCAT(t1.dataareaid, '_', t1.itemid) AS ItemKey,
        t1.itemid,
        t1.dataareaid,
        ISNULL(t1.itemcategory, '') AS Category,
        ISNULL(producttrans.name, '') AS ItemName,
        
        -- Pricing: If item has variants, set to 0 (price is on variant level)
        CASE 
            WHEN t1.itemid IN (SELECT itemid FROM ProductVariants) THEN 0
            ELSE (
                SELECT TOP 1 PriceDiscSales.amount
                FROM [dataverse_company_prod].[dbo].pricedisctable PriceDiscSales
                WHERE PriceDiscSales.itemrelation = t1.itemid
                    AND PriceDiscSales.itemcode = 0
                    AND PriceDiscSales.dataareaid = t1.dataareaid
                    AND PriceDiscSales.module = 1
                    AND (todate = '1900-01-01' OR todate > GETDATE())
                    AND fromdate <= GETDATE()
            )
        END AS RetailPrice,
        
        ISNULL(t1.itembuyergroupid, '') AS BuyerGroup,
        
        CASE 
            WHEN t1.itemid IN (SELECT itemid FROM ProductVariants) THEN 0
            ELSE (
                SELECT TOP 1 pricediscpurch.amount
                FROM [dataverse_company_prod].[dbo].pricedisctable pricediscpurch
                WHERE pricediscpurch.itemrelation = t1.itemid
                    AND pricediscpurch.itemcode = 0
                    AND pricediscpurch.dataareaid = t1.dataareaid
                    AND pricediscpurch.module = 2
                    AND (pricediscpurch.todate = '1900-01-01' OR pricediscpurch.todate > GETDATE())
            )
        END AS CostPerPiece,
        
        ISNULL(inventitemgroupitem.itemgroupid, '') AS ItemGroup,
        '' AS CategoryHierarchy,
        ISNULL(t1.itemtype, '') AS [Type],
        ISNULL(t1.itemsubtype, '') AS SubType,
        '' AS Color,           -- Simple products have no variants
        '' AS Style,
        '' AS Size,
        '' AS Config,
        CAST(setup.multipleqty AS NUMERIC(10,2)) AS Multiples,
        '' AS Stopped,
        ISNULL(bar.itembarcode, '') AS Barcode
        
    FROM [dataverse_company_prod].[dbo].[inventtable] t1
    
    LEFT JOIN [dataverse_company_prod].[dbo].ecoresproducttranslation producttrans 
        ON producttrans.languageid = 'en-US'
        AND producttrans.product = t1.product
    
    LEFT JOIN [dataverse_company_prod].[dbo].[inventitemgroupitem] 
        ON inventitemgroupitem.itemdataareaid = t1.dataareaid
        AND inventitemgroupitem.itemid = t1.itemid
    
    LEFT JOIN [dataverse_company_prod].[dbo].inventitembarcode bar 
        ON bar.itemid = t1.itemid
        AND bar.dataareaid = t1.dataareaid
        AND bar.retailshowforitem = 1
    
    LEFT JOIN [dataverse_company_prod].[dbo].inventitempurchsetup setup 
        ON setup.itemid = t1.itemid
        AND setup.dataareaid = t1.dataareaid
    
    UNION ALL
    
    -- Branch 2: Variant Products (from ProductVariants CTE)
    SELECT 
        ItemKey, itemid, dataareaid, Category, ItemName, RetailPrice,
        BuyerGroup, CostPerPiece, ItemGroup, CategoryHierarchy,
        [Type], SubType, Color, Style, Size, Config, Multiples, Stopped, Barcode
    FROM ProductVariants
    
) t1
GO


-- =====================================================
-- QUERYING THE DIMENSION FROM FACT TABLES
-- Example: How to join fact tables to product dimension
-- =====================================================

-- SELECT 
--     f.TransactionID,
--     f.ItemID,
--     f.NetAmount,
--     
--     -- Dimension attributes
--     dim.ItemName,
--     dim.RetailPrice,
--     dim.CostPerPiece,
--     dim.Type,
--     dim.SubType
--     
-- FROM FACT_RetailTransSalesTrans f
-- 
-- LEFT JOIN Delta.DIM_AllItems dim ON 
--     dim.ItemKey = CASE
--         WHEN f.inventdimid IS NULL THEN 
--             CONCAT(f.dataareaid, '_', f.itemid)          -- Simple product
--         ELSE 
--             CONCAT(f.dataareaid, '_', f.itemid, 
--                    f.inventcolorid, f.inventstyleid, 
--                    f.inventsizeid, f.configid)           -- Variant product
--     END;


-- =====================================================
-- PERFORMANCE OPTIMIZATION OPTIONS
-- =====================================================

-- Option 1: Materialized view (dedicated SQL pool)
-- CREATE MATERIALIZED VIEW [Delta].[DIM_AllItems_Materialized] AS ...

-- Option 2: CETAS pattern (serverless pool)
-- CREATE EXTERNAL TABLE [Delta].[DIM_AllItems_External]
-- WITH (LOCATION = '/dimensions/dim_allitems/', ...)
-- AS SELECT * FROM [Delta].[DIM_AllItems];

-- Option 3: Indexing (if using dedicated pool)
-- CREATE INDEX idx_itemkey ON DIM_AllItems(ItemKey);
-- CREATE INDEX idx_itemid ON DIM_AllItems(itemid, dataareaid);
-- CREATE INDEX idx_barcode ON DIM_AllItems(Barcode) WHERE Barcode != '';
