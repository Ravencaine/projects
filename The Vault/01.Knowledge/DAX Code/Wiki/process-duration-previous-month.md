---
created: 2026-08-02
updated: 2026-08-05
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, filter, calculate]
---

# Process Duration Previous Month

Returns the sum of process duration days for the prior period (one month before maximum date).

```dax
Process Duration Previous Month =
VAR _DateLastMonth = [Date Last Month]
VAR _Duration =
    CALCULATE(
        SUM('Process Duration'[Days]),
        FILTER(
            'Process Duration',
            'Process Duration'[Date] = _DateLastMonth
        )
    )
RETURN _Duration
```

## Pattern

Same structure as [[process-duration.md]] but substitutes `_DateLastMonth` as the filter anchor — demonstrating the measure branching pattern: a shared anchor measure (`Date Last Month`) used by multiple downstream measures.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
