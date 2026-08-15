---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
source_url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-Power-BI-reporting-with-the-new-date-picker/ba-p/5295674
note_type: source
tags: [power-bi, date-picker, slicer, relative-dates, fabric, datazoe]
---

# Deep dive: the new date picker slicer option (Preview) (Microsoft Fabric / DataZoe)

> **Type:** article
> **Author:** Microsoft Fabric / DataZoe
> **Published:** 2026-07-16
> **URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-Power-BI-reporting-with-the-new-date-picker/ba-p/5295674
> **Routed to:** Power BI

## Summary

Date Picker Slicer (Preview) — a new slicer style combining relative date ranges (rolling forward with data refresh) and manual overrides. Dual summary shows filtered date range vs selected range. Supports single-line compact layout, single date selection, slider, and overlay calendar. Relative ranges persist when pinned to dashboards.

## Key Claims

### Enabling
- Enable preview: File → Options and settings → Options → Preview features → Date picker slicer
- Available in Slicer visual → Visual → Slicer settings → Options → Date picker
- Requires a date column in the slicer field

### Relative Ranges
- Anchor: Last date, First date, or Today
- Offset options (e.g., Last 30 days starting 5 days back)
- Automatically moves forward as data refreshes
- Relative range continues to apply when pinned to dashboard (unlike filter pane relative dates)

### Viewer Capabilities
- Pick different relative range, reset to published default
- Manual date range from calendar
- Single date: select same date twice
- Slider to adjust range
- Slider can be moved back/forth to offset the range

### Dual Summary
- Top summary: actual date range the data column is filtered to
- Bottom summary: the relative or manual range selected
- If relative range falls outside available data → shows dates inside available data + tooltip explaining incompleteness

### Persistence
- Default: viewer filters persist (report consumers continue where they left off)
- Toggle off: viewer filter persistence → reset to defaults on each load
- Desktop: File → Options → Current File Report Settings
- Web: File → Settings

## Metadata

| Field | Value |
|-------|-------|
| Source file | Deep dive into Power BI reporting with the new date picker slicer option (Preview).md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
