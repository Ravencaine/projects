---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Where Everything You've Learned About Context Finally Pays Off
source_url: https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
note_type: reference
tags: [dax, time-intelligence, dateadd, sameperiodlastyear, parallelperiod, period-comparison]
---

# Time Shift Functions: DATEADD vs SAMEPERIODLASTYEAR vs PARALLELPERIOD

Three functions that shift the date context backward or forward in time. The choice depends on whether you need a literal shift or complete periods.

## DATEADD — Literal Shift by Any Interval

```dax
Sales LY =
CALCULATE(
    SUM(Sales[Amount]),
    DATEADD(Dates[Date], -1, YEAR)
)
```

Returns a table of dates shifted by the specified interval from the current context. `-1 YEAR` gives the same dates one year earlier, regardless of what the current period is.

- **Intervals:** `DAY`, `MONTH`, `QUARTER`, `YEAR`
- **Use negative** for past, **positive** for future
- Most flexible: can shift by any interval in any direction
- `DATEADD(Dates[Date], -1, MONTH)` and `DATEADD(Dates[Date], -1, QUARTER)` are both valid

## SAMEPERIODLASTYEAR — Readable YoY Intent

```dax
Sales SPLY =
CALCULATE(
    SUM(Sales[Amount]),
    SAMEPERIODLASTYEAR(Dates[Date])
)
```

Returns exactly the same dates from one year prior. Self-documenting: anyone reading the measure immediately knows it's a YoY comparison.

- Returns the same result as `DATEADD(Dates[Date], -1, YEAR)` in most cases
- Use when the measure is specifically a YoY comparison — readability wins
- Use `DATEADD` when you need flexibility (month or quarter shifts)

## PARALLELPERIOD — Complete Periods Only

```dax
Sales Prior Quarter =
CALCULATE(
    SUM(Sales[Amount]),
    PARALLELPERIOD(Dates[Date], -1, QUARTER)
)
```

Returns the **full prior period** snapped to period boundaries. Unlike DATEADD, it always returns complete periods.

**The critical difference:** If the current context is mid-March (Jan 1 – Mar 15):
- `DATEADD(..., -1, QUARTER)` → Oct 1 to Dec 15 (partial prior quarter)
- `PARALLELPERIOD(..., -1, QUARTER)` → Oct 1 to Dec 31 (complete prior quarter)

Use when you want clean, complete-period benchmarks. Use DATEADD for literal shifts of whatever window is selected.

## Quick Decision Guide

| Situation | Use |
|-----------|-----|
| Shift by 1 year, readability matters | `SAMEPERIODLASTYEAR` |
| Shift by months or quarters | `DATEADD` |
| Need complete prior period (not partial) | `PARALLELPERIOD` |
| Literal shift of whatever is selected | `DATEADD` |

## Related

- [[Date-Table-Must-Be-Marked-Requirement]] — prerequisite: marked Date table required
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — the conceptual model: all time functions are CALCULATE with a date table filter
