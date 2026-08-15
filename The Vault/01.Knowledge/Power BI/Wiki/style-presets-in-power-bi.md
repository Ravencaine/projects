---
created: 2026-08-11
source: Style Presets in Power BI
note_type: pattern
tags: [power-bi, style-presets, json, theming, formatting]
---

# Style Presets — Visual-Level Formatting via JSON

Reusable formatting templates for individual Power BI visuals, defined in JSON theme files. Introduced March 2025 (Power BI Desktop 2.141+).

## Purpose

Style presets allow you to define formatting once and apply it to any matching visual with a single click — without adjusting properties manually per visual. Think of them as themes at the individual visual level.

## When to Use

- Need consistent formatting across multiple visuals of the same type
- Managing multiple reports and want uniform design
- Beginners who struggle navigating the format pane
- Reports where formatting changes need to scale automatically

## Requirements

- Power BI Desktop **March 2025 or newer**
- Presets are **hidden by default** — must be defined in the theme JSON file
- No built-in UI editor; must be written in JSON

## How It Works

1. Prepare a theme JSON file
2. Add a `visualStyles` section
3. Under each visual type (e.g., card, columnChart), add a `stylePresets` block
4. Use the `*` key to set the default preset
5. Load the theme into Power BI
6. The Style Presets section appears in the format pane for matching visuals

## JSON Structure

```json
"visualStyles": {
  "card": {
    "*": {
      "stylePresets": {
        "RoundedCard": {
          "label": { "fontSize": 18 },
          "border": { "radius": 8, "color": "#D3D3D3" }
        }
      }
    }
  }
}
```

- `"*"` = default preset applied automatically to all card visuals
- Named presets (e.g., "RoundedCard") appear as options in the format pane

## Common Preset Names

| Preset | Visual | Description |
|--------|--------|-------------|
| RoundedCard | card | Border radius + adjusted fonts |
| ValueOnly | card | Minimal — for use inside composite visuals |
| DarkMode | card | High-contrast for dark themes |
| CompactBar | barChart | Narrower bars with labels |

## Creating Presets Efficiently

1. Build and export a theme using PowerBI.tips Theme Generator
2. Open the exported JSON in VS Code
3. Copy relevant visual settings
4. Paste into the `stylePresets` block
5. Adjust values as needed

## Limitations

- No UI editor — must write JSON directly
- Presets are not visible unless defined in the theme
- Each preset applies to one visual type only
- Requires March 2025+ version

## Related

- [[style-presets-json]] — snippet: ready-to-use JSON template
- [[boniface-muchendu]] — author
