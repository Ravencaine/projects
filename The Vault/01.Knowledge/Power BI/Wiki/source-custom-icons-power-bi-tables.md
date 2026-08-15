---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
source_url: "https://medium.com/the-bi-corner/elevate-your-power-bi-tables-with-custom-icons-8fc36bad794b"
author: "[[Isabelle Bittar]]"
site: https://medium.com/@isabittar
published: 2024-12-31
source_type: article
kb_routing: Power BI
tags: [power-bi, custom-icons, json-theme, table, cell-element, conditional-formatting, svg]
---

# Elevate Your Power BI Tables with Custom Icons

Isabelle Bittar · KI Data Science · Medium · 2024-12-31

## What this article covers

Embed custom SVG icons into a Power BI JSON theme file and apply them to table columns via cell element conditional formatting. Faster than image data or SVG columns, no sort conflicts, no extra columns needed.

## Advantages over SVG columns

- Lightweight — less visual load
- No column/field sorting conflicts
- No additional columns needed
- Works with JSON theme management

## Limitations

- Icons always small — avoid detailed icons with text
- Conditional formatting requires min/max — workaround with text measure for numerical icon use

## Steps

1. Export current JSON theme
2. Add icons section with SVG code (URL-encoded)
3. Reload theme in Power BI
4. Apply via Cell Elements → Icons in table conditional formatting
