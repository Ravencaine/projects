---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, correlation, color, conditional-formatting, matrix]
---

# Correlation Color (Buckets)

Returns a hex color string based on the correlation value, mapped to fixed |r| buckets. Used as the background color in a correlation matrix visual.

## Signature

```dax
Correlation Color (Buckets) :=
VAR r0  = [Correlation (Lower Triangle, No Diagonal)]
VAR r   = IF ( ISBLANK ( r0 ), BLANK(), r0 )
VAR abs = IF ( ISBLANK ( r ), BLANK(), ABS ( r ) )
RETURN
IF (
    ISBLANK ( r ),
    BLANK(),
    SWITCH (
        TRUE(),
        abs < 0.10,         [_Color White],
        r <= -0.70,         [_Color Dark Orange],
        r <= -0.50,         [_Color Mid Orange],
        r <= -0.30,         [_Color Light Orange],
        r >=  0.70,         [_Color Dark Green],
        r >=  0.50,         [_Color Mid Green],
        r >=  0.30,         [_Color Light Green],
                            [_Color White]
    )
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Correlation (Lower Triangle, No Diagonal)]` | measure | The display measure used on the Matrix visual |

## Returns

A hex color string (e.g., `"#E76F51"`) or `BLANK()`.

## Color Mapping

| Condition | Color | Meaning |
|-----------|-------|---------|
| `abs(r) < 0.10` | `#F5F5F5` (white) | negligible / no correlation |
| `r <= -0.70` | `#E76F51` (dark orange) | high negative |
| `r <= -0.50` | `#F4A896` (mid orange) | medium negative |
| `r <= -0.30` | `#FFEDE7` (light orange) | low negative |
| `r >= 0.70` | `#008080` (dark green) | high positive |
| `r >= 0.50` | `#00BFB2` (mid green) | medium positive |
| `r >= 0.30` | `#DFF5F2` (light green) | low positive |
| `-0.30 < r < 0.30` | `#F5F5F5` (white) | default: not noteworthy |

## Notes

- Applied via Matrix visual → Cell elements → Field Value → Background color
- Static buckets ensure consistent color mapping regardless of filter context — unlike a gradient which rescales to the min/max of the visible data

## Related

- [[dax-color-bucket-conditional-formatting-matrix]] — `pattern` — full setup
- [[color-palette-measures-static-hex-strings]] — `function` — the color constants used
- [[correlation-font-color]] — `function` — paired font color measure
