---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, measure, turnover, rate, rolling]
---

# Turnover Rate

The rolling 12-month employee turnover rate (leavers / headcount) for the period ending at the current context's max date.

## Signature

```dax
Turnover Rate =
VAR _CurrentDate = [Max Date]
VAR _12MWindow = DATESINPERIOD('Turnover Data'[Date], _CurrentDate, -12, MONTH)
RETURN
    DIVIDE(
        CALCULATE([Leavers], _12MWindow),
        CALCULATE([Headcount], _12MWindow)
    )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `_CurrentDate` | scalar | Max date in current filter context |
| `_12MWindow` | table | 12-month date period ending at `_CurrentDate` |

## Returns

A decimal — the turnover rate (0.12 = 12%). Returned as a raw decimal; format as percentage in the visual.

## Notes

`CALCULATE` is applied to the numerator and denominator separately within the same `_12MWindow` context. This ensures both the leavers count and the headcount reference are filtered to the same 12-month window. `DIVIDE` handles zero headcount safely.

## Related

- [[Turnover-Rate-Last-Month]]
- [[Turnover-Rate-Variance]]
- [[DATESINPERIOD-Rolling-12-Month-Window]]
