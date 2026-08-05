---
created: 2026-08-02
source: What Dumbbell Charts Tell You That Grouped Bars Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, diverging-bar, delta, change, winners-losers]
---

# Diverging Delta Chart: (After − Before) Centered at Zero for Winners vs Losers

Compute the delta (after minus before) and plot as a diverging bar chart centered on zero. Used when the starting baseline is irrelevant and the question is purely "who improved and who declined?"

**Pattern:**
1. Calculate `Delta = After − Before` for each category
2. Plot bars centered on zero: positive bars (right) = improvement, negative bars (left) = decline
3. Sort by delta descending — biggest movers jump out first
4. Color: green = positive, red = negative

**Design rules:**
- Always center on zero — the baseline is the starting point, not a reference to beat
- Sort by delta size so the priority list is visible at a glance
- Can also be rendered as a dumbbell or lollipop variant — same encoding rule applies

**When to use:**
- Question: "What should we prioritize next quarter?"
- Starting values are contextually irrelevant
- Non-technical audience needs the headline

**When NOT to use:**
- Audience needs context about where things started ("was that category already good or terrible?") — diverging delta hides the baseline; use a dumbbell instead to show both levels
- Absolute values matter — diverging delta encodes only change, not magnitude of the values themselves

**Prompt template:** *"Calculate the delta (after minus before). Plot a vertical diverging bar chart centered at 0. Sort by delta descending. Colour positive green and negative red."*
