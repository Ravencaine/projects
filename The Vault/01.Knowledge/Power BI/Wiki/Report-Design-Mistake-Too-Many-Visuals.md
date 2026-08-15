---
created: 2026-08-13
source: 5 Mistakes to Avoid in Power BI (That Can Ruin Your Reports)
note_type: pattern
tags: [power-bi, report-design, visual-design, performance, user-experience, beginner]
---

# Report Design Mistake: Too Many Visuals Per Page

<!-- Packing a page with visuals feels productive but creates cognitive overload and slows performance. Five to seven focused visuals beat twenty cluttered ones. -->

## The Mistake

Adding as many visuals as possible to a single report page — charts, KPIs, tables, slicers — thinking "more is more."

```
❌ 15–20 visuals on one page
   → User cannot find what matters
   → Cognitive overload
   → Slower render
   → Conflicting visual hierarchy
```

## Why It Happens

- Dashboard creator optimises for information density, not comprehension
- No governance on report design standards
- Stakeholder pressure to "show everything in one view"

## The Fix Pattern

### Target: 5–7 Visuals Per Page

```
Rule: One question per visual, one page per business topic
```

| Visual Count | Use Case |
|-------------|----------|
| 1–3 | Executive summary / KPI headline |
| 4–7 | Analytical deep-dive page |
| 8+ | Break into multiple pages by theme |

### Focus on Clarity, Storytelling, Key KPIs

```
1. Define the ONE question this page answers
2. Pick the visual type best suited to that question:
   - Trend over time     → line / area chart
   - Part-to-whole       → pie / donut (sparingly)
   - Comparison          → bar / column
   - KPI vs target       → KPI card / gauge
   - Distribution        → histogram / scatter
   - Geography           → map
3. Remove visuals that don't directly serve the page question
```

### Page Naming Convention

Name pages by business question, not by visual type:

```
❌ Page: "Line Chart + Bar Chart + Table"
✓ Page: "Revenue Trend by Region"
✓ Page: "Customer Churn Overview"
✓ Page: "Inventory Status Daily"
```

## Related

- [[Data-Modeling-Mistake-calculated-Columns-vs-Measures]] — Power BI: too many calculated columns is a modelling mistake
- [[Data-Modeling-Mistake-Broken-Relationships]] — Power BI: model structure mistakes that cause wrong results
- [[Data-Modeling-Mistake-Bi-Directional-Filtering]] — Power BI: relationship mistakes causing unexpected results
