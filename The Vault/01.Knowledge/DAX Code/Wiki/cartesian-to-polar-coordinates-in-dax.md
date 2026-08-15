---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, math, spatial, cartesian, polar, atan2]
note_type: pattern

---

# Cartesian to Polar Coordinates in DAX

Converting Cartesian (x, y) coordinates to polar (r, theta) format.

## Formulas

```
r     = sqrt(x^2 + y^2)
theta = ATAN2(y, x)
```

## DAX Implementation

```dax
Radius :=
SQRT( POWER( [X], 2 ) + POWER( [Y], 2 ) )

Angle (Radians) := [Custom ATAN2 Implementation]
Angle (Degrees) := [Angle (Radians)] * 180 / PI()
```

## Use Cases

- Converting screen coordinates to angles for radial charts
- Computing distances from a reference point
- Direction analysis (e.g., wind direction from u/v components)

## Notes

- ATAN2 returns angles from -PI to PI (or -180 to 180 in degrees)
- North = 0 degrees in compass bearings; add 90 degrees to convert from math convention

## Related

- [[atan2-dax-no-native]]
- [[bearing-calculation-in-dax]]
- [[haversine-distance-in-dax]]
