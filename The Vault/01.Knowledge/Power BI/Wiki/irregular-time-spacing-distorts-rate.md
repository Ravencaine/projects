---
created: 2026-08-02
source: When a Line Chart Misleads (And What to Use Instead)
note_type: gotcha
tags: [powerbi, gotcha, data-visualization, line-chart, time-axis, irregular-intervals, datetime]
---

# Irregular Time Spacing: Equal X Spacing Distorts Rate of Change

In a line chart, slope implies rate of change. If a 2-hour gap and a 3-month gap occupy equal horizontal space, the visual rate of change is entirely distorted.

**The problem:** Sequential ordering alone does not justify equal spacing. When points are spaced by visual position rather than elapsed time, short-term volatility gets flattened and long gaps get misrepresented.

**When to skip the line:**
- Events happen at highly irregular or unpredictable intervals
- Time gaps between measurements vary substantially

**Fix: Use a true datetime axis.** Physical distance between points must accurately reflect chronological time elapsed. The slope then represents the actual rate of change.

**Alternative:** Drop the connecting line entirely and use a scatter plot. Let the density of points tell the story — frequent observations cluster visually, sparse observations spread apart, preserving the true temporal structure.

**Rule of thumb:** If the time between points varies by more than 2x, question whether a line is honest. Scatter or broken line for irregular series.
