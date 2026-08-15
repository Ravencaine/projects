---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: workflow
tags: [power-bi, custom-icons, json-theme, cell-element, workflow]
---

# Embed Custom Icons Theme Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

Embed custom icons in a Power BI table via JSON theme + cell element conditional formatting. 5 steps: export theme → transform SVG → add icons section → reload theme → apply in table.

## When to use

When building table visuals that need icon-based indicators (status badges, category icons, trend arrows, KPI markers) and you want lightweight, sort-compatible, no-column-overhead icons.

## Step 1 — Export current JSON theme

1. Open Power BI Desktop
2. View → Themes → Save Current Theme
3. Save locally (e.g., `ProductTheme.json`)
4. Open in VS Code

## Step 2 — Transform SVG code

For each icon, apply the 4-step URL transformation:

1. Replace double quotes `"` with single quotes `'`
2. Escape: `#` → `%23`, spaces → `%20`
3. Remove line breaks and indentation — collapse to one line
4. Add prefix: `data:image/svg+xml;utf8,`

## Step 3 — Add icons section to JSON

At the end of the JSON theme file, add:

```json
"icons": {
  "IconName1": {
    "url": "data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24'>...</svg>"
  },
  "IconName2": {
    "url": "data:image/svg+xml;utf8,<svg width='24' height='24' viewBox='0 0 24 24'>...</svg>"
  }
}
```

## Step 4 — Reload theme in Power BI

View → Themes → Browse for Themes → select updated JSON file.

## Step 5 — Apply icons via Cell Elements

1. Select table visual
2. Expand the column formatting
3. Navigate to **Icon** section
4. Icon type → select **Icon** (or URL)
5. By value / Rules → choose the icon by its theme name
6. Press OK

Icons appear in the column cells.

## Performance note

Theme icons are lightweight — they render as URL references, not as image data in every cell. This is faster than image data columns.

## Related

- [[svg-to-theme-url-transformation]] — transformation details
- [[custom-icons-json-theme-cell-element-pattern]] — pattern
- [[icons-numerical-values-min-max-gotcha]] — numerical value limitation
