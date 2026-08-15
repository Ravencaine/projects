---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: pattern
tags: [power-bi, custom-icons, json-theme, cell-element, conditional-formatting, svg, pattern]
---

# Custom Icons JSON Theme Cell Element Pattern

**Type:** Pattern · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

Embed custom icons (SVG, PNG, JPEG, GIF, Unicode, emoji) in a Power BI JSON theme file and apply them to table columns via cell element conditional formatting. Achieves polished visual indicators without extra model columns or SVG sorting conflicts.

## When to use

When you need icon-based visual indicators in table columns (status badges, category icons, trend indicators) and want: fast visual load, no sort conflicts, and theme-managed deployment.

## Theme file structure

```json
"icons": {
  "IconName": {
    "url": "data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24'>...</svg>"
  }
}
```

## Applying icons in the table

1. Select table visual
2. Open Cell Elements formatting
3. Navigate to Icon formatting for the target column
4. Icon type → Icon (or URL)
5. By value or rules → select the icon by name

## Icon naming in theme

Each icon in the theme must have a unique `IconName` key. The name is what appears in the conditional formatting dropdown.

## Design constraints

- Keep icons simple and small — icons render at fixed small size
- Avoid detailed icons with embedded text (e.g., pills with labels)
- For complex designs: consider SVG column approach instead

## Related

- [[svg-to-theme-url-transformation]] — URL encoding steps
- [[embed-custom-icons-theme-workflow]] — step-by-step
- [[icons-numerical-values-min-max-gotcha]] — min/max constraint workaround
