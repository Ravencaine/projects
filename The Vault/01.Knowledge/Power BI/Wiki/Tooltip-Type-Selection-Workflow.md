---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
note_type: workflow
tags: [power-bi, tooltip, tooltip-type-selection, workflow]
---

# Tooltip Type Selection — 5-Tier Decision Workflow

> **Type:** workflow
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-06

## Overview

Power BI offers 5 tooltip types ranging from zero-config defaults to fully custom report pages. Choose based on how much control the report needs.

## Decision Tree

```
Does the default tooltip show what users need?
├── YES → Use Default visual tooltip
└── NO
    ├── Just need a few extra fields?
    │   └── Use Tooltip field well
    ├── Need to hide some visual fields?
    │   └── Use Tooltip fields only
    ├── Need narrative/calculated context?
    │   └── Use Sentence format
    └── Need visuals, KPIs, images?
        └── Use Report page tooltip
```

## Tier 1 — Default Visual Tooltip

**When:** Standard hover is sufficient.

**Steps:** Nothing — Power BI builds it automatically from visual fields.

**Formatting:** Format visual → General → Tooltips → Text, Background, Actions.

## Tier 2 — Tooltip Field Well

**When:** Default is mostly right but needs enrichment (e.g., add YoY change).

**Steps:**
1. Select visual
2. Drag fields to **Tooltip** field well in the Fields pane
3. Fields appear in tooltip below default fields

## Tier 3a — Tooltip Fields Only

**When:** A field is in the visual for formatting/sorting but shouldn't appear on hover; or want to surface only specific supplementary fields.

**Steps:**
1. Format visual → General → Tooltips → Options
2. Turn ON **Tooltip fields only**
3. Add only the desired fields to the Tooltip field well

## Tier 3b — Sentence Format

**When:** Want a written sentence that mixes text + data values (e.g., "Sales changed by $3.7M (44%) since last year").

**Steps:**
1. Format visual → General → Tooltips → Options
2. Turn ON **Sentence format**
3. Write template using `{FieldName}` for each field reference
4. Toggle **Bold values** to highlight substituted values
5. Toggle **Sentence format only** to hide all other fields

## Tier 4 — Report Page Tooltip

**When:** Need multiple visuals, KPIs, images, or complex layouts in the tooltip.

**Steps:**

*On the tooltip page:*
1. Design the report page (visuals, text boxes, KPIs, images)
2. View → Page information
3. Turn ON **Allow use as tooltip**

*On the consuming visual:*
1. Select visual
2. Format visual → General → Tooltips → Options
3. Set **Type** = **Report page**
4. Pick the tooltip page from the dropdown

**Note:** Filters from the hovered data point flow through automatically.

## Tier 5 — Help Tooltip (separate)

**When:** Need to explain the visual itself to new users (not the data point).

**Steps:**
1. Format visual → General → Header icons → Icons
2. Turn ON **Help tooltip**
3. Choose **typed text** (short guidance) or **report page** (rich content)

**Pro tip:** Point a Help tooltip report page at an animated GIF background for a quick demo walkthrough.

## See Also

- [[Source-Tooltip-Options-Generally-Available]] — source article
- [[Sentence-Format-Template-Pattern]] — template syntax for sentence format
- [[Drillable-Hierarchy-Sentence-Tooltip-Pattern]] — ISINSCOPE + SWITCH for drill-aware sentences
