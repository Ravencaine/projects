---
title: "Power BI Remove Filter Functions Explained: ALL, ALLSELECTED, ALLEXCEPT & ALLFILTERED with Practical DAX Examples"
source: "https://medium.com/@sultan.jamshed10/power-bi-remove-filter-functions-explained-all-allselected-allexcept-allfiltered-with-5a93e01a7c71"
author:
  - "[[SULTAN ANSARI]]"
published: 2026-07-22
created: 2026-08-03
description: "Introduction"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!QXrPk7zlJYGcTlawRflKwA.png.webp)

## Introduction

When building reports in **Power BI**, one of the biggest challenges is understanding **filter context**. Every slicer, chart, or table on your report page applies filters to your data. Sometimes you want to ignore those filters, sometimes you want to keep a few of them, and sometimes you only want to remove specific filters.

### Understanding Filter Context

Suppose you have the following **Sales** table.

```c
Product   Category      Region    Sales
Laptop   Electronics    North     5000
Mobile   Electronics    South     4000
Chair    Furniture      North     3000
Table    Furniture      South     2000
```

Imagine the report has:

- Region Slicer
- Category Slicer
- Product Chart

Normally every visual follows these filters.

The functions below change this behavior.

1. **ALL()**

ALL() removes **all filters** from a table or a column.

Think of it as saying:

Ignore every filter and calculate using the complete dataset.

```c
Syntax

ALL(Table)

ALL(Column)
```
```c
Total Sales = SUM(Sales[Sales])

Sales All = 
CALCULATE([Total Sales],
ALL(Sales)
)
```
![](99.System/Attachments/1!xfsfPmqtKZZJ-6UWUi3P7A.png.webp)

If the report is filtered to only Bihar state or a Delhi state,Total Sales shows:

1000

But overall sales means total sales still return 1000 because ALL() ignores every filter.

**When to Use ALL()**

- Percentage of total sales
- Overall rankings
- Grand totals
- Benchmark calculations

### 2\. ALLSELECTED()

ALLSELECTED() removes filters applied **inside the visual**, but keeps filters selected by the user from slicers or page filters.

Respect what the user selected, but ignore the current chart’s row context.

```c
Syntax

ALLSELECTED(Table)

ALLSELECTED(Column)
```
```c
AllSelected Sales = CALCULATE(
    [Total Sales],
    ALLSELECTED(Sales)
   
)
```
![](99.System/Attachments/1!inakpG_0_NKeLyP33Ufwzg.png.webp)

The slicer is respected.Only State Bihar region apply filter.

The visual filter is removed.

**Common Uses**

- Dynamic percentages
- Interactive dashboards
- Running totals
- Responsive KPI cards

### 3\. ALLEXCEPT()

ALLEXCEPT() removes every filter except the columns you specify.

Remove all filters except this one.

```c
Syntax

ALLEXCEPT(
    Table,
    Column1,
    Column2
)
```
```c
State Total Sales = 
CALCULATE(
    [Total Sales],
    ALLEXCEPT(
        Sales,
        Sales[State]
    )
)
```
![](99.System/Attachments/1!Ql0pSaEctUhlxPRIIjd5dg.png.webp)

Suppose the report has:

State=Bihar  
Product= Laptop

Normally Total Sales= 1000

State total sales return 700

because it removes Product filters but keeps state filters.

**When to Use ALLEXCEPT()**

- Category totals
- Department totals
- Parent-child calculations
- Percentage within category

### 4\. ALLFILTERED()

ALLFILTERED() removes filters created inside the current visual but keeps filters coming from outside visuals and slicers.

It is similar to ALLSELECTED(), but it works differently in complex filter propagation scenarios.

Return all rows that remain after external filters are applied.

```c
Syntax

ALLFILTERED(Table)

ALLFILTERED(Column)
```
```c
Filtered Sales = CALCULATE( 
[Total Sales], 
ALLFILTERED(Sales) 
)
```

The measure ignores the Product row context but still respects the page and slicer filters.

**Best Uses**

### Final Thoughts

Understanding filter context is one of the most important skills in Power BI. Functions like **ALL**, **ALLSELECTED**, **ALLEXCEPT**, and **ALLFILTERED** give you complete control over how DAX calculations respond to filters.

If you’re building production-level dashboards, mastering these functions will help you create dynamic KPIs, percentage calculations, rankings, and interactive reports with confidence.

The more you practice these functions with real datasets, the easier DAX will become.