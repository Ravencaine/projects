---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, time-intelligence, beginner, ytd, mtd, qtd, previous-year, growth]
---

# Time Intelligence Functions

Time intelligence is where DAX delivers the most business value — comparing periods, calculating YTD totals, and tracking growth rates.

## Prerequisite: A Proper Date Table

All time intelligence functions require a dedicated Date dimension table with:
1. Continuous dates (no gaps — every single day)
2. Marked as a Date table in Power BI (Table Tools → Mark as Date Table)
3. One active relationship to the fact table

```dax
Date =
ADDCOLUMNS(
    CALENDAR(DATE(2023, 1, 1), DATE(2025, 12, 31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "YearMonth", FORMAT([Date], "YYYY-MM")
)
```

## Year-to-Date (YTD)

```dax
Revenue YTD =
TOTALYTD(
    [Total Revenue],
    Date[Date]
)
```

Accumulates from January 1 to the current date context. If viewing September 15, shows Jan 1 through Sep 15.

## Month-to-Date (MTD)

```dax
Revenue MTD =
TOTALMTD(
    [Total Revenue],
    Date[Date]
)
```

Accumulates from the 1st of the current month to the current date context.

## Quarter-to-Date (QTD)

```dax
Revenue QTD =
TOTALQTD(
    [Total Revenue],
    Date[Date]
)
```

Accumulates from the 1st of the current quarter.

## Previous Year Same Period

```dax
Revenue PY =
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(Date[Date])
)
```

Returns the same dates shifted back one year. If viewing September 2017, returns September 2016.

## Year-over-Year Growth

```dax
Revenue Growth % =
VAR CurrentRevenue = [Total Revenue]
VAR PreviousRevenue = [Revenue PY]
RETURN
    DIVIDE(
        CurrentRevenue - PreviousRevenue,
        PreviousRevenue,
        0
    )
```

VAR stores intermediate results. DIVIDE handles the division safely.

## Previous Month

```dax
Revenue Previous Month =
CALCULATE(
    [Total Revenue],
    PREVIOUSMONTH(Date[Date])
)
```

Returns the entire previous month's revenue.

## Month-over-Month Growth

```dax
Revenue MoM Growth % =
VAR Current = [Total Revenue]
VAR Previous = [Revenue Previous Month]
RETURN
    DIVIDE(Current - Previous, Previous, 0)
```

## Rolling 12 Months

```dax
Revenue L12M =
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(
        Date[Date],
        LASTDATE(Date[Date]),
        -12,
        MONTH
    )
)
```

Last 12 calendar months ending at the last visible date — not a calendar YTD.

## Fiscal Year Handling

If your fiscal year doesn't start January 1:

```dax
Revenue Fiscal YTD =
TOTALYTD(
    [Total Revenue],
    Date[Date],
    "3/31"   // Fiscal year ends March 31
)
```

The third parameter specifies the fiscal year end date.

## Related

- [[calculate-context-modifier]] — CALCULATE is the engine behind time intelligence
- [[time-intelligence-common-mistakes]] — three mistakes that break time intelligence
- [[row-context-vs-filter-context]] — time filters work by modifying filter context
