---
created: 2026-08-04
note_type: pattern
tags: [power-bi, dax, design-best-practices, report-layout, dashboard]
---

# Power BI Design Best Practices

Report and dashboard layout principles that improve readability, performance, and user experience in Power BI.

## Visual Layout

### Grid and Alignment
- Use a **8px baseline grid** — Power BI snap-to-grid helps
- Keep visuals aligned; misalignment signals sloppy data
- Leave breathing room: minimum 4px between visual borders

### Visual Hierarchy
```
┌─────────────────────────────────────┐
│  Title (24–28pt, bold)             │
│  Subtitle / KPI callout (16–18pt)   │
├─────────────────────────────────────┤
│  Primary insight (large visual)     │
│                                     │
├───────────────┬─────────────────────┤
│  Supporting   │  Supporting         │
│  detail       │  detail             │
└───────────────┴─────────────────────┘
```

### Color Consistency
- **One accent color** — use sparingly for callouts and KPIs
- **Neutral backgrounds** for most visuals; let data provide the color
- **Max 5 colors** per visual, max 7 per report

## Performance Principles

### Reduce Visual Complexity
- Fewer visuals per page = faster rendering
- Remove unnecessary axes, gridlines, and legends
- Use **Tooltips** for detail instead of embedding it in the visual

### Model Hygiene
- Import only needed columns
- Use **聚合** (Aggregations) for large fact tables
- Avoid bidirectional cross-filtering unless necessary

## Navigation

### Report Bookmarks vs Pages
| Use | When |
|-----|------|
| Bookmarks | Switching visual states, drill-through, spotlight |
| Pages | Major section navigation, consistent cross-page context |

### Slicers
- Place slicers in a **dedicated filter pane** or top banner — not scattered
- Use **single-select slicers** where multi-select isn't needed
- Prefer **dropdown** over list/checkbox for >10 items

## Accessibility

- Ensure **color is not the only differentiator** — pair with labels or patterns
- Use **alt text** on every visual (Right-click → Edit alt text)
- Minimum **3:1 contrast ratio** for text and shapes

## Related

- [[dashboard-design-principles-framework]] — dashboard UX design
- [[accessibility-in-power-bi-visual-design]] — accessibility checklist
- [[power-bi-visual-performance]] — performance optimization
