---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: pattern
tags: [power-bi, html, font-awesome, dax, icon, cdn, pattern]
---

# Font Awesome DAX Icon Measure Pattern

**Type:** Pattern · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

Return a Font Awesome icon from a DAX measure using a CDN stylesheet + SUBSTITUTE placeholders for icon code, color, and size. Icons are fully dynamic — color and size change per data context.

## Template measure

```dax
Icon Font awesome icon set up =
"<head>
    <meta name=""viewport"" content=""width=device-width, initial-scale=1"">
    <link rel=""stylesheet"" href=""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css""/>
</head>
<i style=""color:{COLOR}"" class=""{ICON_CODE} {SIZE}"">
</i>
&nbsp;"
```

Three placeholders: `{COLOR}`, `{ICON_CODE}`, `{SIZE}`.

## CDN for Font Awesome 6.1.1

`https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css`

Free tier includes solid icons. Membership unlocks additional icon sets.

## Size classes

| Class | Size |
|-------|------|
| `fa-xs` | Extra small |
| `fa-sm` | Small |
| `fa-md` | Medium |
| `fa-lg` | Large |
| `fa-xl` | Extra large |
| `fa-2x` – `fa-10x` | Fixed multiplier |

## Icon substitution example

```dax
Icon green arrow up =
SUBSTITUTE(
    SUBSTITUTE(
        SUBSTITUTE(
            [Icon Font awesome icon set up],
            "{ICON_CODE}", "fa-solid fa-arrow-trend-up"
        ),
        "{SIZE}", "fa-md"
    ),
    "{COLOR}", [Color Green]
)
```

## Common icon codes

| Icon | Code |
|------|------|
| Arrow up | `fa-solid fa-arrow-trend-up` |
| Arrow down | `fa-solid fa-arrow-trend-down` |
| Check | `fa-solid fa-check` |
| Warning | `fa-solid fa-triangle-exclamation` |
| Star | `fa-solid fa-star` |

## Combining with shapes

Icons can be placed inside HTML shapes (div/oval) via the `{TEXT}` placeholder:

```dax
"[Icon green arrow up] & " " & _Variation
```

Icon + space + text inside the oval shape.

## Related

- [[html-shape-measure-template]] — shape with icon placeholder
- [[substitute-placeholder-chaining]] — nested SUBSTITUTE
- [[html-measure-integration-pattern]] — full integration
