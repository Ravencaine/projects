---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: pattern
tags: [power-bi, html, dax, conditional-formatting, color, icon, pattern]
---

# Dynamic HTML Conditional Styling Pattern

**Type:** Pattern · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

Use DAX IF to determine HTML/CSS property values (colors, icons, text) and SUBSTITUTE to inject them into an HTML template. Produces conditional visual output — colors, icons, and text change based on the underlying data without separate measures per variant.

## When to use

When you need KPI badges, status indicators, or shape-based labels that change color/icon/text based on business rules (positive/negative, above/below target, category type).

## Formula structure

```dax
VAR _BgColor = IF([Value] < 0, [Color Light Red], [Color Light Green])
VAR _FontColor = IF([Value] < 0, [Color Red], [Color Green])
VAR _Icon = IF([Value] < 0, [Icon Down], [Icon Up])
VAR _Text = FORMAT(ABS([Value]), "0.0%")
VAR _Shape =
    SUBSTITUTE(
        SUBSTITUTE(
            SUBSTITUTE(
                [Oval Set Up],
                "{BACKGROUND_COLOR}", _BgColor
            ),
            "{FONT_COLOR}", _FontColor
        ),
        "{TEXT}", _Icon & " " & _Text
    )
RETURN
    IF([Value] <> BLANK(), _Shape)
```

IF determines the color, icon, and text. SUBSTITUTE injects all three into the HTML template. IF gates output to BLANK when no data.

## Step-by-step

1. **IF for background color:** light red if negative, light green if positive
2. **IF for font color:** dark red if negative, dark green if positive
3. **IF for icon:** down arrow if negative, up arrow if positive (Font Awesome codes)
4. **FORMAT for text:** ABS() removes sign, FORMAT adds percentage
5. **SUBSTITUTE chain:** injects all three values into HTML template
6. **IF guard:** returns BLANK when underlying value is blank

## Color measures pattern

```dax
Color Green = "#2C6D6A"
Color Red = "#C0392B"
Color Light Green = "#D5F5E3"
Color Light Red = "#FADBD8"
```

Define color hex values as separate measures — reusability across all conditional styling.

## Icon measures pattern

```dax
Icon green arrow up =
SUBSTITUTE(
    SUBSTITUTE(
        SUBSTITUTE([Icon Template],
            "{ICON_CODE}", "fa-solid fa-arrow-trend-up"),
        "{SIZE}", "fa-md"),
    "{COLOR}", [Color Green]
)
```

## Related

- [[html-shape-measure-template]] — template
- [[substitute-placeholder-chaining]] — SUBSTITUTE chain
- [[font-awesome-dax-icon-measure]] — icon measures
- [[html-measure-integration-pattern]] — underlying mechanism
