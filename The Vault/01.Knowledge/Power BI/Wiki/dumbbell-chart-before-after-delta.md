---
created: 2026-08-02
source: What Dumbbell Charts Tell You That Grouped Bars Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, dumbbell-chart, dot-plot, before-after, delta]
---

# Dumbbell Chart: Dot + Connector for Before/After Magnitude of Change

Dumbbell chart = dot plot + connector line. Shows magnitude of change between two conditions (before/after, pre/post, budget/actual) — the line length IS the story, no mental arithmetic needed.

**Anatomy:**
- Left dot = before value; right dot = after value
- Connector line length = magnitude of change
- Direction: dot shifted right = improvement; dot shifted left = decline

**Reading rules:**
- Long line = big change
- Short line = little movement
- Right dot further along = improvement
- Label the connector directly with the delta (+17, -10) — do not make readers squint at the axis

**Design rules:**
- **Sort by "after" value**, not alphabetically — alphabetical sorting produces random scatter; ranked sorting surfaces the headlines ("Tools & systems skyrocketed +17, Career growth tanked -10")
- Add a **reference line** (e.g., target = 60%) if context helps
- Best for 8+ categories where grouped bars become overwhelming

**When to use dumbbell:**
- Before vs after comparison (exactly two time points)
- Question sounds like: "Where did we improve most?" / "Did the training move the needle?"
- Magnitude of change is the real story — not the raw values themselves

**When NOT to use:**
- More than two time points → line chart instead
- Absolute values matter more than change → grouped bar chart
- Fewer than 5 categories → grouped bars are readable enough

See `bump-chart-vs-line-vs-slope.md` for the related slopegraph pattern (rank changes, not magnitude).
