---
created: 2026-08-05
updated: 2026-08-05
source: Arrow Charts in Power BI Enhancing Data Visualization (Boniface Muchendu)
note_type: pattern
tags: [dax, period-over-period, current-period, previous-period, parallelperiod, arrow-chart]
---

# Period-over-Period DAX Measures for Arrow Charts

Three DAX measures needed to build an Arrow chart: current period value, previous period value, and percentage change.

## Measure 1: Current Period Value

```dax
Current Qtr Sales = SUM(Sales[Amount])
```

The base measure — total for the current selected period.

## Measure 2: Previous Period Value

```dax
Prev Qtr Sales =
CALCULATE(
    [Current Qtr Sales],
    PARALLELPERIOD(DimDate[Date], -1, QUARTER)
)
```

`PARALLELPERIOD` shifts the date context back by one quarter, so the measure automatically returns the same period in the previous quarter regardless of which quarter is selected.

Alternative using `SAMEPERIODLASTYEAR`:

```dax
-- Same quarter, previous year
Prev Qtr YoY =
CALCULATE(
    [Current Qtr Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)
```

## Measure 3: Percentage Change

```dax
% Change =
DIVIDE(
    [Current Qtr Sales] - [Prev Qtr Sales],
    [Prev Qtr Sales]
)
```

Returns a decimal (e.g., 0.15 for 15% increase). Format as percentage in Power BI.

## Measure 4: Arrow Series Measures (Positive/Negative Split)

```dax
Sales Positive =
IF(
    [Current Qtr Sales] > [Prev Qtr Sales],
    [Current Qtr Sales],
    BLANK()
)

Sales Negative =
IF(
    [Current Qtr Sales] < [Prev Qtr Sales],
    [Current Qtr Sales],
    BLANK()
)
```

These feed the conditional formatting on the line chart markers.

## Common Time Intelligence Variations

| Period shift | Function | Example |
|-------------|----------|---------|
| Previous quarter | `PARALLELPERIOD(..., -1, QUARTER)` | `PARALLELPERIOD(DimDate[Date], -1, QUARTER)` |
| Previous month | `PARALLELPERIOD(..., -1, MONTH)` | `PARALLELPERIOD(DimDate[Date], -1, MONTH)` |
| Same quarter, prior year | `SAMEPERIODLASTYEAR()` | `SAMEPERIODLASTYEAR(DimDate[Date])` |
| Same month, prior year | `SAMEPERIODLASTYEAR()` on monthly | On a monthly granularity |

## Period Dimension Note

The measures above assume a Date table (`DimDate`) with a relationship to the fact table. The time intelligence functions require a proper date column marked as a Date table.

## Related

- [[Arrow-Chart-Build-Line-Marker-ErrorBar]]
- [[Dual-Measure-Conditional-Formatting-Positive-Negative]]
