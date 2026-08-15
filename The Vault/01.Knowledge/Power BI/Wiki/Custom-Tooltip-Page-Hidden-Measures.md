---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
note_type: atomic
tags: [power-bi, tooltip, custom-tooltip, page, hidden-measures, measure-visibility, report-page, interaction]
---

# Custom Tooltip Page for Hidden Measures

Create a separate report page and use it as a custom tooltip to control exactly which values appear when hovering over a chart. This hides internal helper measures (like Max Graph Area and Min Graph Area) that should not appear in the default tooltip.

## How to Create

1. **Create a new page** → name it e.g. "Tooltip"
2. Add visuals to the page showing only the intended tooltip content (e.g. date, vital name, value)
3. **Format** the page: Page information → **Tooltip: On**
4. Optionally: set the page size to a compact canvas (Page size → Type → Tooltip)
5. Return to the main page → select the chart → **Format** → **Tooltips** → **Type: Report page**
6. Select the tooltip page from the dropdown

## Why Use a Custom Tooltip

| Default Tooltip | Custom Tooltip Page |
|----------------|---------------------|
| Shows all fields/measures in the visual | Shows only what you configure |
| Exposes internal helper measures | Hides Max/Min Graph Area and other scaffolding |
| Limited formatting options | Full formatting control on the tooltip page |
| Same tooltip for all visuals | Different tooltip pages for different visuals |

## Key Use Case

When a chart uses helper measures for formatting (e.g. Max Graph Area, Min Graph Area) — these appear in the default tooltip and confuse users. A custom tooltip page lets you show only the meaningful values: Date, Vital Type, and the actual measurement.

## Related

- [[Source-Oblique-Area-Chart-Native-Visuals-Isabelle-Bittar]] — source
- [[Dynamic-Graph-Area-Buffer]] — the Max/Min Graph Area measures that a custom tooltip hides
- [[Oblique-Area-Chart-Native-Visuals-End-to-End]] — end-to-end; this is the final formatting step
