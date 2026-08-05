---
created: 2026-08-03
source: New Power BI Style Presets.md
note_type: snippet
tags: [power-bi, theme, json, style-presets, clusteredcolumnchart]
---

# ColumnDetailedChartNoLabels Preset

JSON configuration for a structural column chart preset — no data labels, dashed gridlines visible on the value axis.

## Code

```json
"ColumnDetailedChartNoLabels": {
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
      "show": false
    }
  ],
  "valueAxis": [
    {
      "gridlineStyle": "dashed",
      "gridlineShow": true,
      "gridlineColor": {
        "solid": {
          "color": "#ACB5B9"
        }
      }
    }
  ]
}
```

## When to Use

- When chart structure and comparison matter more than exact values
- Situations where axis labels suffice
- Where a cleaner, less cluttered look is preferred

## Related

- [[Style-Presets-Pattern.md]]
- [[Style-Presets-Visual-Hierarchy.md]]
