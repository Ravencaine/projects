---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [custom-fonts, theme-json, font-family, card-visual]
related: [Import-Theme-JSON]
---

# Custom Fonts via Theme JSON

Applies custom font families across all report pages by editing and reimporting a Power BI theme JSON file.

## Steps

### 1 — Export Current Theme

**Power BI Desktop → View → Customize → Export current theme (.json)**

### 2 — Edit the JSON

```json
{
  "name": "Custom Fonts Theme",
  "visualStyles": {
    "card": {
      "*": {
        "general": {
          "fontFamily": "Segoe UI Semibold"
        },
        "calloutValue": {
          "fontSize": 28,
          "fontFamily": "Segoe UI Semibold"
        },
        "labels": {
          "fontSize": 10,
          "fontFamily": "Segoe UI"
        }
      }
    },
    "slicer": {
      "*": {
        "header": {
          "fontFamily": "Segoe UI Semibold",
          "fontSize": 12
        },
        "items": {
          "fontFamily": "Segoe UI",
          "fontSize": 10
        }
      }
    },
    "multiRowCard": {
      "*": {
        "cardTitle": {
          "fontFamily": "Segoe UI Semibold",
          "fontSize": 12
        },
        "itemSubtitle": {
          "fontFamily": "Segoe UI",
          "fontSize": 9
        }
      }
    },
    "clusteredBarChart": {
      "*": {
        "legend": {
          "fontFamily": "Segoe UI",
          "fontSize": 10
        },
        "xAxis": {
          "fontFamily": "Segoe UI",
          "fontSize": 9
        }
      }
    }
  }
}
```

### 3 — Reimport Theme

**Power BI Desktop → View → Browse for themes → select edited JSON**

## What Can Be Formatted via JSON

| Visual | Properties |
|--------|-----------|
| Card | calloutValue font, label font, background |
| MultiRowCard | cardTitle, itemSubtitle |
| Slicer | header font, item font |
| Clustered Bar | legend, x-axis, y-axis font |
| All visuals | general → fontFamily |

## Limitations

- Fonts must be installed on the viewer's machine or embedded via Power BI Service.
- The formatting pane does not expose all font properties — JSON is required for Card callout values and Slicer items.
- A new JSON theme replaces the previous one entirely.

## Related

- [[Import-Theme-JSON]] — Power Query workflow for editing and reimporting themes
- [[Advanced-KPI-Cards]] — card visual formatting
