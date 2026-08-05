---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, spatial, polar, cartesian, coordinates, trigonometry]
---

# Cartesian to Polar Conversion in DAX

Converting Cartesian coordinates (x, y) to polar coordinates (radius, angle) using DAX.

## Concept

- **Cartesian**: (x, y) — horizontal and vertical distance from origin
- **Polar**: (r, θ) — distance from origin and angle from the positive x-axis

## Radius (r)

```dax
Radius = SQRT( [X]^2 + [Y]^2 )
```

This is the distance from the origin to the point.

## Angle (θ) in Radians

```dax
Angle Radians =
    VAR __X = [X]
    VAR __Y = [Y]
    VAR __Angle =
        SWITCH(
            TRUE(),
            __X > 0, ATAN( __Y / __X ),
            __X < 0 && __Y >= 0, PI() + ATAN( __Y / __X ),
            __X < 0 && __Y < 0, -PI() + ATAN( __Y / __X ),
            __X = 0 && __Y > 0, PI() / 2,
            __X = 0 && __Y < 0, -PI() / 2,
            0
        )
    RETURN __Angle
```

This uses ATAN (not ATAN2 — see [[atan2-dax-no-native]]) and handles all four quadrants.

## Angle in Degrees

```dax
Angle Degrees = DEGREES( [Angle Radians] )
```

## Related

- [[atan2-dax-no-native]] — ATAN2 implementation for correct quadrant handling
- [[bearing-direction-dax]] — geographic bearing calculation
- [[haversine-distance-dax]] — geographic distance
