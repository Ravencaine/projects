---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: pattern
tags: [dax, power-bi, color, conditional-formatting, matrix]
---

# DAX Color Bucket Conditional Formatting (Matrix)

Apply discrete color buckets to a correlation matrix using DAX measures — instead of Power BI's built-in gradient — so colors remain meaningful regardless of the active filter context.

## Purpose

Map each correlation value to a background and font color based on fixed |r| buckets. This ensures the color scale stays consistent even when a filtered view (e.g., one department) has a narrower range of correlations than the full dataset.

## Components

1. **Color palette measures** — `_Color *` static string measures returning hex color values
2. **`Correlation Color (Buckets)`** — background color per bucket
3. **`Correlation Font Color`** — font color per bucket (white on dark backgrounds, black on light)

## Color Palette Measures

```dax
_Color Black       = "#4B4B4B"
_Color Dark Green  = "#008080"
_Color Dark Grey   = "#605E5C"
_Color Dark Orange = "#E76F51"
_Color Light Green = "#DFF5F2"
_Color Light Grey = "#F5F5F5"
_Color Light Orange = "#FFEDE7"
_Color Mid Green  = "#00BFB2"
_Color Mid Grey   = "#E0E0E0"
_Color Mid Orange = "#F4A896"
_Color White      = "#F5F5F5"
```

## Background Color Measure

```dax
Correlation Color (Buckets) =
VAR r0  = [Correlation (Lower Triangle, No Diagonal)]
VAR r   = IF ( ISBLANK ( r0 ), BLANK(), r0 )
VAR abs = IF ( ISBLANK ( r ), BLANK(), ABS ( r ) )
RETURN
IF (
    ISBLANK ( r ),
    BLANK(),
    SWITCH (
        TRUE(),
        abs < 0.10,         [_Color White],       -- very weak/none
        r <= -0.70,         [_Color Dark Orange],  -- high negative
        r <= -0.50,         [_Color Mid Orange],   -- med negative
        r <= -0.30,         [_Color Light Orange],-- low negative
        r >=  0.70,         [_Color Dark Green],   -- high positive
        r >=  0.50,         [_Color Mid Green],    -- med positive
        r >=  0.30,         [_Color Light Green],  -- low positive
                            [_Color White]         -- default: (-0.30, 0.30)
    )
)
```

## Font Color Measure

```dax
Correlation Font Color =
VAR r0  = [Correlation (Lower Triangle, No Diagonal)]
VAR r   = IF ( ISBLANK ( r0 ), BLANK(), r0 )
VAR absr = ABS ( r )
RETURN
IF (
    ISBLANK ( r ),
    BLANK(),
    IF ( absr >= 0.5, "#FFFFFF", [_Color Black] )
)
```

## Application

In the Matrix visual, go to **Cell elements → Field Value** and assign:
- **Background color:** `Correlation Color (Buckets)`
- **Font color:** `Correlation Font Color`

## Key Behaviour

- Fixed buckets (not a gradient) mean the same |r| value always maps to the same color, regardless of which department or filter is active
- Font color switches to white when the background is dark (abs(r) >= 0.5), ensuring readability
- The `< 0.10` catch-all overrides dark-color buckets when there is essentially no correlation

## Related

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — full matrix setup
- [[correlation-lower-triangle-no-diagonal]] — `function` — the measure this colors
