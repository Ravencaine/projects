---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, spatial, nearest, lookup, distance]
---

# Nearest Point Detection in DAX

Finding the closest location from a list of candidates given an origin point.

## Concept

Given an origin location and a table of candidate locations, find the candidate with the minimum distance. This uses MAXX over a table of Haversine distances, selecting the row with the minimum.

## Pattern

```dax
Nearest Location =
    VAR __OriginLat = [OriginLatitude]
    VAR __OriginLon = [OriginLongitude]
    VAR __LocationsWithDistance =
        ADDCOLUMNS(
            'Locations',
            "Distance",
            [Haversine measure for this row]
        )
    VAR __Nearest = TOPN( 1, __LocationsWithDistance, [Distance], ASC )
    RETURN CONCATENATEX( __Nearest, [LocationName], ", " )
```

The TOPN(1, ..., Distance, ASC) selects the row with the smallest distance. CONCATENATEX converts the single-row table to a text name.

## Finding the Actual Distance

```dax
Distance to Nearest =
    VAR __OriginLat = [OriginLatitude]
    VAR __OriginLon = [OriginLongitude]
    VAR __MinDistance =
        MINX(
            'Locations',
            [Haversine Distance]
        )
    RETURN __MinDistance
```

## All Locations Within Radius

```dax
Locations Within Radius =
    VAR __Radius = [SearchRadius]
    RETURN
        CONCATENATEX(
            FILTER( 'Locations', [Distance] <= __Radius ),
            [LocationName],
            ", "
        )
```

## Related

- [[haversine-distance-dax]] — the underlying distance calculation
- [[transitive-closure-dax]] — all pairs within a threshold
- [[dax-index-pattern-deckler]] — TOPN pattern for selecting extremes
