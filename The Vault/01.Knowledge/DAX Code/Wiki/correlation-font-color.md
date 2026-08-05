---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, correlation, color, conditional-formatting, matrix]
---

# Correlation Font Color

Returns black or white as the font color for a correlation matrix cell, based on the background brightness of the corresponding `Correlation Color (Buckets)` value.

## Signature

```dax
Correlation Font Color :=
VAR r0   = [Correlation (Lower Triangle, No Diagonal)]
VAR r    = IF ( ISBLANK ( r0 ), BLANK(), r0 )
VAR absr = ABS ( r )
RETURN
IF (
    ISBLANK ( r ),
    BLANK(),
    IF ( absr >= 0.5, "#FFFFFF", [_Color Black] )
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Correlation (Lower Triangle, No Diagonal)]` | measure | The display measure used on the Matrix visual |

## Returns

`"#FFFFFF"` (white) when `|r| >= 0.5` (dark background); `"#4B4B4B"` (black) otherwise.

## Notes

- Applied via Matrix visual → Cell elements → Field Value → Font color
- The 0.5 threshold matches the boundary between mid and dark color buckets, ensuring readability on both dark and light backgrounds

## Related

- [[dax-color-bucket-conditional-formatting-matrix]] — `pattern` — full setup
- [[correlation-color-buckets]] — `function` — the paired background color measure
- [[color-palette-measures-static-hex-strings]] — `function` — `_Color Black` constant
