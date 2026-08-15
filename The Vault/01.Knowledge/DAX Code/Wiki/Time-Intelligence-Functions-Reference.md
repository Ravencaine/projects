---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 2
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
note_type: reference
tags: [dax, time-intelligence, reference, mtd, ytd, yoy]
---

# Time Intelligence Functions Reference

DAX built-in time intelligence functions for period-based calculations. All require a proper date table with a continuous date column marked as a date table.

## MTD / YTD Accumulation

### TOTALMTD — Month-to-Date

```dax
MEASURE [MTD Sales] =
TOTALMTD(
    SUM('RetailSalesTransactions'[NetAmount]),
    'dateTable'[Date]
)
```

Cumulative sum from first day of month through the selected date. If user filters to January 15, sums January 1–15.

Under the hood equivalent:

```dax
CALCULATE(
    SUM('RetailSalesTransactions'[NetAmount]),
    DATESMTD('dateTable'[Date])
)
```

### TOTALYTD — Year-to-Date

```dax
MEASURE [YTD Sales] =
TOTALYTD(
    SUM('RetailSalesTransactions'[NetAmount]),
    'dateTable'[Date]
)
```

Cumulative sum from January 1 through the selected date.

## YoY Comparison

### SAMEPERIODLASTYEAR

```dax
MEASURE [YOY Sales] =
CALCULATE(
    [Total Sales],
    ALL('dateTable'[Date]),
    SAMEPERIODLASTYEAR('dateTable'[Date])
)
```

1. `ALL` removes the current date filter
2. `SAMEPERIODLASTYEAR` shifts the same period back one year
3. `Total Sales` is calculated for the prior-year period

For 15 days into January 2024: returns the same 15 days of January 2023.

### DATESMTD / DATESYTD

Used inside CALCULATE as a filter argument:

```dax
CALCULATE(
    [Total Sales],
    DATESMTD('dateTable'[Date])
)
```

Same result as TOTALMTD — preferred for composability inside CALCULATE.

## Date Range Selection

### MAXX + ALLSELECTED — Latest Slicer Date

```dax
MAXX(
    ALLSELECTED(dateTable),
    dateTable[Date]
)
```

Finds the maximum date currently selected by the user's slicer. Used to retrieve the correct budget row when budgets are stored at month level.

### DATESBETWEEN — Dynamic Date Range

```dax
DATESBETWEEN(
    'dateTable'[Date],
    MINX(ALLSELECTED(dateTable), dateTable[Date]),   -- dynamic start
    MAXX(ALLSELECTED(dateTable), dateTable[Date])    -- dynamic end
)
```

Creates a date set from the slicer start to slicer end. Updates automatically when the user changes the slicer.

## Related

- [[SAMEPERIODLASTYEAR-YoY-Pattern]] — YoY calculation with SAMEPERIODLASTYEAR + ALL
- [[ALL-vs-ALLSELECTED]] — ALL ignores all filters; ALLSELECTED respects current slicer context
- [[DATESBETWEEN-Dynamic-Date-Ranges]] — dynamic date filtering that adapts to user slicer
- [[Inventory-Aging-Buckets-Pattern]] — inventory aging using CALCULATE + AgeInWeeks column
