---
created: 2026-08-05
updated: 2026-08-05
source: Power BI Dashboards Decision-Making (Boniface Muchendu)
note_type: atomic
tags: [power-bi, dashboard, executive, kpi, sparkline, design, branding]
---

# Executive One-Pager Dashboard Design

A dashboard designed for an executive audience distils complex data into 5–8 always-visible KPIs — prioritising clarity, context, and company branding over detail.

## Definition

An executive one-pager is a single Power BI dashboard tailored to a specific leadership role. It contains only the non-negotiable metrics that a decision-maker needs to monitor at a glance — no drill-throughs, no full reports.

## Key Principles

| Principle | Detail |
|-----------|--------|
| **5–8 KPIs max** | Too many KPIs dilute focus; fewer creates urgency and clarity |
| **Sparklines for trends** | Mini line charts (sparklines) show direction without visual noise |
| **Simple gauges for targets** | Single-value gauges communicate % to target at a glance |
| **Company branding** | Apply a custom JSON theme with brand colours and fonts |
| **Context, not numbers** | Each KPI tile should have a label that tells a story, not just a metric name |

## What to Avoid

- Shrinking a full report into a dashboard — this produces clutter, not clarity
- Mixing operational detail with strategic KPIs on the same dashboard
- Using complex charts that require explanation

## Design Workflow

1. Interview the executive: "What are the 3 decisions you make from this data each week?"
2. Identify 5–8 KPIs that directly answer those decisions
3. Choose visual types: sparkline (trend), gauge (target), card (single value)
4. Apply company branding theme
5. Publish as a dedicated dashboard, not a report page

## Related

- [[Dashboard-as-App-Landing-Page]]
- [[Power-BI-JSON-Theme]]
- [[KPI-Alert-Setup-Power-BI]]
