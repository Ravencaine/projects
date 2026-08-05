---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [visual-design, hierarchy, contrast, balance, dominance, scale, Gestalt]
related: [Gestalt-Principles, Color-Theory-for-Dashboards, Data-Narratives-Report-Design]
---

# Visual Design Principles for Dashboards

Seven core design principles that apply to all Power BI dashboards, derived from graphic design and visual communication theory.

## The 7 Principles

### 1 — Hierarchy

Arrange elements so the most important information is seen first.

- **Primary:** KPI card at top of page (largest, boldest).
- **Secondary:** Trend chart below the KPI.
- **Tertiary:** Supporting detail in tables or tooltips.
- Use **size**, **weight**, **color**, and **position** to establish hierarchy.

### 2 — Contrast

Use differences in color, size, and weight to separate important elements from less important ones.

- High contrast between KPI values and labels (large, bold vs. small, light).
- Strong color contrast between status indicators (green vs. red).
- Whitespace as a contrast tool — more space = more importance.

### 3 — Balance

Distribute visual weight evenly across the page.

- **Symmetrical balance:** KPI cards arranged in a grid (2×2, 3×3).
- **Asymmetrical balance:** One large visual balanced by several smaller ones.
- Power BI's snap-to-grid helps maintain alignment.
- Avoid clustering all heavy visuals in one corner.

### 4 — Dominance

One visual should command the most attention — the focal point.

- The dominant visual is usually the primary KPI card or the main trend chart.
- Everything else on the page supports or explains the dominant visual.
- If two visuals compete for dominance, add whitespace or reduce one to rebalance.

### 5 — Scale

Use size to communicate relative importance.

- The largest visual = most important.
- Consistent scale ratios create visual rhythm (e.g., 2×, 1.5×, 1× for primary/secondary/tertiary).
- Avoid many elements of equal size — the eye has nowhere to rest.

### 6 — Unity

Ensure all elements feel like part of one cohesive report.

- **Consistent color palette** across all pages.
- **Same font family** throughout (Segoe UI).
- **Uniform spacing** system (12px, 24px, 48px).
- **Theme JSON** enforces unity automatically.

### 7 — Gestalt Grouping

Use the five Gestalt principles (see [[Gestalt-Principles]]) to create visual groups.

- Proximity groups related elements.
- Similarity groups same-category visuals.
- Closure reduces visual clutter by implying completeness.

## The 3-30-300 Rule in Design Terms

| Tier | Design Priority |
|------|----------------|
| 3s | Hierarchy + Dominance — one focal point, instantly readable |
| 30s | Contrast + Scale — pattern visible without interaction |
| 300s | Unity + Balance — full report feels coherent |

## Related

- [[Gestalt-Principles]] — perceptual foundation for grouping
- [[Color-Theory-for-Dashboards]] — contrast and palette for unity
- [[Data-Narratives-Report-Design]] — report-building process that applies all 7 principles
