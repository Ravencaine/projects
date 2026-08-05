---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Dashboard Design Principles Used by Top Companies.md
note_type: pattern
tags: [power-bi, pattern, progressive-disclosure, drill-through, page-hierarchy, overview]
---

# Progressive Disclosure Pattern

A layered page architecture for Power BI dashboards that presents summary KPIs first and surfaces detail on demand. Most viewers only ever need the top layer — burying that summary under filters and detail visuals forces everyone to do the analyst's job just to read a headline number.

## Three-Layer Architecture

### Layer 1: Overview Page
The handful of KPIs that matter most, at a glance. No scrolling required.

- Top 3–5 headline metrics as KPI cards
- One trend chart showing the primary metric over time
- Status indicators (red/green/amber)

### Layer 2: Category Pages
Breakdowns by a single dimension: region, product, customer segment.

- Each category gets its own page
- Consistent layout across category pages so users build spatial memory
- Same KPI cards as the overview, filtered to that category

### Layer 3: Detail Pages
Drill-through views for someone who wants to investigate a specific anomaly.

- Transaction-level detail
- Raw data tables
- Anomaly annotations

## Navigation Hierarchy

```
Executive Overview
    └── Regional Risk & Portfolio Dynamics
            └── Credit Risk Intelligence (drill-through by branch, loan type)
```

Drill-through pages are accessed by right-clicking a visual element and selecting **Drill through:** they are not on the main navigation path.

## Key Design Rules

| Rule | Reason |
|---|---|
| Overview page loads first | Sets context before exploring |
| KPI cards on every page | No page should require navigation to find the headline number |
| Consistent card placement | Users learn where to look |
| Category pages use the same color system | "Red" means the same thing everywhere |
| Detail pages are optional navigation | Only analysts investigating anomalies need these |

## Related

- [[dashboard-design-principles-framework]] — `pattern`
- [[slicer-discipline-filter-intent]] — `pattern`
- [[kpi-validation-programmatic-check]] — `pattern`
