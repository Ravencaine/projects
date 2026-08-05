---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: reference
tags: [dax, spatial, distance, trigonometry, geography]
---

# Distance Calculations in DAX — Overview

DAX has no native spatial functions, but all geographic calculations can be implemented using trigonometry and DAX's mathematical functions. Ch12 of DAX for Humans covers the full spatial calculation suite.

## The Core Challenge

Geographic coordinates are angles (latitude and longitude in degrees). Distance and direction calculations require:
1. Converting degrees to radians (RADIANS())
2. Trigonometric functions (SIN, COS, ATAN, ATAN2)
3. The arc functions (ASIN, ACOS) for inverse calculations

## Key Patterns in This Series

| Pattern | File | Description |
|---------|------|-------------|
| ATAN2 | [[atan2-dax-no-native]] | Four-quadrant arctangent (DAX has ATAN but not ATAN2) |
| Cartesian to Polar | [[cartesian-to-polar-conversion]] | (x,y) → (radius, angle) |
| Haversine Distance | [[haversine-distance-dax]] | Great-circle distance between lat/long points |
| Bearing/Direction | [[bearing-direction-dax]] | Compass direction between two points |
| Nearest Point | [[nearest-point-dax]] | Find closest match from a list of locations |
| Transitive Closure | [[transitive-closure-dax]] | All pairs within a distance threshold (graph reachability) |
| Box Sizes | [[box-size-optimization-dax]] | Optimal shipping box based on item dimensions |

## Prerequisites

All spatial calculations require:
- Latitude and longitude columns in decimal degrees
- EARTH_RADIUS constant (typically 6,371 km or 3,959 miles)
- RADIANS() wrapper on all degree inputs
- DEGREES() wrapper if converting back to degrees for display

## Related Functions

- RADIANS(), DEGREES() — degree/radian conversion
- SIN(), COS(), TAN() — basic trig
- ASIN(), ACOS(), ATAN() — inverse trig
- ATAN2() — implemented from ATAN (no native DAX version)
- PI() — π constant
- SQRT() — square root
