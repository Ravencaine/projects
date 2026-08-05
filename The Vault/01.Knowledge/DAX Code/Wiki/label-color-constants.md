---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: snippet
tags: [dax, snippet, color, constants]
---

# Label Color Constants

Hex color constants used for chart label formatting — font and background colors for variance indicators.

## Code

```dax
_Color Dark Green    = "#31D286"
_Color Dark Red      = "#F05660"
_Color Text Secondary = "#79797C"
```

## When to Use

- As color targets for conditional font color (`Label Font Color` pattern)
- As base colors for conditional label background series (set via Format pane, not via DAX)
- Stored under `_Constants/Colors` in the PBIX measure tree

## Notes

These are named constants for human readability in the measure tree. They are used as return values in SWITCH measures, which return the string name — Power BI resolves the name to the hex value through per-series formatting bindings.

For label **background** formatting (the main technique), the color is set in the Format pane per-series, not through DAX measures.

## Related

- [[Label-Font-Color-SWITCH]]
- [[Column-Color]]
