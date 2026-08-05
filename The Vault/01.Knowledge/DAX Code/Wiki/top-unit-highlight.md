---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [dax, pattern, highlight, overtime, unit]
---

# Top Unit Highlight

A formatted text string identifying the unit with the highest total OT hours this week, broken down by shift contribution.

## Purpose

Leaders need to know where overtime is concentrated. This measure finds the unit with the most OT hours in the current week and explains whether that is driven by a single shift or spread across the schedule.

## Components

1. `MAXX(ALL(Units), [OT Hours This Week])` — finds unit with highest OT total
2. `FILTER + FIRSTNONBLANK` — retrieves unit name
3. Per-shift OT table via `ADDCOLUMNS(ALL(Scheduling Data[Shift]), ...)` with `KEEPFILTERS`
4. Shift attribution with 60% share threshold via `SWITCH(TRUE(), ...)`
5. `FORMAT` for comma-separated hour display (`"#,##0"`)
6. `ISBLANK` guard — returns BLANK if no data

## Structure

```dax
Top Unit Highlight =
VAR _MaxOT = MAXX(ALL(Units), [OT Hours This Week])
VAR _MaxUnit = CALCULATE(FIRSTNONBLANK(Units[Unit],1),
              FILTER(ALL(Units[Unit]), [OT Hours This Week] = _MaxOT))
VAR _ShiftOTTbl = ADDCOLUMNS(ALL('Scheduling Data'[Shift]),
              "OT_Hours", CALCULATE([OT Hours This Week],
              KEEPFILTERS(Units[Unit] = _MaxUnit)))
VAR _TopShiftOT = MAXX(_ShiftOTTbl, [OT_Hours])
VAR _TopShiftName = MAXX(TOPN(1, _ShiftOTTbl, [OT_Hours], DESC), 'Scheduling Data'[Shift])
VAR _ShiftShare = DIVIDE(_TopShiftOT, _MaxOT)
VAR _ShiftDetail = SWITCH(TRUE(),
    NOT ISBLANK(_TopShiftOT) && _TopShiftOT > 0 && _ShiftShare >= 0.6,
        " — mainly on " & _TopShiftName & " (" & FORMAT(_TopShiftOT,"#,##0") & "h)",
    NOT ISBLANK(_TopShiftOT) && _TopShiftOT > 0 && _ShiftShare < 0.6,
        " — spread across shifts (top: " & _TopShiftName & " " & FORMAT(_TopShiftOT,"#,##0") & "h)",
    "")
RETURN
IF(ISBLANK(_MaxOT), BLANK(),
    "🏥 Top unit: " & _MaxUnit & " with " & FORMAT(_MaxOT,"#,##0") & "h" & _ShiftDetail)
```

## Example Output

```
🏥 Top unit: ER with 342h — mainly on Night (228h)
```

## Related

- [[OT-Hours-This-Week]]
- [[Biggest-Rise-Highlight]]
- [[Lowest-Fill-Rate-Highlight]]
