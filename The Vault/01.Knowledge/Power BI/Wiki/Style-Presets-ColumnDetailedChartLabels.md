---
created: 2026-08-03
updated: 2026-08-05
source: New Power BI Style Presets.md
note_type: snippet
tags: [power-bi, theme, json, style-presets, clusteredcolumnchart]
---

# ColumnDetailedChartLabels Preset

JSON configuration for a data-dense column chart preset — shows drop shadow, bold data labels, and hides the value axis.

## Code

```json
"ColumnDetailedChartLabels": {
  "dropShadow": [
    {
      "show": true,
      "position": "Outer",
      "shadowSpread": 1,
      "shadowBlur": 0,
      "angle": 0,
      "shadowDistance": 0,
      "preset": "Center",
      "transparency": 90
    }
  ],
  "labels": [
    {
      "show": true,
      "bold": true
    }
  ],
  "valueAxis": [
    {
      "show": false
    }
  ]
}
```

## When to Use

- KPI charts that need visible values at a glance
- Focal-point charts in dashboards where data labels add signal
- Default preset for clustered column charts in the theme

## Related

- [[Style-Presets-Pattern.md]]
- [[Style-Presets-Visual-Hierarchy.md]]
