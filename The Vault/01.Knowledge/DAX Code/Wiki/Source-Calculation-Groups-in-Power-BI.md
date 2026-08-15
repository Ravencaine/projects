---
created: 2026-08-06
updated: 2026-08-14
source: Calculation Groups in Power BI
source_url: https://databear.com/calculation-groups-in-power-bi/
video_file:
  - 99.System/Attachments/Video/Implementing-Calculation-Groups-Gif-1.mp4
  - 99.System/Attachments/Video/Slicer-From-Calculation-Group.mp4
note_type: source
tags: [calculation-groups, dax, tabular-editor, power-bi, time-intelligence]
---

# Calculation Groups in Power BI (Annamarie Van Wyk / Data Bear)

A Data Bear blog post by Annamarie Van Wyk explaining what Calculation Groups are, why they reduce measure duplication, and how to create them using Tabular Editor.

> **Type:** article
> **Author:** Annamarie Van Wyk (Data Bear)
> **Published:** 2022-05-03
> **URL:** https://databear.com/calculation-groups-in-power-bi/
> **Routed to:** DAX Code

## Summary

The article introduces Calculation Groups as a Tabular Editor feature that reduces measure duplication in Power BI reports. By wrapping time-intelligence expressions around `SELECTEDMEASURE()`, a single Calculation Item can apply MTD/QTD/YTD to every measure in a visual simultaneously — replacing N separate measures with one shared group. The article walks through installing external tools, creating a Calculation Group and Calculation Item in Tabular Editor, and using it on a report slicer.

## Key Claims

- Calculation Groups eliminate the need to create separate MTD/QTD/YTD versions of every measure
- Created in Tabular Editor (external tool), not directly in Power BI Desktop
- `SELECTEDMEASURE()` acts as a placeholder — any measure added to the visual is automatically wrapped by the active Calculation Item
- External tools (Tabular Editor, DAX Studio, ALM Toolkit) appear in the External Tools ribbon tab after installation
- Versions must be compatible or tools will not appear
- Calculation Groups appear as a regular table in the Power BI model after refresh
- Users can filter out unwanted Calculation Items via the filter pane or slicer

## Notable Details

- Data Bear hosts free training at databear.com/power-bi-training/
- The article embeds two video demonstrations:
  - [[99.System/Attachments/Video/Implementing-Calculation-Groups-Gif-1.mp4]] — creating and using a Calculation Group (22 seconds)
  - [[99.System/Attachments/Video/Slicer-From-Calculation-Group.mp4]] — filtering Calculation Items with a slicer (14 seconds)

## Extracted Notes

Links to notes derived from this source:

- [[Calculation-Groups]] — `atomic` — concept overview of Calculation Groups
- [[Create-a-Calculation-Group]] — `workflow` — step-by-step creation workflow
- [[Calculation-Group-External-Tools]] — `reference` — Tabular Editor, DAX Studio, ALM Toolkit reference
- [[SELECTEDMEASURE]] — `function` — extended with Calculation Group usage

## Metadata

| Field | Value |
|-------|-------|
| Source file | Calculation Groups in Power BI.md |
| Archived at | [[99.System/InboxArchive/2026-08/Calculation Groups in Power BI.md]] |
| Ingestion date | 2026-08-06 |
| Word count | ~480 |
| Attachments | [[99.System/Attachments/Video/Implementing-Calculation-Groups-Gif-1.mp4]], [[99.System/Attachments/Video/Slicer-From-Calculation-Group.mp4]] |
