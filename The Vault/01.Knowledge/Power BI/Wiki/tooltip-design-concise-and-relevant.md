---
created: 2026-08-01
updated: 2026-08-02
source: "From Messy to Masterpiece The Ultimate Power BI Dashboard Checklist .md"
note_type: atomic
tags: [dashboard-design, tooltips, user-guidance, power-bi]
---

# Tooltip Design — Concise and Relevant

Tooltips must provide only the most pertinent information — enough to clarify the visual, not to replace it.

## Principle

A tooltip is an on-demand detail layer. It should supplement the visual, not replicate the label. Over-stuffed tooltips defeat their purpose: the user should not need to hover to understand the chart, only to get the specific value or cross-detail they cannot fit on the axis or label. This principle extends [[enhancing-data-narratives-power-bi-tooltips]], which covers the implementation mechanics.

## Design Rules

- **Concise**: limit to 3–5 data points per tooltip — not the entire dataset
- **Relevant**: show what cannot be inferred from the visual alone (exact values, % of total, period-over-period change)
- **Contextual**: use the primary visual's fields to inform tooltip content — dynamic, not static
- **Readable**: do not overcrowd the tooltip card — a single clear metric beats a dense table
- **Do not use tooltips as the primary data communication channel**: labels should always be sufficient without hovering

## Related

- [[enhancing-data-narratives-power-bi-tooltips]] — source note with full Power BI tooltip implementation (Mark Chen)
- [[unlock-power-multiple-tooltips-power-bi]] — multiple tooltip pages per visual
- [[label-formatting-units-truncation-tooltips]] — labels carry units; tooltips carry the detail
