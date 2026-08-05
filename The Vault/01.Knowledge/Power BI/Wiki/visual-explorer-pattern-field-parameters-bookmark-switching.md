---
created: 2026-08-02
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data
note_type: pattern
tags: [power-bi, field-parameters, bookmarks, visual-explorer, user-empowerment, ux]
---

# Visual Explorer Pattern — Field Parameters + Bookmark Switching

A self-service "plug-in section" added to any Power BI report that lets users pick their own metric, dimension, and chart type — eliminating ad-hoc report requests.

## Architecture

```
User selection:
  Metric slicer  →  Field parameter (NAMEOF to measure)
  Dimension slicer → Field parameter (NAMEOF to column)
  Visual type  →  Bookmark navigator (switches stacked charts)

Stacked visuals (all bound to same parameter):
  Bar chart    ← overlaps → Column chart ← overlaps → Line chart ← etc.
  All bound to Metric + Dimension field parameters
```

## Key Design Decisions

- **Stacked overlap:** all chart types occupy the same canvas position
- **Bookmark without data:** `Data: unchecked` so parameter slicers persist across bookmark switches
- **Copy "View Selection" group:** PBIX template includes the navigation UI — paste and connect bookmarks

## Components

1. [[field-parameters-for-metric-dimension-selection]] — two field parameters
2. [[bookmark-navigator-for-visual-type-switching]] — bookmark per visual type
3. [[dynamic-chart-title-from-metric-dimension-selections]] — `Chart Title` measure
4. [[bar-color-by-metric-type-variation-vs-absolute]] — color by metric variant

## Why It Works

- Users self-serve → fewer ad hoc requests
- One section replaces dozens of near-identical pages
- Metric + dimension + chart type = infinite combinations from a fixed set of visuals

## Related

- [[Field-Parameters]] — field parameter reference
- [[dynamic-text-titles-in-power-bi]] — dynamic title pattern
