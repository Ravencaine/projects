---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: atomic
tags: [power-bi, custom-icons, svg, table, performance, sorting, atomic]
---

# Custom Icons vs SVG Columns Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

Custom icons embedded in the JSON theme and applied via cell element formatting have three key advantages over SVG columns/measures: performance, sorting, and model complexity.

## Comparison

| | Custom Icons (theme) | SVG columns/measures |
|--|---------------------|---------------------|
| **Visual load** | Lightweight | Heavier |
| **Column sorting** | No conflict | Can break sorting |
| **Model column** | Not needed | Extra column required |
| **Theme-managed** | Yes | No |
| **Icon size** | Fixed small | Scalable |

## Why SVG columns break sorting

SVG columns return image data, which Power BI treats differently from text/numeric fields. When used in a table, they can cause the sort order of adjacent columns to behave unexpectedly.

## Why custom icons are lighter

Icons defined in the theme are rendered as URL references, not as embedded image data in every cell. The browser/renderer pulls the icon from the theme definition once.

## When to prefer SVG columns

- Need scalable or detailed icons (theme icons are always small)
- Icon design includes text or fine detail
- Need precise color control per data value

## When to prefer custom icons

- Need simple status/category indicators
- Performance is important
- Sorting integrity is critical
- No model column overhead wanted

## Related

- [[custom-icons-json-theme-cell-element-pattern]] — the pattern
- [[icon-sizing-limitation]] — the size constraint
