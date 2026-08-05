---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, spatial, bearing, direction, navigation, trigonometry]
---

# Bearing and Direction in DAX

Calculating the compass direction (bearing) between two geographic points using DAX.

## Concept

Bearing (or azimuth) is the compass direction from point A to point B, measured in degrees clockwise from North (0°). For example:
- 0° = North
- 90° = East
- 180° = South
- 270° = West

## Formula

Using ATAN2 to compute bearing:

```dax
Bearing =
    VAR __Lat1 = RADIANS( 'Points'[Latitude1] )
    VAR __Lon1 = RADIANS( 'Points'[Longitude1] )
    VAR __Lat2 = RADIANS( 'Points'[Latitude2] )
    VAR __Lon2 = RADIANS( 'Points'[Longitude2] )
    VAR __DeltaLon = __Lon2 - __Lon1
    VAR __X = COS( __Lat2 ) * SIN( __DeltaLon )
    VAR __Y = COS( __Lat1 ) * SIN( __Lat2 ) - SIN( __Lat1 ) * COS( __Lat2 ) * COS( __DeltaLon )
    VAR __Bearing = MOD( 360 + 180 / PI() * ATAN( __X / __Y ), 360 )
    RETURN __Bearing
```

The MOD wraps the result to the 0–360 range. The ATAN handles the quadrant adjustment based on the signs of X and Y.

## Compass Direction Labels

```dax
Compass Direction =
    VAR __Bearing = [Bearing]
    VAR __Direction = SWITCH( TRUE(),
        __Bearing < 22.5, "N",
        __Bearing < 67.5, "NE",
        __Bearing < 112.5, "E",
        __Bearing < 157.5, "SE",
        __Bearing < 202.5, "S",
        __Bearing < 247.5, "SW",
        __Bearing < 292.5, "W",
        __Bearing < 337.5, "NW",
        "N"
    )
    RETURN __Direction
```

## Related

- [[atan2-dax-no-native]] — ATAN2 implementation
- [[haversine-distance-dax]] — distance between two points
- [[cartesian-to-polar-conversion]] — x,y to radius,angle conversion
