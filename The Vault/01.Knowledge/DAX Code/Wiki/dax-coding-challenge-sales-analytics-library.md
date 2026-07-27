---
created: 2026-07-27
source: "Data Engineering Coding Challenge (DAX)"
source_url: "https://medium.com/@jjr8888/data-engineering-coding-challenge-dax-e6225dcc8d1f"
note_type: reference
tags: [dax, reference, coding-challenge, measure-library, sales-analytics]
---

# DAX Coding Challenge — Sales Analytics Library

A solved take-home coding challenge covering the five foundational measures of a sales analytics library: Total Sales, YTD Sales, Previous Year Sales, YoY Growth %, and Sales Contribution %.

> **Challenge source tables:** Sales (OrderID, OrderDate, CustomerID, ProductID, Quantity, Amount), Calendar (Date, Year, Month, Quarter), Products (ProductID, ProductName, Category), Customers (CustomerID, CustomerName, Segment)

## The Five Measures

```dax
-- 1. Total Sales (single source of truth)
Total Sales = SUM(Sales[Amount])

-- 2. YTD Sales
YTD Sales =
TOTALYTD([Total Sales], Calendar[Date])

-- Alternative with explicit date logic
YTD Sales Alt =
CALCULATE([Total Sales], DATESYTD(Calendar[Date]))

-- 3. Previous Year Sales
Previous Year Sales =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(Calendar[Date])
)

-- 4. YoY Growth % (with edge case handling)
YoY Growth % =
VAR CurrentSales = [Total Sales]
VAR PriorSales = [Previous Year Sales]
VAR Growth = CurrentSales - PriorSales
RETURN
IF(
    ISBLANK(PriorSales) || PriorSales = 0,
    BLANK(),
    DIVIDE(Growth, PriorSales)
)

-- 5. Sales Contribution % (category % of all categories)
Sales Contribution % =
VAR CurrentCategorySales = [Total Sales]
VAR AllCategoriesSales = CALCULATE([Total Sales], ALL(Products[Category]))
RETURN DIVIDE(CurrentCategorySales, AllCategoriesSales)

-- Within-segment version (% of parent category)
Sales Contribution Within Segment % =
VAR CurrentSales = [Total Sales]
VAR SegmentTotal = CALCULATE(
    [Total Sales],
    ALLEXCEPT(Products, Products[Category])
)
RETURN DIVIDE(CurrentSales, SegmentTotal)
```

## Key Teaching Points

1. **Single source of truth** — reference `[Total Sales]` not `SUM(Sales[Amount])` in all other measures
2. **VAR pattern** — evaluate once, reuse; makes debugging and logic clear
3. **BLANK() not 0 for missing data** — BLANK propagates correctly in charts; 0 implies "measured and was zero"
4. **ALL vs ALLEXCEPT** — ALL removes all category filters; ALLEXCEPT removes everything except Category (needed for within-segment %)
5. **Date table requirement** — all time intelligence functions require a contiguous date table marked as a date table

## Related

- [[sales-to-budget-variance-percent]] — retail-specific variance pattern
- [[inventory-aging-buckets-0-1-1-2-5-weeks]] — more advanced retail analytics measures
- [[time-intelligence-quick-reference-retail-analytics]] — function cheat sheet
