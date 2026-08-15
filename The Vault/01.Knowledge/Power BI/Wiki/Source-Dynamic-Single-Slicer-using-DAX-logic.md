---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Single Slicer using DAX logic.md"
source_url: https://databear.com/dynamic-single-slicer-using-dax-logic/
author: Boniface Muchendu
note_type: source
tags: [power-bi, slicer, dynamic-slicer, measures-table, boniface-muchendu]
---

# Dynamic Single Slicer using DAX logic (Data Bear)

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2022-10-30
> **URL:** https://databear.com/dynamic-single-slicer-using-dax-logic/
> **Routed to:** Power BI

## Summary

Combines multiple column slicers into a single dynamic slicer using a disconnected measures table with an index column and SELECTEDVALUE DAX logic. Alternative to Dynamic M Query Parameters when M parameters cannot be used. Demonstrated with AdventureWorksDW2012 — 6 columns combined into one slicer.

## Key Steps

1. Import dataset (FactInternetSales from SQL Server)
2. Create Calendar table via CALENDAR()
3. Create disconnected measures table with index column via Enter Data
4. Write DAX SELECTEDVALUE logic
5. Build slicer from measures table + clustered column chart

## Key Claims

- Combines any number of slicers into one using a disconnected table
- Measures table (AllMeasuresTable) stores metric names + index
- Index column enables order/priority
- SELECTEDVALUE returns the selected measure name
- Clustered column chart uses the DAX measure in Values; visuals blank until selection made

## Metadata

| Field | Value |
|-------|-------|
| Source file | Dynamic Single Slicer using DAX logic.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
