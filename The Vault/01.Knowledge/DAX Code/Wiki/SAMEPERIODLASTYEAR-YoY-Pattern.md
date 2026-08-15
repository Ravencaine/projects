---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 2
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317
note_type: pattern
tags: [dax, year-over-year, time-intelligence, comparison]
---

# SAMEPERIODLASTYEAR YoY Pattern

Use `CALCULATE` + `ALL` + `SAMEPERIODLASTYEAR` to compare the current filtered period to the same period one year prior. Shifts the date filter back exactly one year while preserving the period shape (days → days, months → months).

## Pattern

```dax
MEASURE [YOY Sales] =
CALCULATE(
    [Total Sales],                     -- 1. measure to evaluate
    ALL('dateTable'[Date]),            -- 2. remove current date filter
    SAMEPERIODLASTYEAR('dateTable'[Date])  -- 3. apply prior-year dates
)
```

## How It Works

| Step | Function | Purpose |
|------|---------|---------|
| 1 | `[Total Sales]` | Base measure — evaluated in the new context |
| 2 | `ALL('dateTable'[Date])` | Clears the current date filter from the context |
| 3 | `SAMEPERIODLASTYEAR(...)` | Applies the equivalent dates shifted back one year |

## Period Shape Preservation

`SAMEPERIODLASTYEAR` preserves the shape of the filtered period:

| Current Selection | Prior-Year Result |
|------------------|-------------------|
| January 1–15 | January 1–15 (prior year) |
| Q1 2024 | Q1 2023 |
| Full year | Full year |

This matters: you want the same days/weeks/months compared, not a full calendar year offset.

## Combining with Variance

```dax
MEASURE [YOY %] =
VAR yoy_sales =
    CALCULATE(
        [Total Sales],
        ALL('dateTable'[Date]),
        SAMEPERIODLASTYEAR('dateTable'[Date])
    )
RETURN
    IF(
        ISBLANK(yoy_sales),
        BLANK(),
        DIVIDE([Total Sales], yoy_sales) - 1
    )
```

## Alternative: Same-Period-Last-Year (SPLY)

```dax
-- Identical result, different naming convention
MEASURE [Total Sales SPLY] =
CALCULATE(
    SUM('RetailSalesTransactions'[NetAmount]),
    ALL('dateTable'[Date]),
    SAMEPERIODLASTYEAR('dateTable'[Date])
)
```

## Related

- [[Time-Intelligence-Functions-Reference]] — full time intelligence reference including TOTALMTD, TOTALYTD
- [[Conditional-Variance-Display-Hide-Minus-100]] — variance pattern with ISBLANK guard
