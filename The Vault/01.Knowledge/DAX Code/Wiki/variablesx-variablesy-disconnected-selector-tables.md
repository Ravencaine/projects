---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, power-bi, matrix, correlation, pattern]
---

# Disconnected Selector Tables for Correlation Matrix (VariablesX / VariablesY)

Two identical `DATATABLE`-based calculated tables that list the variable names used as rows and columns in a correlation matrix visual.

## Signature

```dax
VariablesX = DATATABLE ( "Variable", STRING, { { "name" }, ... } )
VariablesY = DATATABLE ( "Variable", STRING, { { "name" }, ... } )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `Variable` | STRING | Column name; holds the display name of each numeric variable in the model |

## Returns

A single-column table with one row per variable. `VariablesX` drives **Rows** on the Matrix visual; `VariablesY` drives **Columns**.

## Example

```dax
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
```

## Notes

- Both tables contain identical data; they are separate so `SELECTEDVALUE(VariablesX[Variable])` and `SELECTEDVALUE(VariablesY[Variable])` can resolve independently in the same visual context
- Each variable name in the table must **exactly match** the string used in the `SWITCH(TRUE())` branches of the `Correlation` measure
- Add or remove rows to change which variables appear in the matrix — no other code changes needed
- These tables are **disconnected** from the data model (no relationships), relying entirely on `SELECTEDVALUE` + `SWITCH` for dynamic lookup

## Related

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — end-to-end setup
- [[correlation-core-pearson-measure]] — `function` — uses these tables to resolve X and Y
