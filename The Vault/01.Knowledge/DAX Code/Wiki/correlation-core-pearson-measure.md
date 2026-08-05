---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, correlation, pearson, measure, matrix]
---

# Correlation — Core Pearson Correlation Measure

Calculates the Pearson correlation coefficient between two numeric variables, resolving them dynamically from the currently selected row and column in a Matrix visual.

## Signature

```dax
Correlation :=
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )
VAR Base = SUMMARIZE ( 'Data', 'Data'[ID], "Xcol", MAX(...), "Ycol", MAX(...) )
VAR WithXY = ADDCOLUMNS ( Base, "X", SWITCH(TRUE(), XName = "Name1", [Xcol], ...), "Y", SWITCH(TRUE(), YName = "Name1", [Xcol], ...) )
VAR Clean = FILTER ( WithXY, NOT ISBLANK ( [X] ) && NOT ISBLANK ( [Y] ) )
VAR AvgX = AVERAGEX ( Clean, [X] )
VAR AvgY = AVERAGEX ( Clean, [Y] )
VAR Num = SUMX ( Clean, ( [X] - AvgX ) * ( [Y] - AvgY ) )
VAR Den = SQRT ( SUMX ( Clean, ( [X] - AvgX ) ^ 2 ) * SUMX ( Clean, ( [Y] - AvgY ) ^ 2 ) )
RETURN IF ( 0 = COUNTROWS ( Clean ), BLANK(), Num / Den )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `VariablesX[Variable]` | STRING | Currently selected variable name for the row axis |
| `VariablesY[Variable]` | STRING | Currently selected variable name for the column axis |
| Base table columns | any | One `MAX()` per numeric variable in the data table |

## Returns

A decimal value in [-1, +1]. Returns `BLANK()` when either variable has no valid data rows.

## Example (full measure)

```dax
Correlation =
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )
VAR Base =
    SUMMARIZE (
        'HR Data', 'HR Data'[Employee ID],
        "Perf",   MAX ( 'HR Data'[Performance Rating] ),
        "Train",  MAX ( 'HR Data'[Training Hours Completed] ),
        "Abs",    MAX ( 'HR Data'[Absenteeism Rate (%)] ),
        "Eng",    MAX ( 'HR Data'[Engagement Survey Score] ),
        "OT",     MAX ( 'HR Data'[Overtime Hours] ),
        "Tenure", MAX ( 'HR Data'[Tenure in Role (months)] )
    )
VAR WithXY =
    ADDCOLUMNS (
        Base,
        "X", SWITCH ( TRUE(), XName = "Performance Rating", [Perf], XName = "Training Hours Completed", [Train], XName = "Absenteeism Rate (%)", [Abs], XName = "Engagement Survey Score", [Eng], XName = "Overtime Hours", [OT], XName = "Tenure in Role (months)", [Tenure], BLANK() ),
        "Y", SWITCH ( TRUE(), YName = "Performance Rating", [Perf], YName = "Training Hours Completed", [Train], YName = "Absenteeism Rate (%)", [Abs], YName = "Engagement Survey Score", [Eng], YName = "Overtime Hours", [OT], YName = "Tenure in Role (months)", [Tenure], BLANK() )
    )
VAR Clean = FILTER ( WithXY, NOT ISBLANK ( [X] ) && NOT ISBLANK ( [Y] ) )
VAR N     = COUNTROWS ( Clean )
VAR AvgX  = AVERAGEX ( Clean, [X] )
VAR AvgY  = AVERAGEX ( Clean, [Y] )
VAR Num   = SUMX ( Clean, ( [X] - AvgX ) * ( [Y] - AvgY ) )
VAR Den   = SQRT ( SUMX ( Clean, ( [X] - AvgX ) ^ 2 ) * SUMX ( Clean, ( [Y] - AvgY ) ^ 2 ) )
RETURN IF ( 0 = N, BLANK(), Num / Den )
```

## Notes

- **Naming conflict:** The VAR `Base` shadows the DAX function `BASE()`. Use a different name like `BaseData` if needed
- **Division by zero guard:** `IF ( 0 = N, BLANK(), Num / Den )` — denominator is zero only when all X or all Y values are identical
- **Respects report filters:** `SUMMARIZE` over the base table means all active filters (slicers, cross-highlighting) apply to the employee cohort
- **String matching:** Variable names in `SWITCH(TRUE())` must exactly match the strings in `VariablesX`/`VariablesY`

## Related

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — full matrix implementation
- [[pearson-correlation-coefficient-in-dax]] — `pattern` — formula walkthrough
- [[correlation-lower-triangle-no-diagonal]] — `function` — wraps this measure to hide upper triangle
- [[variablesx-variablesy-disconnected-selector-tables]] — `function` — selector tables this depends on
