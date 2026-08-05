---
created: 2026-08-03
source: New Power BI Style Presets.md
note_type: workflow
tags: [power-bi, theme, json, style-presets]
---

# Create and Apply Style Presets

Five-step end-to-end workflow for building a custom theme with style presets in Power BI Desktop.

## Prerequisites

- Power BI Desktop (March 2025 release or later)
- Visual Studio Code (recommended for JSON editing)
- `$schema` URL: `https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.141.json` (or latest)

## Steps

1. **Customize the base theme in Power BI Desktop**
   - Open your report
   - Go to **View > Themes > Customize current theme**
   - Make formatting changes through the UI (colors, fonts, etc.)
   - Click **Apply**
   - Go to **View > Themes > Save current theme** and export the `.json` file

2. **Add the `$schema` reference**
   - Open the exported `.json` in Visual Studio Code
   - Add or update the `$schema` property directly under the `name` field:
     ```json
     "$schema": "https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.141.json"
     ```
   - This enables IntelliSense: smart autocomplete and validation as you type

3. **Define the visual type defaults**
   - Under `visualStyles`, add a section for each visual type you want to configure (e.g., `clusteredColumnChart`, `lineChart`, `cardVisual`)
   - Use `"*"` as the key to set base formatting for all instances of that visual type
   - Assign a default preset via the `stylePreset` property:
     ```json
     "clusteredColumnChart": {
       "*": {
         "categoryAxis": [{ "showAxisTitle": false, "fontSize": 9 }],
         "stylePreset": [{ "name": "ColumnDetailedChartLabels" }]
       }
     }
     ```

4. **Create named preset definitions**
   - Add sibling properties to the visual type section, each named after a preset (e.g., `ColumnSimpleChart`, `LineDetailedChart`)
   - Each preset overrides only the properties it needs — all others inherit from the `"*"` defaults:
     ```json
     "ColumnSimpleChart": {
       "background": [{ "show": false }],
       "categoryAxis": [{ "show": false }],
       "labels": [{ "show": false }]
     }
     ```

5. **Load the theme and apply presets in Power BI Desktop**
   - Save the updated `.json` file
   - In Power BI Desktop: **View > Themes > Browse for themes** and reload the file
   - Click any visual → **Format > Style preset** — all custom presets for that visual type appear in the dropdown
   - Select a preset per visual instance

> **Note:** The Style preset dropdown appears in the Format pane **only** if at least one custom preset has been defined for that visual type in the JSON file.

## Variations

- **Add presets to new visual types:** repeat steps 3–4 for `lineChart`, `cardVisual`, `multiRowCard`, `slicer`, etc.
- **Override global defaults:** add `"*": { "*": { ... } }` under `visualStyles` for settings that apply to all visuals (background, border, tooltip, visual header)
- **Find the latest schema URL:** inside Power BI Desktop go to **View > Themes > Customize current theme** → click the "How to create a theme" link at the bottom → GitHub schema page

## Common Errors

- [[Style-Presets-Missing-Dropdown-Gotcha.md]] — Style preset dropdown does not appear

## Related

- [[Style-Presets-Pattern.md]] — the core pattern this workflow implements
- [[Style-Presets-Visual-Hierarchy.md]] — understand the 3-level inheritance model before defining presets
- [[Custom-Fonts-via-Theme-JSON.md]]
