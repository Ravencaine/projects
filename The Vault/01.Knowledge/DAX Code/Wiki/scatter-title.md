---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, power-bi, tooltip, dynamic-title, text-concatenation]
---

# Scatter Title — Dynamic Chart Title for Correlation Tooltip

Concatenates the two selected variable names into a dynamic scatter chart title, displaying them in the tooltip.

## Signature

```dax
Scatter Title := [Selected X Name] & " vs " & [Selected Y Name]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Selected X Name]` | measure | Current row variable name |
| `[Selected Y Name]` | measure | Current column variable name |

## Returns

Text string: e.g., `"Overtime Hours vs Engagement Survey Score"`

## Notes

- Used as the Title field on the scatter chart visual in the tooltip page
- Dynamic: updates automatically as the user hovers over different cells in the matrix

## Related

- [[interactive-tooltip-scatter-chart-on-matrix]] — `pattern` — tooltip scatter chart
- [[selected-x-name-selected-y-name]] — `function` — the source measures
- [[scatter-subtitle-html-dynamic-label-badge]] — `function` — HTML subtitle for the same tooltip
