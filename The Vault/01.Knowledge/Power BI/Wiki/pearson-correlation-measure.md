---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: pattern
tags: [powerbi, dax, correlation, pearson, summarize, switch]
---

# Pearson Correlation Measure

A DAX measure that computes the Pearson correlation coefficient between two variables selected via `VariablesX[Variable]` (rows) and `VariablesY[Variable]` (columns) in a Power BI Matrix visual.

## Formula

```c
Correlation =
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )

-- One row per employee, respecting all report filters (e.g., Department)
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

-- Map selected variable names to numeric series
VAR WithXY =
    ADDCOLUMNS (
        Base,
        "X",
            SWITCH (
                TRUE(),
                XName = "Performance Rating",           [Perf],
                XName = "Training Hours Completed",     [Train],
                XName = "Absenteeism Rate (%)",         [Abs],
                XName = "Engagement Survey Score",      [Eng],
                XName = "Overtime Hours",              [OT],
                XName = "Tenure in Role (months)",     [Tenure],
                BLANK ()
            ),
        "Y",
            SWITCH (
                TRUE(),
                YName = "Performance Rating",           [Perf],
                YName = "Training Hours Completed",     [Train],
                YName = "Absenteeism Rate (%)",         [Abs],
                YName = "Engagement Survey Score",      [Eng],
                YName = "Overtime Hours",              [OT],
                YName = "Tenure in Role (months)",     [Tenure],
                BLANK ()
            )
    )

VAR Clean = FILTER ( WithXY, NOT ISBLANK ( [X] ) && NOT ISBLANK ( [Y] ) )
VAR N     = COUNTROWS ( Clean )
VAR AvgX  = AVERAGEX ( Clean, [X] )
VAR AvgY  = AVERAGEX ( Clean, [Y] )
VAR Num   = SUMX ( Clean, ( [X] - AvgX ) * ( [Y] - AvgY ) )
VAR Den   =
    SQRT (
        SUMX ( Clean, ( [X] - AvgX ) ^ 2 ) *
        SUMX ( Clean, ( [Y] - AvgY ) ^ 2 )
    )
RETURN IF ( Den = 0, BLANK(), Num / Den )
```

## Key Design Decisions

- **SUMMARIZE** over 'HR Data' collapses to one row per employee, ensuring each observation is counted once regardless of visual context.
- **ADDCOLUMNS + SWITCH** maps the string variable names selected in the matrix to their numeric columns.
- **FILTER** removes rows where either X or Y is blank.
- **Denominator guard** (`Den = 0`) returns BLANK when all values are identical (no variance).
- Respects all report-level filters (department, role, etc.) because SUMMARIZE operates on the filtered data model.

## Variants

| Measure | Purpose |
|---------|---------|
| `Correlation` | Core Pearson coefficient (raw value -1 to +1) |
| `Correlation (Lower Triangle, No Diagonal)` | Hides upper triangle and diagonal for cleaner visual — see [[lower-triangle-no-diagonal-correlation]] |

## Related

- [[pearson-correlation-coefficient]]
- [[variablesx-variablesy-tables]]
- [[lower-triangle-no-diagonal-correlation]]
