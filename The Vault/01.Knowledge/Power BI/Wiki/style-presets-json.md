---
created: 2026-08-11
source: Style Presets in Power BI
note_type: snippet
tags: [power-bi, style-presets, json, theming]
---

# Style Presets JSON — visualStyles Template

Ready-to-use JSON snippet for defining style presets in a Power BI theme file.

## Full Theme Structure

```json
{
  "name": "My Theme",
  "visualStyles": {
    "card": {
      "*": {
        "stylePresets": {
          "RoundedCard": {
            "label": {
              "fontSize": 18,
              "fontFamily": "Segoe UI",
              "color": "#333333"
            },
            "border": {
              "radius": 8,
              "color": "#D3D3D3",
              "weight": 1,
              "show": true
            }
          },
          "ValueOnly": {
            "label": {
              "fontSize": 28,
              "fontFamily": "Segoe UI Semibold"
            },
            "border": {
              "show": false
            }
          },
          "DarkMode": {
            "label": {
              "fontSize": 18,
              "color": "#FFFFFF"
            },
            "background": {
              "color": "#1E1E1E",
              "transparency": 0
            }
          }
        }
      }
    },
    "columnChart": {
      "*": {
        "stylePresets": {
          "CompactBars": {
            "general": {
              "responsive": true
            },
            "legend": {
              "show": false
            }
          }
        }
      }
    }
  }
}
```

## Key Properties

| Key | Purpose |
|-----|---------|
| `visualStyles` | Top-level container for visual formatting |
| `card` / `columnChart` / etc. | Target visual type |
| `*` | Default preset applied to all matching visuals |
| `stylePresets` | Container for named preset definitions |
| Named preset ("RoundedCard") | Individual preset available in format pane |

## Usage

1. Add the `visualStyles` section to an existing theme JSON
2. Load the theme in Power BI: View > Browse for themes
3. Select a matching visual
4. Open Format pane > Style Presets — the named presets appear
