---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, correlation, matrix, selector, tooltip]
---

# Selected X Name / Selected Y Name

Captures the currently selected variable name from the Matrix visual's row and column axes. Used to drive dynamic axis labels and the variable lookup in tooltip scatter charts.

## Signatures

```dax
Selected X Name := SELECTEDVALUE ( VariablesX[Variable] )
Selected Y Name := SELECTEDVALUE ( VariablesY[Variable] )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `VariablesX[Variable]` | column | Row variable names from the disconnected selector table |
| `VariablesY[Variable]` | column | Column variable names from the disconnected selector table |

## Returns

A single text string — the display name of the currently selected variable in the row (X) or column (Y) axis. Returns `BLANK()` if no value or multiple values are selected.

## Notes

- `SELECTEDVALUE` is safe in a Matrix visual context because exactly one cell is active at a time
- In the tooltip page, these measures retrieve the same selected values from the parent visual's context
- Both measures are referenced by `X Value`, `Y Value`, and `Scatter Subtitle (HTML)` to build the dynamic scatter chart labels

## Related

- [[interactive-tooltip-scatter-chart-on-matrix]] — `pattern` — tooltip scatter chart
- [[x-value-y-value-dynamic-variable-mapping]] — `function` — uses these to map to numeric values
- [[scatter-subtitle-html-dynamic-label-badge]] — `function` — uses these for plain-language text
- [[variablesx-variablesy-disconnected-selector-tables]] — `function` — the source tables
