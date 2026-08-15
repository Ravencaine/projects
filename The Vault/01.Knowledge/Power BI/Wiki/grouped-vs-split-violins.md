---
created: 2026-08-02
updated: 2026-08-05
source: What Violin Plots Tell You That Boxplots Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, violin-plot, grouped, split, comparison]
---

# Grouped vs Split Violins: Comparing Subgroups Within Categories

When data has subgroups within each main category, two structural choices:

**Grouped violins:** multiple narrow violins placed side by side within each main category (e.g., bike vs car delivery times within each city).

Use when: 2–4 subgroups per category; want to compare both within-category and between-category patterns.

**Split violins:** one violin per category, left half = subgroup A, right half = subgroup B.

Use when: exactly 2 subgroups; direct head-to-head comparison (before vs after, treatment vs control); saves horizontal space vs grouped.

Limit: More than 2 subgroups becomes confusing — use grouped violins instead or switch to a different chart type.

**Design choice:**
- Grouped = wider per category; good for dense layouts
- Split = same width as single violin; good for narrow layouts or when you want direct A/B
- Both require careful color coding so the two halves/readers instantly know which group is which
