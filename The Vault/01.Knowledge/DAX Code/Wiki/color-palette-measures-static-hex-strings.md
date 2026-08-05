---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, color, palette, measure]
---

# Color Palette Measures (Static Hex Strings)

A set of measures that return hardcoded hex color strings, used as building blocks for DAX-driven conditional formatting.

## Signatures

```dax
_Color Black         = "#4B4B4B"
_Color Dark Green    = "#008080"
_Color Dark Grey     = "#605E5C"
_Color Dark Orange   = "#E76F51"
_Color Light Green   = "#DFF5F2"
_Color Light Grey    = "#F5F5F5"
_Color Light Orange  = "#FFEDE7"
_Color Mid Green     = "#00BFB2"
_Color Mid Grey      = "#E0E0E0"
_Color Mid Orange    = "#F4A896"
_Color White         = "#F5F5F5"
```

## Returns

Each measure returns a single text string: a hex color code.

## Notes

- These are **measures** (not constants) so they can be referenced by name inside other measures without circular dependency
- String values are returned unquoted when used in DAX string concatenation for HTML output
- Naming convention: `_Color <Name>` signals these are utility/helper measures

## Related

- [[dax-color-bucket-conditional-formatting-matrix]] — `pattern` — uses these measures for matrix color buckets
- [[scatter-subtitle-html-dynamic-label-badge]] — `function` — uses the same palette for HTML-based labels
