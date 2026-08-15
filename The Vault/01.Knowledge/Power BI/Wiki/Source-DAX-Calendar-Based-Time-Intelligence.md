---
created: 2026-08-09
updated: 2026-08-09
source: "DAX Calendar-Based Time Intelligence What You Must Know Before Editing Your Model.md"
source_url: https://medium.com/riccardo-perico/dax-calendar-based-time-intelligence-what-you-must-know-before-editing-your-model-51f14c653c76
note_type: source
tags: [power-bi, dax, time-intelligence, calendar-based, lineage, TMDL, preview-feature]
---

# DAX Calendar-Based Time Intelligence: What You Must Know Before Editing Your Model

Calendar-based time intelligence (preview, September 2024) requires caution when modifying date table structure — deleting columns causes broken references that block model processing.

> **Type:** article
> **Author:** Riccardo Perico
> **Published:** 2025-11-20
> **URL:** https://medium.com/riccardo-perico/dax-calendar-based-time-intelligence-what-you-must-know-before-editing-your-model-51f14c653c76
> **Routed to:** Power BI

## Summary

Calendar-based time intelligence is a DAX preview feature (September 2024) that handles custom calendars, non-standard date hierarchies, and sparse calendars without imposing structural rules. The article focuses on a critical gotcha: deleting a column used in the calendar definition breaks the model because Power BI does not surface missing references in the calendar UI. Users must manually delete broken mappings in TMDL View to recover.

## Key Claims

- Calendar-based time intelligence supports any calendar (custom weeks, non-standard hierarchies, sparse calendars)
- Power BI handles column renaming correctly — the lineage tag remains unchanged
- Deleting a column used in a calendar definition causes processing failure with error: "CalendarColumnReference object refers to a column that has been deleted"
- After a failed processing, the new column does not exist yet — users are stuck
- The calendar UI does not show missing references; TMDL View or manual repair is required
- Using Bravo for Power BI reduces the risk of structural changes

## Extracted Notes

- [[Calendar-Based-Time-Intelligence-Column-Deletion-Gotcha]] — `gotcha` — deleting calendar columns breaks references; rename instead

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Calendar-Based Time Intelligence What You Must Know Before Editing Your Model.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~550 |
| External refs | SQLBI calendar article, MS Learn UDF overview |
