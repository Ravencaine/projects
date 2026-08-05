---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [power-query, theme-json, custom-fonts]
related: [Custom-Fonts-via-Theme-JSON]
---

# Import Theme JSON with Custom Fonts (Power Query)

Export a Power BI theme, edit the JSON to add custom font families, and reimport to apply fonts across all report visuals.

## Step 1 — Export Current Theme

In Power BI Desktop: **View → Customize → Export current theme (.json)**.

## Step 2 — Edit the JSON

Open the exported JSON and locate the `visualStyles` section. Add `fontFamily` under each visual type:

```json
{
  "name": "Custom Font Theme",
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
          "fontFamily": "Segoe UI Semibold"
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
    }
  }
}
```

## Step 3 — Reimport Theme

In Power BI Desktop: **View → Browse for themes → select the edited JSON**.

## Notes

- Bittar's "Custom Fonts in Power BI" article covers this end-to-end. The JSON approach is the only way to set fonts on card callout values and slicer items — the standard formatting pane doesn't expose these.
- Custom fonts must be installed on the viewer's machine, or embed the report in the Power BI service where fonts are hosted.
- The theme JSON approach applies fonts consistently across all pages and all visuals of a given type — much faster than formatting each visual individually.
- To apply font changes to existing reports: reimport the theme → all visuals update automatically.

## Related

- [[Custom-Fonts-via-Theme-JSON]] — Power BI pattern note with full JSON reference
- [[Build-Period-Table]] — another Power Query workflow note
