---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Year-to-Date, Rolling Averages, and Comparisons
source_url: https://medium.com/@saketsis/dax-time-intelligence-year-to-date-rolling-averages-and-comparisons-6a120ccef282
note_type: gotcha
tags: [dax, time-intelligence, ytd, cumulative-total, pitfall, reset, wrong-metric]
---

# YTD Is Not the Same as a Cumulative Total — They Reset Differently

YTD and cumulative totals are often confused but behave differently: **YTD resets at the start of each year; a running cumulative total does not**.

## YTD: Resets Each Year

```dax
Revenue YTD = TOTALYTD(SUM(Sales[Revenue]), 'Date'[Date])
```

`TOTALYTD` starts accumulating from January 1 (or the fiscal year start if a fiscal end is specified) and **resets to zero on January 1 of the next year**.

In a multi-year visual, each year shows its own YTD accumulation independently.

## Cumulative Total: No Reset

```dax
Revenue Cumulative =
CALCULATE(
    SUM(Sales[Revenue]),
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
    )
)
```

A cumulative total without a year filter accumulates from the first date in the table to the current date — it does **not** reset annually.

## When This Matters

- **Multi-year dashboards**: YTD on a 3-year line chart shows 3 separate rising-then-falling lines (reset each January). A cumulative total shows a single monotonically increasing line.
- **Fiscal year reporting**: If the fiscal year doesn't align with the calendar year, YTD with the fiscal end parameter is correct; a naive cumulative total will give wrong totals.
- **Starting mid-year**: A model with data starting July 2023 — YTD in January 2024 correctly returns 0 (new year). A cumulative total would show all historical data under January 2024's row.

## Rule

> If your visual spans multiple years and should show continuously growing totals, use a cumulative total measure, not YTD.

## Related

- [[Running-Total-Functions-TOTALMTD-TOTALQTD-TOTALYTD]] — TOTALYTD as a YTD-specific cumulative; fiscal year parameter
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — the conceptual model behind YTD functions
