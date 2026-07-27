---
title: "Data Engineering Coding Challenge (DAX)"
source: "https://medium.com/@jjr8888/data-engineering-coding-challenge-dax-e6225dcc8d1f"
author:
  - "[[Jesse Ruiz (she/they)]]"
published: 2026-06-17
created: 2026-07-27
description: "​Sample Data Engineering Take Home Test with Solution"
Processed: "Unprocessed"
---
## Sample Data Engineering Take Home Test with Solution

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*vSBTqrPubmhzqV2_)

Photo by Scott Graham on Unsplash

In this article, I provide readers with a hands-on DAX coding challenge: building a comprehensive sales analytics measure library for Power BI. This exercise tests your ability to create production-ready measures that handle time intelligence, comparisons, and edge cases.

This challenge simulates a real BI developer take-home assignment. Set aside 30–45 minutes and try to complete it before viewing the solution below.

If you’re interested in data engineering, cloud architecture and practical technical guidance, please consider following my medium page.

## The Challenge: Build a Sales Analytics Measure Library

Your Power BI model has these tables:

\- Sales (OrderID, OrderDate, CustomerID, ProductID, Quantity, Amount)

\- Calendar (Date, Year, Month, Quarter)

\- Products (ProductID, ProductName, Category)

\- Customers (CustomerID, CustomerName, Segment)

Create these measures:

1\. Total Sales — basic sum of Amount

2\. YTD Sales — year-to-date cumulative sales

3\. Previous Year Sales — same period last year

4\. YoY Growth % — year-over-year percentage change with proper NULL handling

5\. Sales Contribution % — each category’s percentage of total sales

Don’t look at the solution below until you tried it yourself…(scroll down for solution)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*bn7knOx--vhQ4THD)

Photo by Aron Visuals on Unsplash

## Complete Solution:

```sh
// =====================================================
// MEASURE 1: Total Sales (Foundation)
// =====================================================
Total Sales = SUM(Sales[Amount])
 - Comments: This is your base measure. All other measures reference this
 - rather than repeating SUM(Sales[Amount]). Single point of change.
// =====================================================
// MEASURE 2: YTD Sales (Year-to-Date)
// =====================================================
YTD Sales =
TOTALYTD(
[Total Sales],
Calendar[Date]
)
 - Alternative with explicit date logic:
YTD Sales Alt =
CALCULATE(
[Total Sales],
DATESYTD(Calendar[Date])
)
 - Comments: TOTALYTD is syntactic sugar for CALCULATE + DATESYTD.
 - Both require a proper Date table marked as a date table in Power BI.
 - If user selects March 2024, this shows cumulative Jan-Mar 2024.
// =====================================================
// MEASURE 3: Previous Year Sales
// =====================================================
Previous Year Sales =
CALCULATE(
[Total Sales],
SAMEPERIODLASTYEAR(Calendar[Date])
)
 - Comments: SAMEPERIODLASTYEAR shifts the entire date filter context
 - back one year. If March 2024 is selected, this returns March 2023.
 - Works with any date granularity (day, month, year).
// =====================================================
// MEASURE 4: YoY Growth % (with NULL handling)
// =====================================================
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
 - Comments: Three edge cases matter:
 - 1. No prior year data (new product) → show BLANK, not error
 - 2. Prior year was zero → avoid division by zero
 - 3. Use DIVIDE() which returns BLANK on div/0 automatically
 - Simpler alternative:
YoY Growth % Simple =
DIVIDE(
[Total Sales] - [Previous Year Sales],
[Previous Year Sales]
)
 - Comments: DIVIDE handles the zero case automatically, returning BLANK.
 - Use the VAR version when you need more explicit control or logging.
// =====================================================
// MEASURE 5: Sales Contribution % (Percentage of Total)
// =====================================================
Sales Contribution % =
VAR CurrentCategorySales = [Total Sales]
VAR AllCategoriesSales = CALCULATE([Total Sales], ALL(Products[Category]))
RETURN
DIVIDE(CurrentCategorySales, AllCategoriesSales)
 - Comments: ALL(Products[Category]) removes category filter, giving grand total.
 - If user filters to Electronics, this shows Electronics as % of ALL categories.
 - Within-segment version (% of parent):
Sales Contribution Within Segment % =
VAR CurrentSales = [Total Sales]
VAR SegmentTotal = CALCULATE(
[Total Sales],
ALLEXCEPT(Products, Products[Category])
)
RETURN
DIVIDE(CurrentSales, SegmentTotal)
 - Comments: ALLEXCEPT removes ALL filters EXCEPT specified columns.
 - Shows product as % of its category, not % of everything.
```

## Key Points to Discuss:

1\. Why reference \[Total Sales\] instead of SUM()? Single source of truth. If business logic changes (exclude returns, convert currency), you change one measure.

2\. Why VAR statements? Readability and performance. Values compute once and can be reused. Makes debugging easier — you can see intermediate results.

3\. Why BLANK() not zero for missing data? BLANK propagates correctly in charts (gaps in line charts) and doesn’t distort averages. Zero would imply “measured and was zero” vs “no data.”

4\. Why ALL vs ALLEXCEPT? ALL removes all filters on a table/column. ALLEXCEPT removes everything except specified columns — useful for hierarchical percentages.

5\. Date table requirement? All time intelligence functions require a contiguous date table marked as a date table. Missing dates break these calculations.

Thanks for reading!

#tech #codingchallenge #dax #powerbi #dataanalytics