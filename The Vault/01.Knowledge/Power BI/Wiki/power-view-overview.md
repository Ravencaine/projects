---


title: "Power View Overview"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, power-view, visualization]
note_type: pattern
description: "Power View — design surface, fields pane, filters pane, visualizations. Single-table and relational examples from the Northwind database. From Dunlop Chapter 6."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power View

An interactive data visualization tool built into Excel 2013. Runs inside Excel as a sheet type (not a separate application in 2013). Creates reports with tables, matrices, charts, and maps.

## Interface Components

### Design Surface

The main canvas where visualizations are placed and arranged. Click any empty area to deselect.

### Fields Pane

Lists all tables and fields from the Data Model. Drag fields onto the design surface to add them to visualizations.

### Filters Pane

Filters apply to the **entire report** (not individual charts). Configure top N filters, field filters, and comparison filters.

## Visualization Types

| Type | Best For |
|------|---------|
| Table | Tabular data, summarized lists |
| Matrix | Two-dimensional cross-tabulation (like PivotTable) |
| Bar Chart | Comparing categories |
| Column Chart | Time series, categorical comparison |
| Map | Geographic data (requires location field) |
| Tile | Section headers / navigation within a report |
| Multiple Years | Time-series comparison (select multiple year fields) |

## Source Reference

Chapter 6, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
