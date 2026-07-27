---
title: "Advanced Power BI DAX Measures for Retail Analytics Pt 2"
source: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317"
author:
  - "[[Jesse Ruiz (she/they)]]"
published: 2026-07-20
created: 2026-07-27
description: "Part 2: Time Intelligence and Inventory Aging"
Processed: "Unprocessed"
---
## Part 2: Time Intelligence and Inventory Aging

A conversational technical guide to time-based calculations and aging analysis

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*TLOWexl0NWtuFyFI)

Photo by Jack B on Unsplash

## The Problem: Comparing Time Periods Correctly

Retail analytics requires constant comparisons across time:

\- How do this month’s sales compare to last month?

\- What were our year-to-date sales vs. same period last year?

\- What percentage of sales come from fresh inventory vs. aged inventory?

These questions seem simple, but the underlying DAX is subtle. Get it wrong, and your year-over-year comparisons will return garbage.

## Code Block 9F: Month-to-Date Sales

DAX provides built-in time intelligence functions when you have a proper date table:

```sh
- =====================================================
 - MONTH-TO-DATE SALES
 - =====================================================
MEASURE _Metrics[MTD Sales] =
TOTALMTD(
SUM('RetailSalesTransactions'[NetAmount]), - Measure to aggregate
'dateTable'[Date] - Date column to use
)
```

TOTALMTD automatically calculates the cumulative sum from the first of the month through the selected date. If the user filters to January 15, it sums January 1–15.

Under the Hood:

```sh
- TOTALMTD is equivalent to:
CALCULATE(
SUM('RetailSalesTransactions'[NetAmount]),
DATESMTD('dateTable'[Date])
)
```

## Code Block 9G: Year-to-Date Sales

```sh
- =====================================================
 - YEAR-TO-DATE SALES
 - =====================================================
MEASURE _Metrics[YTD Sales] =
TOTALYTD(
SUM('RetailSalesTransactions'[NetAmount]),
'dateTable'[Date]
)
```

Same pattern as MTD, but accumulates from January 1 through the selected date.

## Code Block 9H: Year-over-Year Sales (Same Period Last Year)

This is where it gets interesting. We need to compare the current period to the same period one year ago:

```sh
- =====================================================
 - YEAR-OVER-YEAR SALES (Prior Year Same Period)
 - =====================================================
MEASURE _Metrics[YOY Sales] =
CALCULATE(
[Total Sales], - Base measure
ALL('dateTable'[Date]), - Remove current date filter
SAMEPERIODLASTYEAR('dateTable'[Date]) - Apply prior year dates
)
```

How It Works:

If the current filter is January 1–15, 2024:

1\. ALL removes the 2024 date filter

2\. SAMEPERIODLASTYEAR shifts to January 1–15, 2023

3\. Total Sales is calculated for the 2023 period

Alternative Pattern:

```sh
- Same result, slightly different syntax
MEASURE _Metrics[Total Sales SPLY] =
CALCULATE(
SUM('RetailSalesTransactions'[NetAmount]),
ALL('dateTable'[Date]),
SAMEPERIODLASTYEAR('dateTable'[Date])
)
```

## Code Block 9I: Year-to-Date Budget with MAXX

Budgets are often stored differently than actuals. You might have one budget row per month, not per day. Here’s how to get the YTD budget respecting slicer selections:

```sh
- =====================================================
 - YEAR-TO-DATE BUDGET
 - =====================================================
MEASURE _Metrics[YTD Budget] =
CALCULATE(
SUM('StoreBudgets'[YTDBudget]),
'StoreBudgets'[Date] = MAXX(
ALLSELECTED(dateTable), - Respects slicers
dateTable[Date]
)
)
```

MAXX + ALLSELECTED finds the latest date in the user’s slicer selection, then retrieves the budget for that date (which would contain the YTD amount up to that point).

## Code Block 9J: Year-to-Date Variance

Now we combine the YTD measures with our variance pattern:

```sh
- =====================================================
 - YEAR-TO-DATE VARIANCE
 - =====================================================
MEASURE _Metrics[YTD %] =
VAR year_to_date_percent =
IF(
ISBLANK([YTD Budget]),
BLANK(),
DIVIDE([YTD Sales], [YTD Budget]) - 1
)
VAR display_year_to_date_percent =
IF(
year_to_date_percent <= -1,
BLANK(),
year_to_date_percent
)
RETURN display_year_to_date_percent
```

## Inventory Aging Analysis

Retail businesses need to track how old their inventory is when it sells. Fresh inventory (0–1 weeks old) selling is good. Old inventory (5+ weeks) selling indicates product aging problems.

## Code Block 9K: 0–1 Week Old Inventory Sales

```sh
- =====================================================
 - INVENTORY AGING: 0–1 WEEK OLD SALES
 - =====================================================
MEASURE _Metrics[0–1 Week $] =
CALCULATE(
[Total Sales],
RetailSalesTransactions[AgeInWeeks] = 0, - Filter to fresh items
DATESBETWEEN(
dateTable[Date],
MINX(ALLSELECTED(dateTable), dateTable[Date]), - Slicer start
MAXX(ALLSELECTED(dateTable), dateTable[Date]) - Slicer end
)
)
```

The DATESBETWEEN with ALLSELECTED ensures we respect the user’s date slicer while also filtering by inventory age.

## Code Block 9L: 1–2 Weeks Old (With Zero Handling)

