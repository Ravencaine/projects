---
created: 2026-08-02
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data
source_url: https://medium.com/microsoft-power-bi/build-a-visual-explorer-in-power-bi-let-users-choose-what-and-how-they-see-data-d19d35c765e8
author: Isabelle Bittar
published: 2025-11-01
note_type: source
tags: [power-bi, field-parameters, bookmarks, visual-explorer, dynamic-title, ux]
---

# Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data

**Author:** [[Author-Isabelle-Bittar]]
**Published:** 2025-11-01
**URL:** https://medium.com/microsoft-power-bi/build-a-visual-explorer-in-power-bi-let-users-choose-what-and-how-they-see-data-d19d35c765e8
**Level:** Any | **Category:** Data Visualization

## Core Components

- Field parameters for metric + dimension selection
- Stacked chart types switched via bookmarks (Data: unchecked)
- Bookmark navigator as the visual type selector
- Dynamic `Chart Title` from `ALLSELECTED` on both parameters
- `Bar Color` measure gated by metric Order from the field parameter

## Notes Extracted

1. [[visual-explorer-pattern-field-parameters-bookmark-switching]] — the full pattern
2. [[field-parameters-for-metric-dimension-selection]] — parameter definitions
3. [[bookmark-navigator-for-visual-type-switching]] — bookmark setup
4. [[dynamic-chart-title-from-metric-dimension-selections]] — title measure
5. [[bar-color-by-metric-type-variation-vs-absolute]] — color by metric variant
