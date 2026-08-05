---


title: "Power View Charts and Maps"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, power-view, pattern]
note_type: pattern
description: "Power View bar charts, column charts, pie charts, and map visualizations — inserting, resizing, and filtering. From Dunlop Chapter 6."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power View: Charts and Maps

## Bar and Column Charts

### Insert
```
Insert → Bar/Column Chart → select type
```

### Resize
Click and drag handles on the chart border.

### Multi-Year Display
Select multiple year fields to create a clustered column chart showing each year side-by-side.

## Map Visualization

Requires a **geographic field** (country, state, city). Power View resolves locations automatically.

### Setup
1. Select a geographic field
2. Power View prompts to confirm the field type
3. Drag numeric field to **Size** (for bubble map) or as a column value (for filled map)

### Filters
Use the **Filters pane** to filter data across all charts simultaneously.

## Tile View

An alternative to tables for displaying categorical groupings:

```
Select tile by → field (e.g., product category)
Each tile = one category
```

## Source Reference

Chapter 6, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
