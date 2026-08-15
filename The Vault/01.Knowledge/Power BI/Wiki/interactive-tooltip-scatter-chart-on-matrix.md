---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: pattern
tags: [dax, power-bi, tooltip, scatter, visualization]
---

# Interactive Tooltip — Scatter Chart on Correlation Matrix

A tooltip page on a Power BI report that displays a scatter chart of the two variables in the currently hovered matrix cell, showing the individual data points behind the correlation.

## Purpose

Drill-through context on hover: users see the actual distribution of data points and a trend line, making it immediately clear why the correlation is strong, weak, or negative.

## Components

1. **Tooltip page** (Page type: Tooltip, ~400×500px)
2. **Scatter chart:** X-Axis: `X Value`, Y-Axis: `Y Value`, Details: `Employee ID`
3. **Measures:** `Selected X Name`, `Selected Y Name`, `X Value`, `Y Value`, `Scatter Title`, `Scatter Subtitle (HTML)`
4. **Trend line** enabled via Analysis pane

## Page Setup

```
Page type: Tooltip
Size: ~400px × 500px
```

## Scatter Chart Measures

```dax
Selected X Name = SELECTEDVALUE ( VariablesX[Variable] )
Selected Y Name = SELECTEDVALUE ( VariablesY[Variable] )

X Value =
VAR _name = [Selected X Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",            MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",       MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",          MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",        MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",                MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",       MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)

Y Value =
-- identical SWITCH structure, references [Selected Y Name]
```

```dax
Scatter Title = [Selected X Name] & " vs " & [Selected Y Name]
```

## HTML Subtitle (colored badge + plain-language sentence)

```dax
Scatter Subtitle (HTML) =
VAR _x = [Selected X Name]
VAR _y = [Selected Y Name]
VAR _r = [Correlation]
VAR _abs = IF ( ISBLANK ( _r ), BLANK(), ABS ( _r ) )

VAR _labelRaw =
    SWITCH( TRUE(),
        _r <= -0.70, "high negative",
        _r <= -0.50, "medium negative",
        _r <= -0.30, "low negative",
        _r >=  0.70, "high positive",
        _r >=  0.50, "medium positive",
        _r >=  0.30, "low positive",
        "very weak/none"
    )
VAR _labelText = UPPER(LEFT(_labelRaw,1)) & MID(_labelRaw,2,LEN(_labelRaw)-1)

VAR _bg = IF( _labelRaw = "very weak/none" || _abs < 0.10, [_Color White], SWITCH( _labelRaw, "high negative", [_Color Dark Orange], "medium negative", [_Color Mid Orange], "low negative", [_Color Light Orange], "high positive", [_Color Dark Green], "medium positive", [_Color Mid Green], "low positive", [_Color Light Green] ) )
VAR _fg = IF( _labelRaw IN { "high negative", "high positive", "medium negative", "medium positive" }, "#FFFFFF", [_Color dark grey] )

VAR _badgeFull = "<span style='background-color:" & _bg & "; color:" & _fg & "; padding:1px 6px; font-size:12px; font-family:Segoe UI Light; font-weight:600; display:inline-block; white-space:nowrap'>" & _labelText & " correlation</span>"
VAR _headline = _badgeFull & ", <b>r = " & FORMAT( _r, "0.00" ) & "</b>"

VAR _sentenceRaw = _y & " tends to increase as " & _x & " increases"
VAR _sentenceFinal = IF( _r > 0, SUBSTITUTE( SUBSTITUTE( _sentenceRaw, "increases", "<b>increases</b>" ), "decreases", "<b>decreases</b>" ), SUBSTITUTE( SUBSTITUTE( _sentenceRaw, "increases", "<b>decreases</b>" ), "decreases", "<b>increases</b>" ) )

RETURN
IF( ISBLANK(_r) || ISBLANK(_x) || ISBLANK(_y), BLANK(),
    "<div style='color:" & [_Color dark grey] & "; font-family:Segoe UI Light; font-size:12px; line-height:1.4'>" & _headline & "<br/>" & _sentenceFinal & "</div>"
)
```

## Link to Matrix

On the Matrix visual: **General → Tooltip → Select the tooltip page** as the report page to use.

## Key Behaviour

- Scatter chart is filtered by the same report-level filters as the matrix, so department slicers propagate to the tooltip
- The HTML subtitle dynamically flips "increases" → "decreases" based on the sign of r
- The color badge matches the same bucket thresholds used in the matrix conditional formatting

## Related

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — parent matrix pattern
- [[selected-x-name-selected-y-name]] — `function` — variable name capture measures
- [[x-value-y-value-dynamic-variable-mapping]] — `function` — dynamic numeric value mapping
- [[scatter-subtitle-html-dynamic-label-badge]] — `function` — HTML subtitle measure
