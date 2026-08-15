---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into tooltip options in Power BI visuals (Generally Available).md"
note_type: atomic
tags: [power-bi, tooltip, report-page-tooltip, non-interactive, limitation, drillthrough]
---

# Report Page Tooltip — Non-Interactive Limitation

> **Type:** atomic
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-06

## The Limitation

Report page tooltips are **display-only**. Consumers can hover and read, but they **cannot**:
- Select or adjust slicers inside the tooltip page
- Click on other visuals in the tooltip page
- Interact with any element on the tooltip page

## Why It Matters

Authors sometimes assume the tooltip page works like a mini report. It doesn't. The moment a consumer hovers over a data point, the tooltip page renders as a static card — no interactivity.

## The Alternative: Drillthrough Pages

When consumers need to interact with the filtered view:

1. Build a **Drillthrough page** in the same report (or a different report in the same workspace)
2. Set the drillthrough source fields to match the tooltip's source visual
3. Let consumers **right-click** a data point to open the drillthrough page
4. The drillthrough page is fully interactive — slicers, visuals, and filters all work

**Report page tooltip** = rich display, no interaction
**Drillthrough page** = right-click access, fully interactive

## See Also

- [[Source-Tooltip-Options-Generally-Available]] — source article
- [[Tooltip-Type-Selection-Workflow]] — when to choose report page tooltip
