---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: pattern
tags: [powerbi, dax, scatter-chart, tooltip, dynamic-measure, switch]
---

# Scatter Tooltip X/Y Value Measures

A set of DAX measures that dynamically map the variables selected in the correlation matrix rows/columns to their numeric values, enabling a scatter chart on a tooltip page.

## Supporting Measures

```c
Selected X Name = SELECTEDVALUE ( VariablesX[Variable] )

Selected Y Name = SELECTEDVALUE ( VariablesY[Variable] )
```

## X Value Measure

```c
X Value =
VAR _name = [Selected X Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",           MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",     MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",         MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",      MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",             MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",   MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)
```

## Y Value Measure

```c
Y Value =
VAR _name = [Selected Y Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",           MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",     MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",         MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",      MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",             MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",   MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)
```

## Scatter Chart Configuration

| Axis | Field |
|------|-------|
| X-Axis | `X Value` |
| Y-Axis | `Y Value` |
| Details / Legend | `Employee ID` from 'HR Data' |

## Tooltip Page Setup

1. Add a new report page → set **Page Type** to **Tooltip** in page settings.
2. Resize to ~400px × 500px (compact).
3. Add the scatter chart with the above configuration.
4. Enable **Trend line** under the **Analysis** pane.
5. Assign this page as the tooltip page for the correlation matrix visual.

## Title Measure

```c
Scatter Title = [Selected X Name] & " vs " & [Selected Y Name]
```

## Notes

- These measures use the same SWITCH pattern as `[[pearson-correlation-measure]]` but output the raw values instead of the correlation coefficient.
- Both X Value and Y Value must be placed on a visual context that iterates over individual employees (e.g., a scatter chart with Employee ID as Details).

## Related

- [[pearson-correlation-measure]]
- [[variablesx-variablesy-tables]]
