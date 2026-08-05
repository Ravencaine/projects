---
created: 2026-08-02
source: Next-Level Dashboard Design With Power BI's New Card Visual With Reference Labels
note_type: atomic
tags: [powerbi, card-visual, reference-labels, kpi, feature]
---

# New Card Visual Anatomy (Power BI November 2023+)

The new card visual (released November 2023) layers three content zones top-to-bottom:

```
[Image] Callout Value    ← primary KPI number (font, size, unit display)
         Label            ← category/title string (font, color, size)
─────────── divider ─────
         Reference Label   ← secondary indicator (title + optional Detail sub-value)
         Detail            ← optional interpretive sub-value (variances, deltas)
```

**Callout Values** — primary KPI values dropped into the `Data` field well; each becomes a card in the layout grid.

**Reference Labels** — sub-indicators added per series under the `Reference labels` tab; each has a title (editable to custom text via `Content → Custom`) and an optional `Detail` field for additional DAX measures.

**Key constraint:** Detail sub-values cannot be dynamically colored via `fx` — workaround is conditional formatting on the detail's own measure, applied before it is referenced in the card.

> Extends `new-chart-data-label-anatomy.md` — both share the "Detail sub-value" concept with the same fx limitation.
