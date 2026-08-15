---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Where Everything You've Learned About Context Finally Pays Off
source_url: https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
note_type: reference
tags: [dax, time-intelligence, datesinperiod, lastdate, rolling-window, trailing, moving-average]
---

# Rolling Window Functions: DATESINPERIOD + LASTDATE

`DATESINPERIOD` returns a sliding window of dates ending or starting at a given anchor point. Combined with `LASTDATE`, it produces rolling trailing windows that slide with the current date context.

## DATESINPERIOD — Sliding Date Window

```dax
DATESINPERIOD(<dates>, <start/end date>, <number>, <interval>)
```

Returns a table of dates for a specified duration. Use a negative number to look backwards from the anchor, positive to look forward.

## Trailing 3-Month Rolling Total

```dax
Rolling 3 Month Sales =
CALCULATE(
    SUM(Sales[Amount]),
    DATESINPERIOD(
        Dates[Date],
        LASTDATE(Dates[Date]),  -- anchor: last date in current context
        -3,                      -- go back 3 periods
        MONTH                    -- by month
    )
)
```

`LASTDATE(Dates[Date])` returns the last date in the current filter context — the anchor point. `DATESINPERIOD` then builds a 3-month window ending at that date. As the user filters to different months, the window slides automatically.

## Other Common Uses

| Calculation | DATESINPERIOD config |
|-------------|---------------------|
| Rolling 7-day average | `DATESINPERIOD(Dates[Date], LASTDATE(Dates[Date]), -7, DAY)` |
| Trailing 12-month revenue | `DATESINPERIOD(Dates[Date], LASTDATE(Dates[Date]), -12, MONTH)` |
| 90-day customer activity | `DATESINPERIOD(Dates[Date], LASTDATE(Dates[Date]), -90, DAY)` |
| Forward 3-month forecast | `DATESINPERIOD(Dates[Date], LASTDATE(Dates[Date]), +3, MONTH)` |

## Why LASTDATE as Anchor

`LASTDATE` performs context transition: it evaluates the last date *within the current filter context*, not the absolute last date in the table. This means the rolling window always starts from whatever period the user has selected — powerful for "rolling N months from current selection" behavior.

For the absolute last date regardless of user filter, use `MAX(Dates[Date])` instead.

## Related

- [[Time-Shift-Functions-DATEADD-SAMEPERIODLASTYEAR-PARALLELPERIOD]] — shift functions vs rolling windows
- [[Endurance-Improvement-FIRSTDATE-LASTDATE-Pattern]] — LASTDATE also used for first/last boundary anchoring in progress metrics
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — conceptual model
