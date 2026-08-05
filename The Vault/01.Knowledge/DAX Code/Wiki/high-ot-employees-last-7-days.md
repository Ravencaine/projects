---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, overtime, threshold, employee]
---

# High OT Employees (Last 7 Days)

Counts employees whose total overtime in the last 7 days exceeds a configurable threshold (default 10 hours).

## Signature

```dax
High OT Employees (Last 7 Days) =
VAR _MaxDate   = [Max Date]
VAR _MinDate   = [Max Date - 7]
VAR Threshold  = COALESCE([High OT Flag Hours], 10)
RETURN
    COUNTROWS(
        FILTER(
            ADDCOLUMNS(
                SUMMARIZE(
                    FILTER(
                        'Scheduling Data',
                        'Scheduling Data'[Date] > _MinDate &&
                        'Scheduling Data'[Date] <= _MaxDate
                    ),
                    'Scheduling Data'[EmployeeID]
                ),
                "OT7",
                    CALCULATE(
                        SUM('Scheduling Data'[OvertimeHours]),
                        'Scheduling Data'[Date] >= _MinDate,
                        'Scheduling Data'[Date] <= _MaxDate
                    )
            ),
            [OT7] > Threshold
        )
    )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `_MaxDate` | scalar | Latest date in context |
| `_MinDate` | scalar | `_MaxDate - 7` |
| `Threshold` | scalar | COALESCE of user-defined hours flag or default 10 |

## Returns

An integer — the number of employees over the OT threshold.

## Notes

`SUMMARIZE` groups rows by `EmployeeID` (one row per employee). `ADDCOLUMNS` adds a per-employee OT total. `FILTER` then keeps only those above threshold. `COUNTROWS` returns the count. This is a row-level aggregation inside a table expression — it cannot be expressed with a simple `CALCULATE` filter.

The pattern `ADDCOLUMNS(SUMMARIZE(...))` is the standard approach for per-group threshold filtering in DAX.

## Related

- [[High-OT-Flag-Highlight]]
- [[Max-Date-Pattern-Rolling-Window]]
