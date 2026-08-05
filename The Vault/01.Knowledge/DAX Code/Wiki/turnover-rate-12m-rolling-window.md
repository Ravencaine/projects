---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, turnover, rolling-window, datesinperiod, 12-month, hr, calculate]
---

# Turnover Rate (12M Rolling Window)

Calculates a rolling 12-month turnover rate using `DATESINPERIOD` anchored on the max visible date.

## Components

```c
Headcount = SUM('Turnover Data'[Headcount])
Leavers   = SUM('Turnover Data'[Leavers])
Max Date  = MAX('Turnover Data'[Date])
```

## Turnover Rate

```c
Turnover Rate =
VAR _CurrentDate = [Max Date]
VAR _12MWindow = DATESINPERIOD('Turnover Data'[Date], _CurrentDate, -12, MONTH)
RETURN
    DIVIDE(
        CALCULATE([Leavers],   _12MWindow),
        CALCULATE([Headcount], _12MWindow)
    )
```

## Prior Period (Last Month Anchor)

```c
Last Month Date = EOMONTH([Max Date], -1)

Turnover Rate Last Month =
VAR _LastMonthDate = [Last Month Date]
VAR _12MWindow = DATESINPERIOD('Turnover Data'[Date], _LastMonthDate, -12, MONTH)
RETURN
    DIVIDE(
        CALCULATE([Leavers],   _12MWindow),
        CALCULATE([Headcount], _12MWindow)
    )
```

## Variance

```c
Turnover Rate Variance = [Turnover Rate] - [Turnover Rate Last Month]
```

## Key Design Points

- `DATESINPERIOD(date_col, end_date, -12, MONTH)` — 12-month trailing window
- `EOMONTH(date, -1)` — last day of previous month for the parallel window
- `DIVIDE` handles zero-division safely
- Both measures are filter-aware: switching Department, Geography, Tenure Band keeps them accurate

## Related

- [[rolling-total-udf]] — rolling window UDF pattern
- [[datesinperiod]] — DAX time intelligence function
