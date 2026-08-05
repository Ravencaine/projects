---
created: 2026-08-03
source: New Power BI Style Presets.md
note_type: snippet
tags: [power-bi, theme, json, style-presets, clusteredcolumnchart]
---

# ColumnSimpleChart Preset

JSON configuration for a minimal embedded column chart preset — strips all visual chrome: no labels, no axes, no borders, no shadow, no padding.

## Code

```json
"ColumnSimpleChart": {
  "background": [
    {
      "show": false
    }
  ],
  "border": [
    {
      "show": false
    }
  ],
  "categoryAxis": [
    {
      "show": false
    }
  ],
  "dropShadow": [
    {
      "show": false
    }
  ],
  "labels": [
    {
      "show": false
    }
  ],
  "padding": [
    {
      "left": 0,
      "right": 0,
      "bottom": 0,
      "top": 0
    }
  ],
  "title": [
    {
      "show": false
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

- Small or embedded visuals where minimalism is essential
- Sparkline-style charts placed beside KPI cards
- When the visual is purely decorative or contextual

## Related

- [[Style-Presets-Pattern.md]]
- [[Style-Presets-Visual-Hierarchy.md]]
