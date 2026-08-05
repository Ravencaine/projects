---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, filter, calculate]
---

# Process Duration (Current Month)

Returns the sum of process duration days for the current period (maximum date in the dataset).

```dax
Process Duration =
VAR _MaxDate = [Maximum Date]
VAR _Duration =
    CALCULATE(
        SUM('Process Duration'[Days]),
        FILTER(
            'Process Duration',
            'Process Duration'[Date] = _MaxDate
        )
    )
RETURN _Duration
```

## Pattern

`CALCULATE + FILTER` is used here to change the filter context — the FILTER overrides the existing date filter to isolate only the row matching `_MaxDate`, then SUM aggregates the Days column.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
