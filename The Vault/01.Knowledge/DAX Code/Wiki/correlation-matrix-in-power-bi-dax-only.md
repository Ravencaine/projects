---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: pattern
tags: [dax, power-bi, correlation, matrix, visualization]
---

# Correlation Matrix in Power BI (DAX-only)

Build a fully dynamic, interactive correlation matrix visual using only DAX and the native Matrix visual in Power BI — no Python, no external tools.

## Purpose

Display pairwise Pearson correlation coefficients between N numeric variables in a matrix format. The visual responds to report-level filters and slicers, making it fully interactive. A tooltip page adds drill-through scatter plots on hover.

## Components

1. **`VariablesX` / `VariablesY`** — disconnected calculated tables (DATATABLE) listing variable names
2. **`Correlation`** — core Pearson measure using `SUMMARIZE`, `ADDCOLUMNS`, `SWITCH`, `SUMX`, `SQRT`, `AVERAGEX`
3. **`Correlation (Lower Triangle, No Diagonal)`** — display modifier hiding the upper triangle and diagonal
4. **Color palette measures** — `_Color *` static color string measures
5. **`Correlation Color (Buckets)`** — background color per correlation bucket
6. **`Correlation Font Color`** — font color (white on dark buckets, black on light)
7. **Tooltip page** — scatter chart with `X Value`, `Y Value`, `Scatter Title`, `Scatter Subtitle (HTML)`
8. **`Selected X Name` / `Selected Y Name`** — captures the currently selected row/column variable name

## Structure

### 1. Calculated Tables

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

### 2. Core Pearson Measure

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

### 3. Lower Triangle Display

```dax
Correlation (Lower Triangle, No Diagonal) =
VAR r     = [Correlation]
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )
RETURN
    IF ( ISBLANK ( r ) || ISBLANK ( XName ) || ISBLANK ( YName ), BLANK(), IF ( XName <= YName, BLANK(), r ) )
```

### 4. Matrix Visual Setup

- Rows: `VariablesX[Variable]`
- Columns: `VariablesY[Variable]`
- Values: `Correlation (Lower Triangle, No Diagonal)`
- Style preset: None
- Row/column subtotals: Off
- Borders: white; gridlines: thin white

### 5. Conditional Formatting (Cell Elements → Field Value)

- Background: `Correlation Color (Buckets)`
- Font color: `Correlation Font Color`

### 6. Tooltip Page

- Page type: Tooltip; size ~400×500px
- Visual: Scatter chart; X-Axis: `X Value`; Y-Axis: `Y Value`; Details: `Employee ID`
- Trend line: On (Analysis pane)
- Assign page as tooltip on the Matrix visual

## Color Buckets

| |r| range | Correlation strength | Background |
|---|---|---|---|
| < 0.10 | very weak/none | `#F5F5F5` |
| 0.10–0.30 | low | orange (neg) / green (pos) | light |
| 0.30–0.50 | medium | orange / green | mid |
| 0.50–0.70 | medium-high | orange / green | mid |
| ≥ 0.70 | high | orange / green | dark |
| 0.70–1.00 | high | teal / coral | dark |

## Related

- [[pearson-correlation-coefficient-in-dax]] — `pattern` — the Pearson formula embedded in the Correlation measure
- [[correlation-core-pearson-measure]] — `function` — the Correlation measure
- [[correlation-lower-triangle-no-diagonal]] — `function` — display modifier
- [[dax-color-bucket-conditional-formatting-matrix]] — `pattern` — color bucket system
- [[interactive-tooltip-scatter-chart-on-matrix]] — `pattern` — tooltip scatter chart
- [[pearson-correlation-coefficient]] — `atomic` — the statistical concept
