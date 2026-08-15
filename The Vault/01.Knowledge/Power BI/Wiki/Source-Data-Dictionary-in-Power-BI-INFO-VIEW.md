---
created: 2026-08-09
updated: 2026-08-09
source: "Data Dictionary in Power BI Create One with INFO.VIEW.md"
source_url: https://databear.com/data-dictionary-in-power-bi/
note_type: source
tags: [power-bi, data-dictionary, metadata, info.view, documentation, boniface-muchendu]
---

# Data Dictionary in Power BI: Create One with INFO.VIEW

Use the INFO.VIEW DAX functions (October 2024) to programmatically extract model metadata and build a dynamic, self-updating data dictionary directly inside Power BI Desktop.

> **Type:** tutorial
> **Author:** Boniface Muchendu
> **Published:** 2025-07-18
> **URL:** https://databear.com/data-dictionary-in-power-bi/
> **Routed to:** Power BI

## Summary

INFO.VIEW functions extract model metadata as table outputs. The article shows how to create four separate metadata tables (Measures, Tables, Columns, Relationships) and optionally combine them into a single unified data dictionary using SELECTCOLUMNS + UNION. Adding descriptions to measures in model view enriches the dictionary automatically. A dedicated report page with slicers makes the dictionary interactive.

## Key Claims

- INFO.VIEW functions are dynamic — they update automatically as the model changes
- Four variants: INFO.VIEW.MEASURES, INFO.VIEW.TABLES, INFO.VIEW.COLUMNS, INFO.VIEW.RELATIONSHIPS
- Measure descriptions entered in the Properties pane appear in INFO.VIEW.MEASURES on refresh
- Combining all four with SELECTCOLUMNS + UNION into one table enables slicer-based filtering
- A dedicated report page with text slicer and type slicer makes the dictionary explorable by non-technical users

## Step Summary

1. Create `ModelMeasures = INFO.VIEW.MEASURES()`
2. Add descriptions to measures in Model view (Properties pane)
3. Refresh to see descriptions in the table
4. Create `ModelTables = INFO.VIEW.TABLES()`, `ModelColumns = INFO.VIEW.COLUMNS()`, `ModelRelationships = INFO.VIEW.RELATIONSHIPS()`
5. Combine into one `DataDictionary` table using SELECTCOLUMNS + UNION + Type column
6. Build a report page with table visuals and slicers

## Extracted Notes

- [[INFO-VIEW-Combined-Data-Dictionary-Workflow]] — `pattern` — SELECTCOLUMNS + UNION to merge all four INFO.VIEW outputs into a single filterable data dictionary

## Metadata

| Field | Value |
|-------|-------|
| Source file | Data Dictionary in Power BI Create One with INFO.VIEW.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~700 |
