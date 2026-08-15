---
created: 2026-07-29
updated: 2026-08-02
source: "Power BI UX: 7 Key Features"
note_type: atomic
tags: [ux, power-bi-features, drillthrough, bookmarks, multilingual, feedback]
related: [Data-Narratives-Report-Design, The-3-30-300-Rule]
source_url:
---

# Power BI UX: 7 Key Features

Seven Power BI features that significantly improve the user experience of a dashboard — from navigation to accessibility.

## The 7 Features

### 1 — Custom Tooltips

Purpose: provide contextual detail on demand without leaving the current view.

- Create a dedicated tooltip page (Power BI page size: Tooltip).
- Design it with small multiples, supporting KPIs, or trend sparklines.
- Assign to a visual via **Format → Tooltips → Report page**.

### 2 — Bookmarks and Buttons

Purpose: navigate between report pages or apply filter states without requiring the filter pane.

- Create bookmarks for each key view.
- Add buttons that trigger bookmarks.
- Use to build guided report tours or mode switches (e.g., detailed view ↔ summary view).

### 3 — Drillthrough Pages

Purpose: allow users to jump from a summary visual to a detailed page filtered to the selected item.

- Create a dedicated drillthrough page.
- Add the field to the **Drillthrough** well of the source visual.
- Power BI automatically filters the target page to the selected context.

### 3b — Interactive Features as a Holistic Pattern

Drillthrough, filters, and slicers form a unified interactive exploration pattern:

- **Drill-down:** navigate within a visual's hierarchy (e.g., Year → Quarter → Month)
- **Filters:** narrow the dataset by specific criteria (field-level, visual-level, page-level, report-level)
- **Slicers:** always-visible filter controls that update the report in real time

Van Zyl frames these as a *single concept*: **empowering users to unearth tailored insights**. The technical implementation (drill-down, filter pane, slicer visual) is secondary to the UX goal — self-service data exploration without analyst intervention.

> Source: [[Source-Crafting-Compelling-Impactful-Power-BI-Reports]] — Althea Van Zyl, 2024-07-09

### 4 — Q&A Visual

Purpose: let users ask natural-language questions about the data.

- Add the **Q&A** visual to a page.
- Pin frequently asked questions as suggested questions.
- Review Q&A language suggestions to improve the semantic model.

### 5 — Field Parameters

Purpose: let users switch between metrics or dimensions on a single visual.

- Go to **Modeling → New parameter → Fields**.
- Add to a visual's axis or legend — Power BI handles the switching.
- See: [[Field-Parameters]].

### 6 — Scorecard Visual (Goal)

Purpose: track KPIs against targets over time with built-in status indicators.

- Use the **Scorecard** visual (in preview/GA depending on version).
- Set target values, thresholds, and status display.
- Works with pbix files and DirectQuery.

### 7 — Multi-Language Reports

Purpose: make reports accessible in multiple languages for global audiences.

- Use Power BI's **Modeling → Languages** to set report language.
- Create a translation table (key → English, key → French, etc.).
- Use DAX `FORMAT` with locale strings for number/date formatting.

## Notes

- These 7 features are the ones Bittar highlights as underused in most client dashboards.
- The combination of drillthrough + bookmarks + tooltips directly supports the [[The-3-30-300-Rule]] — tooltip supports 3-second context, drillthrough supports 300-second analysis.
- Bittar's "Unlocking Potential: 7 Features to Elevate User Experience" article covers each in detail.

## Related

- [[Data-Narratives-Report-Design]] — design process that integrates these features
- [[Field-Parameters]] — implementation detail for feature #5
- [[The-3-30-300-Rule]] — user experience framework these features serve
