---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: workflow
tags: [power-map, bing-maps, geospatial, 3d, animation]
---

# Power Map: Install, Layer Tour, Bubble/Heat/Region, and Time Animation

Power Map (Excel 2013/2016, now part of 3D Maps in newer Excel) plots Excel data on Bing Maps in 2D and 3D, with geographic fields auto-detected and time-based animation.

## Prerequisites

- Excel 2013 with Power Map installed (if the Insert → Map icon is missing, search "download Power Map" from Microsoft and install)
- Data with at least one geographic field (City, State, Country, Latitude/Longitude)
- Data in an Excel table or Power Query output

## Steps

1. **Enable Power Map**
   - If not visible: File → Options → Add-Ins → Manage Excel Add-Ins → Go → check Power Map
   - Restart Excel

2. **Launch Power Map**
   - Select the data range or click any cell in the table
   - Insert → Map → Launch Power Map
   - Accept the auto-detected geographic fields (Country + State by default) → click Next
   - Or manually select: Geography →拖 fields to Geography box

3. **Add the First Layer**
   - Layer 1 pane:
     - **Height (Y-axis):** drag the numeric field to plot (e.g., Accesses, Unemployment Rate, Sales)
     - **Category:** drag a categorical field for color segmentation (e.g., OS type, Product Category)
   - The map auto-zooms to the data region

4. **Visualization Formats** (icons above the Height box)
   - **Clustered Column:** one column per geographic point
   - **Stacked Column:** stacked segments within the column (compare two metrics)
   - **Bubble:** circle sized by the numeric value
   - **Heat Map:** colored gradient overlay; adjust opacity, radius, and color scale via the gear icon
   - **Region:** choropleth map — regions shaded by value

5. **Adjust Layer Properties** (gear icon)
   - Opacity: transparency of the data overlay
   - Radius: size/spread of bubbles or heat map radius
   - Color scale: set minimum/maximum colors (e.g., green → red)
   - Uncheck boxes for Show zeroes / Show negatives / Show nulls

6. **Build a Tour**
   - Layer 1 pane → click + to add Layer 2, Layer 3, etc.
   - Each layer can have different data, visualization type, and time setting
   - Tour Editor: Name the tour; add scenes (click Scene to save current view)
   - Scenes can be sequenced with transitions (fade, dissolve, wipe)

7. **Time Animation**
   - Ensure data has a date/year column
   - Right-click the year column → Rename → change type to Date
   - Right-click the numeric value column → Set as Height
   - Check the series of year fields to animate → click Play
   - The map animates through time, updating the geographic values

8. **2D Chart View**
   - Check multiple year fields → click 2D Chart on the ribbon
   - Shows a time-series bar chart alongside the map

9. **Save and Export**
   - Play → save the tour
   - Home → Save Image or Record Video (MP4 or WMV)

## Variations

- **Multiple values:** Layer 1 shows 2011 unemployment (blue bubbles); Layer 2 shows 2012 unemployment (orange) — overlay both on the same map
- **Zoomed regional view:** Double-click a country or region on the map to zoom in; use + / - at bottom right

## Common Errors

- **Won't map:** Check that geographic fields are recognized as text (not dates or numbers); use Data → Text to Columns if needed
- **Null geographic values:** Remove or filter rows with empty geography fields before launching Power Map

## Related

- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — the full pipeline Power Map completes
- [[pivot-charts-from-pivot-tables]] — the non-geographic visualization alternative
