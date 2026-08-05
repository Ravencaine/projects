---
created: 2026-08-02
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: atomic
tags: [dax, pattern, datesinperiod, rolling-window, date-filter]
---

# DATESINPERIOD Rolling 12-Month Window

Using `DATESINPERIOD` to generate a date table filter for a rolling N-month window, combined with `CALCULATE` to apply it to a metric.

## Definition

`DATESINPERIOD(DateColumn, StartDate, Number, Interval)` returns a table of dates spanning `Number` intervals backward (or forward) from `StartDate`. Passed as a filter argument to `CALCULATE`, it applies a rolling window filter to any metric.

## Key Points

- `DATESINPERIOD` uses an anchor date as the start point — unlike the Max Date pattern which uses the latest date in context
- Negative `Number` gives a trailing window: `DATESINPERIOD(Date, _Anchor, -12, MONTH)` = 12 months ending at `_Anchor`
- `EOMONTH(Date, -1)` is the canonical way to step back one month and land on the last day — giving the prior period window for comparison
- The pattern `CALCULATE(metric, DATESINPERIOD(...))` wraps the metric expression, not the other way around

## Formula

```dax
// Rolling 12-month turnover rate
VAR _CurrentDate = [Max Date]
VAR _12MWindow = DATESINPERIOD('Turnover Data'[Date], _CurrentDate, -12, MONTH)
RETURN
    DIVIDE(
        CALCULATE([Leavers], _12MWindow),
        CALCULATE([Headcount], _12MWindow)
    )

// Prior period (12 months ending last month)
VAR _LastMonthDate = EOMONTH([Max Date], -1)
VAR _12MWindow = DATESINPERIOD('Turnover Data'[Date], _LastMonthDate, -12, MONTH)
RETURN
    DIVIDE(
        CALCULATE([Leavers], _12MWindow),
        CALCULATE([Headcount], _12MWindow)
    )
```

## Comparison with Max Date Rolling Window

| | Max Date Pattern | DATESINPERIOD Pattern |
|--|--|--|
| Anchor | `MAX(DateColumn)` — latest date in context | Explicit `StartDate` argument |
| Direction | Fixed (`Date > _MinDate && Date <= _MaxDate`) | Controlled by sign of `Number` |
| Flexibility | Very flexible — any N-day window | Best for month/quarter/year alignment |
| Use case | Operational metrics (OT, staffing) | HR/finance rolling rates (turnover, attrition) |

## Related

- [[Max-Date-Pattern-Rolling-Window]]
- [[Turnover-Rate]]
- [[Turnover-Rate-Last-Month]]