```sh
- =====================================================
 - 1–2 WEEKS OLD
 - =====================================================
MEASURE _Metrics[1–2 Week $] =
VAR _1weekold =
CALCULATE(
[Total Sales],
RetailSalesTransactions[AgeInWeeks] = 1,
DATESBETWEEN(
dateTable[Date],
MINX(ALLSELECTED(dateTable), dateTable[Date]),
MAXX(ALLSELECTED(dateTable), dateTable[Date])
)
)
 - RETURN 0 instead of BLANK for summing percentages
RETURN IF(ISBLANK(_1weekold), 0, _1weekold)
```

### Why Return 0 Instead of BLANK?

When calculating percentages, we’ll sum all the age buckets to get a total. If one bucket returns BLANK, the sum becomes undefined. Returning 0 ensures:

\`\`\`

25% + 0% + 50% + 25% = 100% (correct)

25% + BLANK + 50% + 25% =? (undefined)

\`\`\`

## Code Block 9M: 5+ Weeks Old (Aged Inventory)

```sh
- =====================================================
 - 5+ WEEKS OLD (Aged Inventory)
 - =====================================================
MEASURE _Metrics[5+ Week $] =
VAR _weeksold =
CALCULATE(
[Total Sales],
RetailSalesTransactions[AgeInWeeks] > 4, - 5 or more weeks
DATESBETWEEN(
dateTable[Date],
MINX(ALLSELECTED(dateTable), dateTable[Date]),
MAXX(ALLSELECTED(dateTable), dateTable[Date])
)
)
RETURN IF(ISBLANK(_weeksold), 0, _weeksold)
```

## Code Block 9N: Total and Percentage Measures

```sh
- =====================================================
 - TOTAL SALES (SUM OF AGE BUCKETS)
 - =====================================================
MEASURE _Metrics[Total_SumOfWeeksAge] =
CALCULATE(
[0–1 Week $] + [1–2 Week $] + [2–3 Week $] +
[3–4 Week $] + [4–5 Week $] + [5+ Week $],
DATESBETWEEN(
dateTable[Date],
MIN(dateTable[Date]),
MAX(dateTable[Date])
)
)
 - ===== PERCENTAGE MEASURES =====
MEASURE _Metrics[0–1 Week %] = DIVIDE([0–1 Week $], [Total_SumOfWeeksAge])
MEASURE _Metrics[1–2 Week %] = DIVIDE([1–2 Week $], [Total_SumOfWeeksAge])
MEASURE _Metrics[5+ Week %] = DIVIDE([5+ Week $], [Total_SumOfWeeksAge])
 - ===== AVERAGE AGE =====
MEASURE _Metrics[AVG Product Age in Weeks] =
AVERAGE(RetailSalesTransactions[AgeInWeeks])
```

## Teaching Points

### 1\. ALLSELECTED for Slicer Awareness

```sh
- ALLSELECTED: Respects slicer selections
MINX(ALLSELECTED(dateTable), dateTable[Date]) - Earliest date in slicer
 - ALL: Ignores all filters
MINX(ALL(dateTable), dateTable[Date]) - Earliest date in entire table
```

Use ALLSELECTED when you want to preserve user slicer choices. Use ALL when you want to ignore all filters.

### 2\. DATESBETWEEN for Dynamic Filtering

```sh
DATESBETWEEN(
dateTable[Date],
MINX(ALLSELECTED(dateTable), dateTable[Date]), - Dynamic start
MAXX(ALLSELECTED(dateTable), dateTable[Date]) - Dynamic end
)
 - Vs. hardcoded filter:
 - dateTable[Date] >= DATE(2024, 1, 1) - Static, breaks with different slicers
```

DATESBETWEEN creates a dynamic date range based on context, not hardcoded values.

### 3\. Context Transition with CALCULATE

```sh
- CALCULATE forces filter context transformation
MEASURE Sales = SUM(Transactions[NetAmount]) - Uses current filter context
MEASURE AvgSalesPerStore =
AVERAGEX(
VALUES(Stores[StoreID]), - Creates row context per store
CALCULATE([Sales]) - Transitions back to filter context
)
```

Inside AVERAGEX, we iterate over each store (row context). CALCULATE converts that row context back to filter context so \[Sales\] evaluates correctly for each store.

## What’s Coming in Part 3

In Part 3: Production Targets and Best Practices, we’ll cover:

\- Production target measures (daily/monthly/annual goals)

\- SELECTEDVALUE for granularity detection

\- Dashboard application patterns

\- Common pitfalls and solutions

Continue to [Part 3: Production Targets + Best Practices](https://medium.com/@jjr8888/f152d1b500b5)

## Summary

In this article, we covered:

\- TOTALMTD and TOTALYTD: Built-in time intelligence functions

\- SAMEPERIODLASTYEAR: Year-over-year comparisons

\- MAXX + ALLSELECTED: Getting values for the latest date in slicer

\- Inventory aging buckets: Calculating sales by product age

\- Returning 0 vs BLANK: Ensuring percentages sum correctly

\- DATESBETWEEN: Dynamic date range filtering

These patterns form the foundation for any time-based retail analytics dashboard.

## Additional Resources

\- SQLBI Time Intelligence patterns: [https://www.sqlbi.com/articles/time-intelligence-in-power-bi-desktop/](https://www.sqlbi.com/articles/time-intelligence-in-power-bi-desktop/)

\- TOTALMTD function: [https://learn.microsoft.com/en-us/dax/totalmtd-function-dax](https://learn.microsoft.com/en-us/dax/totalmtd-function-dax)

\- SAMEPERIODLASTYEAR function: [https://learn.microsoft.com/en-us/dax/sameperiodlastyear-function-dax](https://learn.microsoft.com/en-us/dax/sameperiodlastyear-function-dax)

\- ALLSELECTED function: [https://learn.microsoft.com/en-us/dax/allselected-function-dax](https://learn.microsoft.com/en-us/dax/allselected-function-dax)