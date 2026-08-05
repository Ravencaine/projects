---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, spatial, logistics, optimization, packing]
---

# Box Size Optimization in DAX

Selecting the optimal shipping box based on item dimensions using DAX spatial calculations.

## Concept

Given a set of items with length, width, height, and a set of available boxes with their dimensions, find the smallest box that can fit all items. This combines spatial calculations (volume, area, fitting logic) with DAX table manipulation.

## Components

1. **Volume check**: Total item volume ≤ box volume
2. **Max dimension check**: Longest item dimension ≤ box's corresponding dimension
3. **Side fit check**: For 2D projection, items must physically fit within box footprint

## Pattern Structure

```dax
Box Fit =
    VAR __Items = SUMMARIZE( 'OrderItems', 'OrderItems'[ItemKey], "Vol", 'OrderItems'[Volume], "MaxL", 'OrderItems'[Length], "MaxW", 'OrderItems'[Width], "MaxH", 'OrderItems'[Height] )
    VAR __TotalVolume = SUMX( __Items, [Vol] )
    VAR __MaxLength = MAXX( __Items, [MaxL] )
    VAR __MaxWidth = MAXX( __Items, [MaxW] )
    VAR __MaxHeight = MAXX( __Items, [MaxH] )
    VAR __Box = FILTER( 'Boxes', 'Boxes'[Volume] >= __TotalVolume && 'Boxes'[Length] >= __MaxLength && 'Boxes'[Width] >= __MaxWidth && 'Boxes'[Height] >= __MaxHeight )
    VAR __BestBox = TOPN( 1, __Box, [Volume], ASC )
    RETURN CONCATENATEX( __BestBox, [BoxName], ", " )
```

## Related

- [[haversine-distance-dax]] — distance calculations
- [[cartesian-to-polar-conversion]] — coordinate conversion
- [[multi-column-aggregation-dax]] — wide-to-tall reshaping
