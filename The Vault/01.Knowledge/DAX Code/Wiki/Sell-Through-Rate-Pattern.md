---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 3
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-3-f152d1b500b5
note_type: pattern
tags: [dax, retail, production, sell-through, ratio]
---

# Sell-Through Rate Pattern

Calculate what percentage of produced or donated goods actually sold. Used in retail and manufacturing to measure inventory efficiency.

## Formula

$$\text{Sell-Through Rate} = \frac{\text{Items Sold}}{\text{Items Produced}}$$

## Three-Step Build

### Step 1: Items Sold (by category)

```dax
MEASURE [DG_IT_#] =
CALCULATE(
    COUNT(Sales[ItemID]),
    Sales[CatGroup] = "DONATED GOODS"
)
```

Count items sold filtered to the target category.

### Step 2: Items Produced (by category)

```dax
MEASURE [Total_Production_D365_#] =
CALCULATE(
    COUNT(Production[ItemID]),
    Production[CatGroup] = "DONATED GOODS"
)
```

Count items produced from the production table filtered to the same category.

### Step 3: Sell-Through Rate

```dax
MEASURE [SellThrough_Total] =
DIVIDE([DG_IT_#], [Total_Production_D365_#], BLANK())
```

`DIVIDE` with `BLANK()` as the third argument: if no items were produced, return BLANK rather than 0%.

## Hardlines vs. Softlines Split

```dax
MEASURE [Hardlines SellThrough] =
DIVIDE(
    CALCULATE(COUNT(Sales[ItemID]), Sales[CatGroup] = "DONATED GOODS", Sales[Class] = "Hardlines"),
    CALCULATE(COUNT(Production[ItemID]), Production[CatGroup] = "DONATED GOODS", Production[Class] = "Hardlines"),
    BLANK()
)

MEASURE [Softlines SellThrough] =
DIVIDE(
    CALCULATE(COUNT(Sales[ItemID]), Sales[CatGroup] = "DONATED GOODS", Sales[Class] = "Softlines"),
    CALCULATE(COUNT(Production[ItemID]), Production[CatGroup] = "DONATED GOODS", Production[Class] = "Softlines"),
    BLANK()
)
```

## Related

- [[DIVIDE-Safe-Division]] — DIVIDE returns BLANK on zero; / throws error
- [[Inventory-Aging-Buckets-Pattern]] — related retail analytics pattern
