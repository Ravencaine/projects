---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, spatial, distance, haversine, geography]
note_type: pattern

---

# Haversine Distance in DAX

Calculating the great-circle distance between two lat/long coordinates.

## Formula

```
a = sin^2(dlat/2) + cos(lat1) * cos(lat2) * sin^2(dlon/2)
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = R * c
```

## DAX Implementation

```dax
Haversine Distance :=
-- Assumes columns: Lat1, Lon1, Lat2, Lon2 (in decimal degrees)
VAR __R = 6371  -- Earth's radius in km
VAR __lat1 = RADIANS( [Lat1] )
VAR __lat2 = RADIANS( [Lat2] )
VAR __dlat = RADIANS( [Lat2] - [Lat1] )
VAR __dlon = RADIANS( [Lon2] - [Lon1] )
VAR __a =
    SIN( __dlat / 2 ) ^ 2
    + COS( __lat1 ) * COS( __lat2 ) * SIN( __dlon / 2 ) ^ 2
VAR __c = 2 * ATAN( SQRT( __a ) / SQRT( 1 - __a ) )
RETURN
__R * __c
```

## Notes

- Earth radius: 6371 km or 3959 miles
- Haversine is accurate for all distances including very short ones
- For most Power BI scenarios, the spherical approximation is sufficient

## Related

- [[atan2-dax-no-native]]
- [[cartesian-to-polar-coordinates-in-dax]]
- [[bearing-calculation-in-dax]]
