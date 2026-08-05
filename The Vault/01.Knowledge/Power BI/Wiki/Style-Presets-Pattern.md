---
created: 2026-08-03
updated: 2026-08-05
source: New Power BI Style Presets.md
note_type: pattern
tags: [power-bi, theme, json, style-presets]
---

# Style Presets Pattern

Define multiple named visual style variations within a single Power BI JSON theme file, then switch between them per visual instance in Power BI Desktop.

## Purpose

Power BI's March 2025 update adds `stylePreset` support to JSON themes. Previously, each visual type had exactly one set of formatting defined per theme. Style presets allow multiple named variants — e.g., a detailed chart with labels and a minimal chart without — defined in the same JSON file and selectable per visual via **Format > Style preset**.

Use cases:
- KPI cards vs analysis charts (different density levels)
- Embedded visuals vs focal-point visuals
- Conditional layouts without duplicating the entire theme

## Components

1. `$schema` reference (for IntelliSense)
2. Global defaults under `visualStyles > * > *`
3. Visual type defaults under `visualStyles > <type> > *`
4. Named preset definitions under `visualStyles > <type> > <PresetName>`

## Structure

```json
{
  "name": "My Theme",
  "$schema": "https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.141.json",
  "visualStyles": {
    "*": {
      "*": {
        // global defaults — apply to all visuals
      }
    },
    "clusteredColumnChart": {
      "*": {
        // visual-type defaults — base style for this type
        "stylePreset": [{ "name": "ColumnDetailedChartLabels" }]
      },
      "ColumnDetailedChartLabels": {
        // preset override — inherits missing props from defaults
      },
      "ColumnSimpleChart": {
        // another preset
      }
    }
  }
}
```

## Example

Three presets for a column chart — all defined in one theme:

- **ColumnDetailedChartLabels** — rich display: drop shadow, visible data labels, no gridlines
- **ColumnDetailedChartNoLabels** — structural display: no labels, dashed gridlines
- **ColumnSimpleChart** — minimal embedded: no labels, no axes, no borders, no shadow

## Variations

Presets can be defined for any visual type. Common targets:

| Visual type | Preset names from sample |
|-------------|--------------------------|
| `clusteredColumnChart` | ColumnDetailedChartLabels, ColumnDetailedChartNoLabels, ColumnSimpleChart |
| `lineChart` | LineDetailedChart |
| `cardVisual` | SmallCard |

## Related

- [[Style-Presets-Visual-Hierarchy.md]]
- [[Style-Presets-Workflow.md]]
- [[Custom-Fonts-via-Theme-JSON.md]]
