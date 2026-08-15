---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Year-to-Date, Rolling Averages, and Comparisons
source_url: https://medium.com/@saketsis/dax-time-intelligence-year-to-date-rolling-averages-and-comparisons-6a120ccef282
note_type: pattern
tags: [dax, time-intelligence, rolling-average, averagex, datesinperiod, lastdate, trend, smoothing]
---

# Rolling Average: AVERAGEX + DATESINPERIOD

Rolling averages smooth seasonal fluctuations and one-time spikes, revealing the underlying trend. The pattern uses `AVERAGEX` to iterate over a date window returned by `DATESINPERIOD`.

## 3-Month Rolling Average

```dax
Sales 3M Rolling Avg =
AVERAGEX(
    DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -3, MONTH),
    [Total Sales]
)
```

**How it works:**
- `DATESINPERIOD` builds a 3-month window ending at the current date (`LASTDATE`)
- `AVERAGEX` iterates over each date in that window and computes `[Total Sales]`, then averages the results

## Key Distinction: Rolling Average vs Rolling Total

| Measure | Function | What it shows |
|---------|----------|--------------|
| Rolling total | `CALCULATE + SUM + DATESINPERIOD` | Sum of values in the window |
| Rolling average | `AVERAGEX + DATESINPERIOD` | Average of values in the window |

Rolling averages are better for: expense trends, count-based metrics, noisy data. Rolling totals are better for: revenue, volumes, cumulative goals.

## Common Window Sizes

```dax
-- 6-month rolling average
AVERAGEX(
    DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -6, MONTH),
    [Total Sales]
)

-- 12-month rolling average (TTM)
AVERAGEX(
    DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -12, MONTH),
    [Total Sales]
)

-- 7-day rolling average
AVERAGEX(
    DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -7, DAY),
    [Total Sales]
)
```

## Use Case: Avoiding Overreaction to One Bad Month

A sales director reviewing monthly performance uses the rolling average to avoid reacting to a single sharp dip. The rolling average shows whether the dip is part of a broader declining trend or an isolated event.

## Related

- [[Rolling-Window-Functions-DATESINPERIOD]] — DATESINPERIOD + LASTDATE anchoring (sum-based); this note covers the average variant
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — the conceptual model: DATESINPERIOD is a date table passed as a CALCULATE filter
- [[Date-Table-Must-Be-Marked-Requirement]] — prerequisite
