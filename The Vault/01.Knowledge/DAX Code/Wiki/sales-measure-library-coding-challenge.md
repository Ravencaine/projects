---
created: 2026-07-27
updated: 2026-08-02
source: "Data Engineering Coding Challenge (DAX)"
source_url: https://medium.com/@jjr8888/data-engineering-coding-challenge-dax-e6225dcc8d1f
author: "[[Jesse Ruiz]]"
published: 2026-06-17
note_type: pattern
tags: [dax, measure-library, sales-analytics, time-intelligence, ytd, yoy-growth]
---

# Sales Measure Library Coding Challenge

Hands-on exercise building a production-ready DAX sales analytics measure library. Tests time intelligence, comparisons, and edge case handling.

## Purpose

A structured measure library for a Power BI sales analytics model. Each measure references a base measure rather than repeating column references — single point of change when business logic evolves.

## Model Prerequisites

Required tables: `Sales (OrderID, OrderDate, CustomerID, ProductID, Quantity, Amount)`, `Calendar (Date, Year, Month, Quarter)`, `Products (ProductID, ProductName, Category)`, `Customers (CustomerID, CustomerName, Segment)`.

A contiguous `Calendar` table marked as a date table is required for all time intelligence functions.

## Structure

### Measure 1: Total Sales (Foundation)

```dax
Total Sales = SUM(Sales[Amount])
```

All subsequent measures reference `[Total Sales]` rather than repeating `SUM(Sales[Amount])`.

### Measure 2: YTD Sales (Year-to-Date)

```dax
YTD Sales = TOTALYTD([Total Sales], Calendar[Date])
-- Alternative with explicit date logic:
YTD Sales Alt = CALCULATE([Total Sales], DATESYTD(Calendar[Date]))
```

`TOTALYTD` is syntactic sugar for `CALCULATE + DATESYTD`. Both require a proper date table. If user selects March 2024, returns cumulative Jan–Mar 2024.

### Measure 3: Previous Year Sales

```dax
Previous Year Sales =
CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Calendar[Date]))
```

`SAMEPERIODLASTYEAR` shifts the entire date filter context back one year. Works at any date granularity (day, month, year).

### Measure 4: YoY Growth % (with NULL Handling)

```dax
YoY Growth % =
VAR CurrentSales = [Total Sales]
VAR PriorSales = [Previous Year Sales]
VAR Growth = CurrentSales - PriorSales
RETURN
    IF(
        ISBLANK(PriorSales) | PriorSales = 0,
        BLANK(),
        DIVIDE(Growth, PriorSales)
    )
```

Three edge cases this handles:
1. No prior year data (new product) → show BLANK, not an error
2. Prior year was zero → avoid division by zero
3. `DIVIDE()` returns BLANK automatically on div/0

Simpler alternative using `DIVIDE`'s built-in blank-on-error:
```dax
YoY Growth % Simple = DIVIDE([Total Sales] - [Previous Year Sales], [Previous Year Sales])
```

### Measure 5: Sales Contribution % (Percentage of Total)

```dax
Sales Contribution % =
VAR CurrentCategorySales = [Total Sales]
VAR AllCategoriesSales = CALCULATE([Total Sales], ALL(Products[Category]))
RETURN DIVIDE(CurrentCategorySales, AllCategoriesSales)
```

`ALL(Products[Category])` removes the category filter to return the grand total. If user filters to Electronics, shows Electronics as % of ALL categories.

Within-segment version (% of parent):
```dax
Sales Contribution Within Segment % =
VAR CurrentSales = [Total Sales]
VAR SegmentTotal = CALCULATE([Total Sales], ALLEXCEPT(Products, Products[Category]))
RETURN DIVIDE(CurrentSales, SegmentTotal)
```

`ALLEXCEPT` removes ALL filters EXCEPT the specified column — shows product as % of its category, not % of everything.

## Key Design Principles

1. **Single source of truth**: reference `[Total Sales]` not `SUM(Sales[Amount])`. One place to change if business logic changes (exclude returns, convert currency).
2. **Use VAR for readability and performance**: values compute once and can be reused. Makes debugging easier.
3. **Return BLANK, not zero**: BLANK propagates correctly in charts (gaps in line charts) and does not distort averages. Zero implies "measured and was zero" vs. "no data."
4. **ALL vs ALLEXCEPT**: `ALL` removes all filters on a table/column. `ALLEXCEPT` removes everything except specified columns — use for hierarchical percentages.
5. **Date table requirement**: all time intelligence functions require a contiguous date table marked as a date table. Missing dates break these calculations.

## Related

- [[calculate]] — CALCULATE as the foundation for all context modifications
- [[calculate-table]] — CALCULATETABLE for equivalent filter context in table expressions
- [[time-intelligence-quick-reference-retail-analytics]] — comprehensive time intelligence function reference
- [[allexcept]] — ALLEXCEPT vs ALL comparison
- [[divide]] — DIVIDE's blank-on-div-0 behaviour
- [[averagex-iterator-pattern]] — SUMX, AVERAGEX and iterator fundamentals
