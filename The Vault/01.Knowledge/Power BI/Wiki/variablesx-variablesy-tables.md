---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: pattern
tags: [powerbi, dax, datatable, calculated-table, correlation]
---

# VariablesX / VariablesY Tables

Two identical calculated tables used as row/column axes for a DAX-only correlation matrix in Power BI. Each table holds the list of variable names that will appear in the matrix.

## Definition

Both tables are identical `DATATABLE` expressions — one for the matrix rows (X axis) and one for the columns (Y axis):

```c
VariablesX =
DATATABLE (
    "Variable", STRING,
    {
        { "Performance Rating" },
        { "Training Hours Completed" },
        { "Absenteeism Rate (%)" },
        { "Engagement Survey Score" },
        { "Overtime Hours" },
        { "Tenure in Role (months)" }
    }
)

VariablesY =
DATATABLE (
    "Variable", STRING,
    {
        { "Performance Rating" },
        { "Training Hours Completed" },
        { "Absenteeism Rate (%)" },
        { "Engagement Survey Score" },
        { "Overtime Hours" },
        { "Tenure in Role (months)" }
    }
)
```

## Usage

- `VariablesX[Variable]` → Rows of the Matrix visual
- `VariablesY[Variable]` → Columns of the Matrix visual
- `SELECTEDVALUE ( VariablesX[Variable] )` → current row variable name inside measures
- `SELECTEDVALUE ( VariablesY[Variable] )` → current column variable name inside measures

## Notes

- Both tables must have identical contents so that every variable pair appears in both row and column positions.
- Add/remove rows from the DATATABLE to change which variables appear in the matrix.
- Used as the foundation for [[pearson-correlation-measure]] and [[scatter-tooltip-x-y-value-measures]].

## Related

- [[pearson-correlation-measure]]
- [[scatter-tooltip-x-y-value-measures]]
