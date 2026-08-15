---
created: 2026-08-09
updated: 2026-08-09
source: "DAX Context Transition Explained in Power BI.md"
source_url: https://databear.com/dax-context-transition-power-bi/
note_type: source
tags: [dax, context-transition, calculate, keeplfilters, removefilters, iterator, boniface-muchendu]
---

# DAX Context Transition Explained in Power BI

Context transition converts row context into filter context. Triggered by CALCULATE, CALCULATETABLE, and measure references. Only matters when row context already exists.

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2026-03-14
> **URL:** https://databear.com/dax-context-transition-power-bi/
> **Routed to:** Power BI

## Summary

Context transition is the mechanism that bridges row context and filter context. Triggered when CALCULATE/CALCULATETABLE is invoked or a measure is referenced inside a row context. The article walks through: AVERAGEX + measure reference → context transition → single-row filter; the order of operations (context transition before filter modifiers); REMOVEFILTERS to undo context transition; and KEEPFILTERS to preserve existing multi-column filters during transition.

## Key Claims

- Context transition converts row context into filter context (row → filter)
- Triggers: CALCULATE, CALCULATETABLE, measure references, time intelligence functions
- Only matters when row context already exists; no row context = no transition
- Order: context transition first, then filter modifiers (REMOVEFILTERS, ALL, etc.)
- REMOVEFILTERS(Customer) inside CALCULATE removes the customer filter introduced by transition
- KEEPFILTERS wraps the iterator to preserve existing multi-column filters during transition
- The monthly average problem: DISTINCT(Date[Month]) inside AVERAGEX replaces the existing month filter instead of adding to it — use KEEPFILTERS(DISTINCT(...))
- Best practice: compute totals in a variable before the iterator

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Context Transition Explained in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~1,200 |
