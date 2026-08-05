---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: atomic
tags: [dax, pattern, date-filter, rolling-window]
---

# Max Date Pattern (Rolling 7-Day Window)

Using `MAX(DateColumn)` as the dynamic anchor point for a rolling N-day window, then deriving the window start as `[Max Date] - N`.

## Definition

`Max Date` captures the most recent date present in the current filter context — it is the right boundary of the rolling window. The left boundary is `[Max Date] - 7`. Both are measures (not calculated columns), so they recompute with every refresh and respond to any slicer or filter context.

## Key Points

- `MAX(DateColumn)` is the foundation — all subsequent date math depends on it
- Subtracting N from `Max Date` gives the window start: `Max Date - 7` (inclusive lower bound, exclusive upper bound in FILTER logic)
- Using `>` on the lower bound and `<=` on the upper bound ensures a clean 7-day window: `Date > _MinDate && Date <= _MaxDate`
- The window is fully dynamic: on each refresh the latest date shifts forward automatically
- The pattern requires a Calendar dimension table or a populated date column in the fact table

## Formula

```dax
Max Date = MAX('Scheduling Data'[Date])

Max Date - 7 = [Max Date] - 7

Last 7 Days Measure =
VAR _MaxDate = [Max Date]
VAR _MinDate = [Max Date - 7]
RETURN
    CALCULATE(
        [Base Metric],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] > _MinDate &&
            'Scheduling Data'[Date] <= _MaxDate
        )
    )
```

## Related

- [[OT-Hours-per-FTE-This-Week]]
- [[OT-Hours-per-FTE-Last-Week]]
