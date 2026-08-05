---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "geography", "coordinate", "osgb", "uk", "spatial"]
note_type: pattern

---

# Ordnance Survey Grid in DAX

Converting UK Ordnance Survey National Grid references to lat/long.

## Purpose

OS Grid references (e.g., "TQ 399 817") are commonly used in UK geographic data.

## DAX Pattern (Partial)

```dax
-- OS Grid to Lat/Long requires Eastings/Northings extraction
-- E = 2-letter prefix + 3-digit Easting
-- N = 2-letter prefix + 3-digit Northing

OSGrid to Lat :=
VAR __E = [Easting]
VAR __N = [Northing]
-- Conversion uses complex geodesic formulas
-- Implement in Power Query for production use
RETURN
[LatFromEN]
```

## Notes

- Full OS Grid to WGS84 conversion requires a complex algorithm
- For Power BI mapping, use Power Query or a pre-computed lookup table

## Related

- [[haversine-distance-in-dax]]
- [[cartesian-to-polar-coordinates-in-dax]]
