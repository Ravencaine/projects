---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [dax, pattern, highlight, fill-rate, staffing]
---

# Lowest Fill Rate Highlight

A formatted text string identifying the unit with the lowest shift fill rate this week, with shift-level attribution for the staffing gap.

## Purpose

Staffing gaps directly impact patient care. This measure flags the unit with the lowest fill rate (filled shifts / scheduled shifts) and explains whether the understaffing is concentrated in a specific shift or distributed across the schedule.

## Components

1. `SUMMARIZE(VALUES(Scheduling Data[Unit]), ...)` + `ADDCOLUMNS` — per-unit fill rate in the 7-day window
2. `MINX` — finds the lowest fill rate value
3. `MAXX(TOPN(1, ..., ASC))` — retrieves the unit name for the lowest rate
4. Two-layer shift attribution: scheduled/filled → unfilled count → share
5. `SWITCH(TRUE(), ...)` with 60% share threshold
6. `ISBLANK` guard

## Structure

```dax
Lowest Fill Rate Highlight =
VAR _lastDate  = [Max Date]
VAR _weekStart = [Max Date - 7]

VAR _UnitFill = ADDCOLUMNS(
    SUMMARIZE(VALUES('Scheduling Data'[Unit]), 'Scheduling Data'[Unit]),
    "FillRate", CALCULATE(
        DIVIDE(SUM('Scheduling Data'[Filled]), SUM('Scheduling Data'[Scheduled])),
        'Scheduling Data'[Date] > _weekStart,
        'Scheduling Data'[Date] <= _lastDate
    )
)
VAR _lowestRate = MINX(_UnitFill, [FillRate])
VAR _dept = MAXX(TOPN(1, _UnitFill, [FillRate], ASC), [Unit])

VAR _ShiftFillTbl2 = ADDCOLUMNS(
    ADDCOLUMNS(ALL('Scheduling Data'[Shift]),
        "Sched", CALCULATE(SUM('Scheduling Data'[Scheduled]),
            KEEPFILTERS('Scheduling Data'[Unit] = _dept),
            'Scheduling Data'[Date] > _weekStart, 'Scheduling Data'[Date] <= _lastDate),
        "Filled", CALCULATE(SUM('Scheduling Data'[Filled]),
            KEEPFILTERS('Scheduling Data'[Unit] = _dept),
            'Scheduling Data'[Date] > _weekStart, 'Scheduling Data'[Date] <= _lastDate)
    ),
    "Unfilled", MAX(0, [Sched] - [Filled]),
    "FillRateShift", DIVIDE([Filled], [Sched])
)

VAR _UnitUnfilledTotal = SUMX(_ShiftFillTbl2, [Unfilled])
VAR _TopShiftUnf = MAXX(_ShiftFillTbl2, [Unfilled])
VAR _TopShiftName = MAXX(TOPN(1, _ShiftFillTbl2, [Unfilled], DESC), 'Scheduling Data'[Shift])
VAR _TopShiftRate = MAXX(FILTER(_ShiftFillTbl2, 'Scheduling Data'[Shift] = _TopShiftName), [FillRateShift])
VAR _Share = DIVIDE(_TopShiftUnf, _UnitUnfilledTotal)

VAR _ShiftDetail = SWITCH(TRUE(),
    _UnitUnfilledTotal > 0 && _Share >= 0.6,
        " — mainly on " & _TopShiftName & " (fill " & FORMAT(_TopShiftRate,"0.0%") & ", " & FORMAT(_TopShiftUnf,"#,##0") & " unfilled)",
    _UnitUnfilledTotal > 0 && _Share < 0.6,
        " — spread across shifts (lowest: " & _TopShiftName & " " & FORMAT(_TopShiftRate,"0.0%") & ", " & FORMAT(_TopShiftUnf,"#,##0") & " unfilled)",
    "")

RETURN
IF(ISBLANK(_lowestRate), BLANK(),
    "⚠️ Lowest filled rate: " & FORMAT(_lowestRate,"0.0%") & " in " & _dept & _ShiftDetail)
```

## Example Output

```
⚠️ Lowest filled rate: 71.2% in Pediatrics — mainly on Night (fill 58.3%, 18 unfilled)
```

## Key Pattern Notes

- `_ShiftFillTbl2` uses a double ADDCOLUMNS: first adds Sched and Filled, then adds Unfilled and FillRateShift as derived columns
- `MAX(0, [Sched] - [Filled])` prevents negative unfilled counts from rounding errors
- `TOPN(1, ..., ASC)` finds the unit with the lowest fill rate; `TOPN(1, ..., DESC)` finds the shift with the most unfilled slots

## Related

- [[Top-Unit-Highlight]]
- [[Max-Date-Pattern-Rolling-Window]]
