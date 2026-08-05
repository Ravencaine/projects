---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: pattern
tags: [powerbi, dax, correlation, conditional-formatting, color]
---

# Correlation Color Buckets

DAX measures that apply bucket-based conditional coloring to correlation matrix cells — applied via **Cell elements → Field value** on the Matrix visual.

> DAX-based color measures are used instead of Power BI's built-in gradient so that colors remain accurate when department-level filters narrow the range of correlation values.

## Color Palette Measures

```c
_Color Black      = "#4B4B4B"
_Color Dark Green = "#008080"
_Color Dark Grey  = "#605E5C"
_Color Dark Orange= "#E76F51"
_Color Light Green= "#DFF5F2"
_Color Light Grey = "#F5F5F5"
_Color Light Orange= "#FFEDE7"
_Color Mid Green  = "#00BFB2"
_Color Mid Grey  = "#E0E0E0"
_Color Mid Orange= "#F4A896"
_Color White     = "#F5F5F5"
```

## Cell Background Measure

```c
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
        abs < 0.10,         [_Color White],        -- very weak/none
        r <= -0.70,         [_Color Dark Orange],   -- high negative
        r <= -0.50,         [_Color Mid Orange],    -- medium negative
        r <= -0.30,         [_Color Light Orange],  -- low negative
        r >=  0.70,         [_Color Dark Green],    -- high positive
        r >=  0.50,         [_Color Mid Green],     -- medium positive
        r >=  0.30,         [_Color Light Green],   -- low positive
                            [_Color White]          -- default (-0.30, 0.30)
    )
)
```

## Font Color Measure

```c
Correlation Font Color =
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

## Application

In the Matrix visual → **Cell elements** → **Field value**:
- Background → `Correlation Color (Buckets)`
- Font color → `Correlation Font Color`

## Why DAX over Built-in Gradient?

- **Built-in gradient** rescales to the visible range — a 0.6 in a department with a range of 0.4–0.7 would show as "high" in orange, which is misleading.
- **DAX buckets** use fixed thresholds regardless of filter context, so 0.6 always maps to the same color.

## Related

- [[lower-triangle-no-diagonal-correlation]]
