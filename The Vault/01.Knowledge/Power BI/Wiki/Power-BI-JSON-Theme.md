---
created: 2026-08-05
source: 3 Time-Saving Hacks for Power BI Development (Boniface Muchendu)
note_type: reference
tags: [power-bi, theme, json, color-palette, font, visual-defaults, workflow]
---

# Power BI JSON Theme

A JSON configuration file that defines the visual appearance of a Power BI report — colors, fonts, text sizes, visual defaults, and more.

## Overview

Power BI themes allow you to define a consistent visual style and apply it to an entire report in one click. Themes are stored as `.json` files and can be created, edited, and shared across reports.

## How to Create

1. In Power BI Desktop: **View → Themes → Customize current theme**
2. Configure colors, fonts, and visual defaults
3. **View → Themes → Save current theme** → exports a `.json` file
4. Open the saved `.json` in **Visual Studio Code** for precise editing

## Key Properties in a Theme JSON

| Property | Description |
|----------|-------------|
| `name` | Theme display name |
| `dataColors` | Hex color palette for chart series |
| `background` | Report background color |
| `foreground` | Primary text color |
| `tableAccent` | Accent color for table and matrix headers |
| `visualStyles` | Per-visual-type overrides (fonts, sizes, margins) |
| `textClasses` | Named text styles with font family, size, and color |

## Why Edit in Visual Studio Code

Visual Studio Code provides syntax highlighting, auto-complete (with JSON schema), and bracket matching — making large theme files easier to navigate and edit than Power BI's built-in theme editor.

## Notes

- Themes do not affect existing visuals until they are reapplied
- Community theme templates are available on GitHub (search `powerbi-theme`)
- Theme JSON files are portable — share them via email, Teams, or a shared drive

## Related

- [[Time-Saving-Hacks-Power-BI-Workflow]]
- [[power-bi-design-best-practices]]
