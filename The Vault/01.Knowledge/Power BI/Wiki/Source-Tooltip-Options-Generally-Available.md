---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
source_url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-tooltip-options-in-Power-BI-visuals-Generally/ba-p/5255518
note_type: source
tags: [power-bi, tooltip, sentence-format, report-page-tooltip, field-parameters, drillthrough, fabric, datazoe]
---

# Deep dive: tooltip options in Power BI visuals (Generally Available) (Microsoft Fabric / DataZoe)

> **Type:** article
> **Author:** Microsoft Fabric / DataZoe
> **Published:** 2026-07-06
> **URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-tooltip-options-in-Power-BI-visuals-Generally/ba-p/5255518
> **Routed to:** Power BI

## Summary

5-tier tooltip progression: Default visual → Tooltip field well → Tooltip fields only / Sentence format only (GA) → Report page tooltip. Help tooltip icon explains the visual itself. Sentence format supports field references, bold values, field parameters, and drillable hierarchies.

## Tooltip Type Progression (Least → Most Custom)

| Tier | Type | Control |
|------|------|---------|
| 1 | Default visual tooltip | Power BI builds from visual fields |
| 2 | Tooltip field well | Add extra fields to enrich default |
| 3 | Tooltip fields only (GA) | Curate exact field list; hide visual-encoded fields |
| 3 | Sentence format (GA) | Write hover content as a sentence with {field} references |
| 4 | Report page tooltip | Replace entirely with custom report page |

## Key Claims

### Tooltip Fields Only
- Format visual → General → Tooltips → Options → Tooltip fields only = ON
- Shows only fields in Tooltip field well; visual's encoded fields hidden
- Use when: field in visual for formatting/sorting but not needed on hover; surfacing supplementary fields like YoY without listing every series

### Sentence Format
- Format visual → General → Tooltips → Options → Sentence format
- Template: plain text + {FieldName} references; Power BI substitutes hovered value
- Bold values: ON highlights substituted values
- Appears below existing tooltip fields by default
- Sentence format only = tooltip shows sentence only

### Field Parameters in Sentences
- {Field parameter} → selected field name
- {Field parameter Fields} → value of selected field (word "Fields" matches parameter's value column name)

### Drillable Hierarchy Sentences
- Add ISINSCOPE + SWITCH + SELECTEDVALUE measure to Tooltip field well
- Reference in template: {Segment or Product Drill} reads correctly at every drill level

### Report Page Tooltips
- Design report page → Page information → Allow use as tooltip
- On consuming visual: Format visual → General → Tooltips → Options → Type = Report page → pick page
- Filters from hovered data point flow through automatically
- NOT interactive (no slicers, no clicking inside)
- For interactive filtered views: use Drillthrough page instead

### Help Tooltip
- Header icons → Icons → Help tooltip
- Shows typed text or report page
- Explains the visual itself (not the data point)
- Report page as Help tooltip: use animated GIF background for quick demo walkthrough

### Chart-Specific Tooltips
- Options card → Chart-specific tooltips (ON by default)
- Adds chart-type context (e.g., % of first/previous on funnel)
- Turn off to rely on curated fields/sentence only

## Metadata

| Field | Value |
|-------|-------|
| Source file | Deep dive into tooltip options in Power BI visuals (Generally Available).md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
