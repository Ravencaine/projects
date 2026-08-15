---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: pattern
tags: [html-visual, calculation-group, dynamic-text, dax, css]
---

# Dynamic HTML Text via Calculation Groups

Render Power BI text with user-selectable font, size, and color by combining an HTML custom visual with a Calculation Group that exposes CSS variables as filterable members.

## Purpose

When you want a Card or text title in Power BI to respect arbitrary Google Fonts, custom font sizes, and dynamic colors without re-publishing the report — drive the visual off a Calculation Group whose calculation items each render a different HTML snippet with CSS variables.

## Components

| Component | Role |
|-----------|------|
| Three DAX measures | The "text" content, the selected font name, the selected font size (with `px`) |
| Calculation Group | Exposes those variables as filterable calculation items |
| HTML custom visual | Renders the resulting HTML/CSS |
| Filters pane mapping | Binds Google Fonts table → font; numeric parameter → size; Calculation Group column → color variant |

## Structure

```dax
MyHTML_Text =
VAR _Text   = "Hello World"
VAR _Font   = SELECTEDVALUE('Google Fonts'[Font Name], "Roboto")
VAR _Size   = SELECTEDVALUE('FontSizeParam'[FontSizeParam Value], 50) & "px"
VAR _Color  = "<color-choice-from-calculation-group>"
RETURN
"<span style=""font-family:" & _Font & "; font-size:" & _Size & "; color:" & _Color & """>" & _Text & "</span>"
```

Place this measure in the **Values** field of the HTML custom visual.

### Calculation Items (in Tabular Editor)

Each calculation item is a different "preset" for color. Typical set:

- **Black** — `"black"`
- **Color** — `SELECTEDVALUE('ColorTable'[Hex], "black")`
- **Gradient** — `"linear-gradient(90deg, " & [Color1] & " " & [Pct1] & "%, " & [Color2] & " " & [Pct2] & "%)"`

Add a column from the calculation group to the report's filter pane; each item changes the resulting CSS without editing DAX.

## Example

Injae Park's demo: every text element on the page (titles, KPI labels, dividers) is an HTML visual. Three filters in the Filter pane — Google Fonts, the numeric parameter for size, the calculation group — let the user re-skin text without ever reopening the file.

## Variations

- **Static fast path** — skip the API, Google Fonts table, and numeric parameter. Hardcode font, size, and color in the measure. See [[google-fonts-api-power-bi]] — Static Variant.
- **Multi-text** — for several text blocks on the same page, swap the measure on each visual, or use a disconnected supporting table to select the message.

## Related

- [[google-fonts-api-power-bi]] — how to populate the font table
- [[kpi-context-cards-with-calculation-groups]] — the same Calculation Group pattern applied to KPI cards
- [[dynamic-color-themes-via-html-rgb]] — extending this pattern to backgrounds, borders, and gradients
