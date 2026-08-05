---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, overtime, rolling-window, week]
---

# OT Hours This Week

Total overtime hours in the most recent 7-day window (absolute, not per FTE).

## Signature

```dax
OT Hours This Week =
VAR _MaxDate = [Max Date]
VAR _MinDate = [Max Date - 7]
VAR _OTHours =
    CALCULATE(
        [OT Hours],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] <= _MaxDate &&
            'Scheduling Data'[Date] > _MinDate
        )
    )
RETURN _OTHours
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `_MaxDate` | scalar | Latest date in current context |
| `_MinDate` | scalar | `_MaxDate - 7` |

## Returns

A number — total OT hours in the last 7 days.

## Notes

Unlike `OT Hours per FTE This Week`, this returns the raw total. It is used in the Dynamic Chart SWITCH as the Column Value for highlight order = 3 (Top Unit Highlight), where the absolute hour count drives the bar chart showing which unit has the highest OT.

## Related

- [[OT-Hours]]
- [[Max-Date-Pattern-Rolling-Window]]
- [[Top-Unit-Highlight]]
