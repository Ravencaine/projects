---

created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, pattern, trigonometry, atan2, quadrant, spatial]

---

# ATAN2 — Four-Quadrant Arctangent (No Native DAX Function)

DAX provides ATAN but lacks the companion ATAN2 function found in most languages including Excel. ATAN2 returns the correct angle across all four Cartesian quadrants, making it essential for robotics, GPS, navigation, and game development.

## Purpose

ATAN alone is limited to angles between -90° and +90°. ATAN2 handles all four quadrants, returning angles from -180° to +180°. Implementing this in DAX requires a helper table and a SWITCH-based measure.

## Structure

**Step 1 — Create the helper table:**

```dax
ATAN2 Table =
VAR __x = SELECTCOLUMNS( GENERATESERIES( -1, 1, 1 ), "X", [Value] )
VAR __y = SELECTCOLUMNS( __x, "Y", [x] )
VAR __Result = CROSSJOIN( __x, __y )
RETURN __Result
```

This generates all four quadrants of a Cartesian plane.

**Step 2 — Create the ATAN2 measure (radians):**

```dax
ATAN2 =
VAR __x = MAX('ATAN2 Table'[X])
VAR __y = MAX('ATAN2 Table'[Y])
VAR __Result =
    SWITCH(
        TRUE(),
        __x > 0, ATAN(__y/__x),
        __x = 0 && __y >= 0, PI()/2,
        __x < 0, ATAN(__y/__x) + PI(),
        __x = 0 && __y < 0, -PI()/2,
        BLANK()
    )
RETURN __Result
```

**Step 3 — Convert to degrees:**

```dax
ATAN2 Degrees =
VAR __x = MAX('ATAN2 Table'[X])
VAR __y = MAX('ATAN2 Table'[Y])
VAR __Result =
    SWITCH(
        TRUE(),
        __x > 0, ATAN(__y/__x),
        __x = 0 && __y >= 0, PI()/2,
        __x < 0, ATAN(__y/__x) + PI(),
        __x = 0 && __y < 0, -PI()/2,
        BLANK()
    )
    * 180/PI()
RETURN __Result
```

## Example

Place X and Y columns (unsummarized) from `ATAN2 Table` alongside the `ATAN2` and `ATAN2 Degrees` measures in a Table visual.

## Notes

- The key insight is that ATAN2 adjusts the ATAN result based on which quadrant the point falls in, correcting for the inherent ambiguity of ATAN (which cannot distinguish between opposite quadrants).
- To convert radians to degrees: multiply by `180/PI()` or wrap in `DEGREES()`.
- This pattern is foundational for spatial calculations in DAX including polar-coordinate conversion, bearing calculations, and geographic direction.

## Related

- [[bearing-calculation-in-dax]]
- [[haversine-distance-in-dax]]
- [[ATAN]]
