---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, correlation, dynamic, switch, mapping, tooltip]
---

# X Value / Y Value — Dynamic Variable Mapping

Maps the currently selected variable name (from `Selected X Name` / `Selected Y Name`) to its numeric value from the data table. Used on a tooltip page to drive a scatter chart's X and Y axes.

## Signatures

```dax
X Value :=
VAR _name = [Selected X Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",           MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",     MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",         MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",      MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",               MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",      MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)

Y Value :=
VAR _name = [Selected Y Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",           MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",     MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",         MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",      MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",               MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",      MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Selected X Name]` / `[Selected Y Name]` | measure | Currently selected variable display name |
| Data table columns | any | `MAX()` of each numeric column in the underlying data table |

## Returns

A numeric value — the data point for the selected variable on a given row of the data table.

## Notes

- Both measures use identical `SWITCH(TRUE())` logic, differing only by which `SELECTEDVALUE` measure they reference
- Each branch calls `MAX()` on the column, which is safe in a scatter chart context where the granularity is per-employee
- Add or remove branches to match the variables defined in `VariablesX`/`VariablesY`
- Returns `BLANK()` when the selected name does not match any branch — this filters out blank points from the scatter chart automatically

## Related

- [[interactive-tooltip-scatter-chart-on-matrix]] — `pattern` — tooltip scatter chart
- [[selected-x-name-selected-y-name]] — `function` — captures the selected variable name
- [[correlation-core-pearson-measure]] — `function` — the same SWITCH pattern for Pearson calculation
