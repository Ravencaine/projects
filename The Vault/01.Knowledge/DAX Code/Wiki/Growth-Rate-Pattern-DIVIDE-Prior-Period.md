---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Year-to-Date, Rolling Averages, and Comparisons
source_url: https://medium.com/@saketsis/dax-time-intelligence-year-to-date-rolling-averages-and-comparisons-6a120ccef282
note_type: pattern
tags: [dax, time-intelligence, growth-rate, divide, mom, qoq, yoy, prior-period, period-comparison]
---

# Growth Rate Pattern: DIVIDE + CALCULATE + Time Shift

Growth rate calculations follow a consistent structure: `(current − prior) / prior`. In DAX this means `DIVIDE(CALCULATE + current, CALCULATE + prior period)`. The time shift function defines which prior period to compare.

## The Universal Template

```dax
<Metric> Growth =
DIVIDE(
    [Current Measure]
        - CALCULATE([Current Measure], <time shift>),
    CALCULATE([Current Measure], <time shift>)
)
```

`DIVIDE` is safe against division-by-zero (returns blank instead of error).

## Month-over-Month (MoM)

```dax
Sales MoM Growth =
DIVIDE(
    [Total Sales]
        - CALCULATE([Total Sales], DATEADD('Date'[Date], -1, MONTH)),
    CALCULATE([Total Sales], DATEADD('Date'[Date], -1, MONTH))
)
```

Positive result = growth. Negative result = decline.

## Quarter-over-Quarter (QoQ)

```dax
Sales QoQ Growth =
DIVIDE(
    [Total Sales]
        - CALCULATE([Total Sales], DATEADD('Date'[Date], -1, QUARTER)),
    CALCULATE([Total Sales], DATEADD('Date'[Date], -1, QUARTER))
)
```

## Year-over-Year (YoY)

```dax
Sales YoY Growth =
DIVIDE(
    [Total Sales]
        - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date])),
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
)
```

Note: `SAMEPERIODLASTYEAR` is readable for YoY specifically; `DATEADD(..., -1, YEAR)` is equivalent but less self-documenting.

## Best Practices

1. **Build a base measure first:** define `[Total Sales]` as `SUM(Sales[Amount])` separately, then build growth on top
2. **Always use DIVIDE:** handles blank/zero denominator gracefully
3. **Choose the right time shift**:
   - `DATEADD(..., -1, MONTH)` for MoM (flexible to other periods too)
   - `DATEADD(..., -1, QUARTER)` for QoQ
   - `SAMEPERIODLASTYEAR` for YoY
4. **Test with slicers:** ensure the prior period shifts correctly when the user filters dates

## Related

- [[Time-Shift-Functions-DATEADD-SAMEPERIODLASTYEAR-PARALLELPERIOD]] — DATEADD and SAMEPERIODLASTYEAR comparison
- [[Date-Table-Must-Be-Marked-Requirement]] — prerequisite for all time shift functions
