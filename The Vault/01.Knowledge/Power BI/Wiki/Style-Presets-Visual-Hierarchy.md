---
created: 2026-08-03
updated: 2026-08-05
source: New Power BI Style Presets.md
note_type: atomic
tags: [power-bi, theme, json, visualstyles]
---

# Visual Styles Hierarchy in JSON Themes

Power BI resolves visual formatting through a three-level inheritance chain in JSON themes. Understanding this hierarchy prevents over-specifying properties and keeps themes maintainable.

## Definition

Formatting is applied in this order — later levels override earlier ones for properties that are explicitly set:

```
Global defaults  →  Visual type defaults  →  Preset overrides
(visualStyles   →  (visualStyles           →  (stylePreset
 > "*">"*")       > <type>">"*")             > <PresetName>)
```

## Key Points

- **Level 1 — Global defaults** (`visualStyles > "*" > "*"`): Settings that apply to every visual in the report. Use this for universal choices: background color, border radius, tooltip formatting, visual header visibility.

- **Level 2 — Visual type defaults** (`visualStyles > <type> > "*"`): Per-visual-type base formatting. Set `stylePreset` here to assign a default preset that loads automatically when the theme is applied.

- **Level 3 — Preset overrides** (`visualStyles > <type> > <PresetName>`): Named style variations that override only the properties they specify. All unset properties cascade down from the type defaults or global defaults.

- **Inheritance is additive, not total.** A preset only needs to define the properties it changes. Missing properties always inherit from the level above.

- **The `stylePreset` assignment** lives in the type defaults (`"*"`) — it names the preset to activate. The preset's actual configuration lives in its own sibling property block.

## Example

```json
"visualStyles": {
  "*": {
    "*": {
      // Level 1: global — all visuals
      "background": [{ "transparency": 0 }]
    }
  },
  "clusteredColumnChart": {
    "*": {
      // Level 2: type defaults — all column charts
      "categoryAxis": [{ "showAxisTitle": false }],
      "stylePreset": [{ "name": "ColumnDetailedChartLabels" }]
    },
    "ColumnSimpleChart": {
      // Level 3: preset — only column charts using this preset
      "background": [{ "show": false }],
      "labels": [{ "show": false }]
    }
  }
}
```

## Related

- [[Style-Presets-Pattern.md]]
- [[Style-Presets-Workflow.md]]
