---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, spatial, haversine, distance, geography, trigonometry]
---

# Haversine Distance in DAX

The Haversine formula calculates the great-circle distance between two points on Earth's surface given their latitude and longitude. DAX has no native geographic functions — Haversine must be built from scratch.

## Purpose

Great-circle distance = shortest distance over Earth's surface along a spherical path (vs Euclidean which would give a straight-line chord through the earth). Essential for logistics, territory analysis, customer proximity, and route optimization.

## Formula

```dax
Haversine Distance (Miles) =
    VAR __Lat1 = RADIANS( 'Locations'[Latitude1] )
    VAR __Lat2 = RADIANS( 'Locations'[Latitude2] )
    VAR __Lon1 = RADIANS( 'Locations'[Longitude1] )
    VAR __Lon2 = RADIANS( 'Locations'[Longitude2] )
    VAR __DeltaLat = __Lat2 - __Lat1
    VAR __DeltaLon = __Lon2 - __Lon1
    VAR __A =
        SIN( __DeltaLat / 2 ) ^ 2
        + COS( __Lat1 ) * COS( __Lat2 ) * SIN( __DeltaLon / 2 ) ^ 2
    VAR __C = 2 * ATAN( SQRT( __A ), SQRT( 1 - __A ) )
    VAR __R = 3959   -- Earth's radius in miles (6371 km for kilometers)
    RETURN __R * __C
```

## Step-by-Step

1. **RADIANS()**: convert degrees to radians (DAX trig functions expect radians)
2. **Δlat, Δlon**: differences between the two points
3. **a**: the Haversine intermediate value (sine of half the chord length squared)
4. **c**: great-circle angular distance in radians (the arccosine-like term)
5. **R × c**: multiply angular distance by Earth's radius

## Alternative: Direct Haversine Measure

```dax
Haversine =
    VAR __Lat1 = RADIANS( [Lat1] )
    VAR __Lat2 = RADIANS( [Lat2] )
    VAR __D =
        SIN( ( __Lat2 - __Lat1 ) / 2 ) ^ 2
        + COS( __Lat1 ) * COS( __Lat2 )
          * SIN( ( RADIANS( [Lon2] - [Lon1] ) ) / 2 ) ^ 2
    RETURN 12742 * ASIN( SQRT( __D ) / 2 )  -- diameter × arcsin in km
```

## Constants

| Unit | Earth's Radius | Earth's Diameter |
|------|---------------|-----------------|
| Miles | 3,959 mi | 7,918 mi |
| Kilometers | 6,371 km | 12,742 km |
| Nautical miles | 3,440 nm | 6,880 nm |

## Related

- [[atan2-dax-no-native]] — directional angle calculation
- [[nearest-point-dax]] — closest location
- [[bearing-direction-dax]] — compass direction
- [[distance-calculation-dax-overview]] — full spatial calculation suite
