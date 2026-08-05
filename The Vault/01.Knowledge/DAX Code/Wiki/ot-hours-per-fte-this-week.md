---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, overtime, rolling-window, week]
---

# OT Hours per FTE This Week

OT Hours per FTE for the most recent 7-day window, anchored to `MAX(Date)`.

## Signature

```dax
OT Hours per FTE This Week =
VAR _MaxDate = [Max Date]
VAR _MinDate = [Max Date - 7]
VAR _OTHoursperFTE =
    CALCULATE(
        [OT Hours per FTE],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] <= _MaxDate &&
            'Scheduling Data'[Date] > _MinDate
        )
    )
RETURN _OTHoursperFTE
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `_MaxDate` | scalar | Latest date in current context |
| `_MinDate` | scalar | `_MaxDate - 7` |

## Returns

A decimal number — overtime hours per FTE for the last 7 days.

## Notes

The window uses `>` on the lower bound and `<=` on the upper bound to capture exactly 7 days inclusive of today. `Max Date` is itself a measure referencing `MAX('Scheduling Data'[Date])`, so the window moves forward automatically on each data refresh.

## Related

- [[Max-Date-Pattern-Rolling-Window]]
- [[OT-Hours-per-FTE]]
- [[OT-Hours-per-FTE-Last-Week]]
- [[OT-Hours-per-FTE-Variance]]
