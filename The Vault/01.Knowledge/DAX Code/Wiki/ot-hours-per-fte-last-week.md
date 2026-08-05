---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, overtime, rolling-window, week]
---

# OT Hours per FTE Last Week

OT Hours per FTE for the 7-day period immediately before the most recent 7 days.

## Signature

```dax
OT Hours per FTE Last Week =
VAR _MaxDate = [Max Date - 7]
VAR _MinDate = [Max Date - 14]
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
| `_MaxDate` | scalar | `[Max Date - 7]` — the start of this week minus 1 |
| `_MinDate` | scalar | `[Max Date - 14]` — 14 days before today |

## Returns

A decimal number — overtime hours per FTE for the prior 7-day window.

## Notes

This measure is structurally identical to `OT Hours per FTE This Week` but uses a shifted date window. The two measures together enable week-over-week comparison. The variance is then `[This Week] - [Last Week]` and `[This Week] / [Last Week] - 1`.

## Related

- [[OT-Hours-per-FTE-This-Week]]
- [[OT-Hours-per-FTE-Variance]]
- [[OT-Hours-per-FTE-Variance-Pct]]
