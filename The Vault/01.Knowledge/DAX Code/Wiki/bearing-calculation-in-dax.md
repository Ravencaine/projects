---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, navigation, bearing, angle, compass]
note_type: pattern

---

# Bearing Calculation in DAX

Calculating the compass bearing from one lat/long to another.

## Formula

```
theta = atan2( sin(dlon) * cos(lat2), cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(dlon) )
bearing = (theta * 180/PI() + 360) % 360
```

## DAX Pattern

```dax
Bearing :=
VAR __lat1 = RADIANS( [Lat1] )
VAR __lat2 = RADIANS( [Lat2] )
VAR __dlon = RADIANS( [Lon2] - [Lon1] )
VAR __x = SIN( __dlon ) * COS( __lat2 )
VAR __y = COS( __lat1 ) * SIN( __lat2 ) - SIN( __lat1 ) * COS( __lat2 ) * COS( __dlon )
VAR __theta = ATAN2( __x, __y )
VAR __bearing = MOD( __theta * 180 / PI() + 360, 360 )
RETURN
__bearing
```

## Notes

- Returns 0 = North, 90 = East, 180 = South, 270 = West
- DAX has no native ATAN2 — use the SWITCH pattern from [[atan2-dax-no-native]]
- Use with [[haversine-distance-dax]] for full navigation calculations

## Related

- [[atan2-dax-no-native]]
- [[haversine-distance-in-dax]]
- [[cartesian-to-polar-coordinates-in-dax]]
