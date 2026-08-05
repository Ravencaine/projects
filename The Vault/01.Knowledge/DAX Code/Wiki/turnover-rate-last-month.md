---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, measure, turnover, rate, rolling]
---

# Turnover Rate Last Month

The rolling 12-month employee turnover rate for the period ending one month before the current context's max date.

## Signature

```dax
Turnover Rate Last Month =
VAR _LastMonthDate = EOMONTH([Max Date], -1)
VAR _12MWindow = DATESINPERIOD('Turnover Data'[Date], _LastMonthDate, -12, MONTH)
RETURN
    DIVIDE(
        CALCULATE([Leavers], _12MWindow),
        CALCULATE([Headcount], _12MWindow)
    )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `_LastMonthDate` | scalar | Last day of the month before the current max date |
| `_12MWindow` | table | 12-month date period ending at `_LastMonthDate` |

## Returns

A decimal — the turnover rate for the prior 12-month period.

## Notes

`EOMONTH(Date, -1)` returns the last day of the month that is one month before `Date`. If today is 2025-09-15, `EOMONTH(2025-09-15, -1)` = 2025-08-31. The DATESINPERIOD then generates the 12-month window ending on that date.

## Related

- [[Turnover-Rate]]
- [[Turnover-Rate-Variance]]
- [[DATESINPERIOD-Rolling-12-Month-Window]]
