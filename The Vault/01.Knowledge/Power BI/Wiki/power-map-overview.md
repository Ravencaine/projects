---


title: "Power Map Overview"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, power-map, visualization]
note_type: pattern
description: "Power Map — 2D map, 3D globe, bubble view, heat map, region view, stacked/clustered columns. From Dunlop Chapter 9."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Map

Geospatial visualization tool (Excel 2013) that plots data on 2D maps or 3D globes. Runs as a separate interface accessed via Insert → Map → Launch Power Map.

## Installation

Power Query is required. Enable via:
```
File → Options → Add-Ins → COM Add-Ins → Microsoft Power Map for Excel
```

## Visualization Types

| Format | Description |
|--------|-------------|
| Stacked Column | Bars stacked vertically at geographic location |
| Clustered Column | Bars side-by-side (used when multiple values per location) |
| Bubble | Circles sized by a numeric value |
| Heat Map | Color gradient showing density/intensity |
| Region | Filled geographic regions (country/state level) |

## Components

| Section | Purpose |
|---------|---------|
| Layer | One dataset mapped |
| Map | The geographic plot |
| Tour | A sequence of scenes with animations |
| Scene | A single view of one or more layers |

## Source Reference

Chapter 9, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
