---
created: 2026-08-02
updated: 2026-08-05
source: What Dumbbell Charts Tell You That Grouped Bars Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, aggregate-overlay, dumbbell, boxplot, micro-macro, summary]
---

# Aggregate Overlay: Micro (Individual) + Macro (Mean/Median) + Boxplot Spread on Dumbbells/Slopegraphs

When a chart has too many series to read individually, layering an aggregate summary lets readers switch between a micro view (per-category) and a macro view (overall trend) on the same canvas.

**Two reading modes on one chart:**

- **Micro** — faint individual lines/dots show each category's trajectory
- **Macro** — bold overlay line shows mean or median trend across all categories

**Adding a boxplot overlay** answers the question: "Is this improvement broad-based or driven by one outlier?"
- Boxplot on top of the dots shows the spread of values at each time point
- Tight box = consistent improvement across categories
- Wide box = improvement driven by a few categories

**Design pattern:**
- Individual series: thin, muted color
- Aggregate line: bold, distinct color
- Boxplot: overlaid on each time point's dot cluster
- Reference line at target if applicable

**Use when:** 8+ categories are making individual tracking impractical; stakeholders need both the category-level story and the aggregate signal.
