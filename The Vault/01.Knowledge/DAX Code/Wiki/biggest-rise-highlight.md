---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [dax, pattern, variance, highlight, unit]
---

# Biggest Rise Highlight

A formatted text string identifying the unit with the largest week-over-week OT/FTE variance, with optional shift-level attribution.

## Purpose

This highlight surfaces emerging operational problems — a unit whose OT is rising fastest — before it escalates. The shift attribution logic (via `_ShiftDetail`) tells leaders whether the increase is concentrated in a single shift or distributed across the board.

## Components

1. `MAXX(ALL(Units[Unit]), [OT Hours per FTE Variance %])` — finds unit with highest variance
2. `FILTER + FIRSTNONBLANK` — retrieves the unit name at that variance
3. Per-shift variance table via `ADDCOLUMNS(ALL(Scheduling Data[Shift]), ...)` with `KEEPFILTERS`
4. Shift attribution logic via `SWITCH(TRUE(), ...)` with 60% share threshold
5. `FORMAT` for signed percentage display (`"+0.0%"`)

## Structure

```dax
Biggest Rise Highlight =
VAR _MaxVariance = MAXX(ALL(Units[Unit]), [OT Hours per FTE Variance %])
VAR _MaxUnit = CALCULATE(FIRSTNONBLANK(Units[Unit],1),
              FILTER(ALL(Units[Unit]), [OT Hours per FTE Variance %] = _MaxVariance))
VAR _ShiftVarTbl = ADDCOLUMNS(ALL('Scheduling Data'[Shift]),
              "VarPct", CALCULATE([OT Hours per FTE Variance %],
              KEEPFILTERS(Units[Unit] = _MaxUnit)))
VAR _TopShiftVar = MAXX(_ShiftVarTbl, [VarPct])
VAR _TopShiftName = MAXX(TOPN(1, _ShiftVarTbl, [VarPct], DESC), 'Scheduling Data'[Shift])
VAR _ShiftShare = DIVIDE(_TopShiftVar, _MaxVariance)
VAR _ShiftDetail = SWITCH(TRUE(),
    NOT ISBLANK(_TopShiftVar) && _TopShiftVar > 0 && _ShiftShare >= 0.6,
        " — mainly on " & _TopShiftName & " (" & FORMAT(_TopShiftVar,"+0.0%") & ")",
    NOT ISBLANK(_TopShiftVar) && _TopShiftVar > 0 && _ShiftShare < 0.6,
        " — spread across shifts (top: " & _TopShiftName & " " & FORMAT(_TopShiftVar,"+0.0%") & ")",
    "")
RETURN
"🔺 Biggest rise in OT/FTE: " & _MaxUnit & " " & FORMAT(_MaxVariance,"+0.0%") & _ShiftDetail
```

## Example Output

```
🔺 Biggest rise in OT/FTE: ICU +18.5% — mainly on Night (+12.1%)
```

## Variations

- Drop the shift attribution entirely for simpler output
- Use a configurable threshold (e.g. 60%) as a measure instead of a hard-coded value
- Swap the emoji prefix to a different Unicode character based on variance direction

## Related

- [[OT-Hours-per-FTE-Variance-Pct]]
- [[High-OT-Flag-Highlight]]
- [[Top-Unit-Highlight]]
