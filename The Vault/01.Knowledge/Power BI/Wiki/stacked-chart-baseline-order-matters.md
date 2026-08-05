---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: atomic
tags: [power-bi, atomic, 100-stacked-chart, baseline, segment, data-visualization]
---

# 100% Stacked Chart — Why Segment Order Matters

In a 100% stacked bar or column chart, only the segment sitting directly on the baseline is genuinely easy to compare across bars. Every segment stacked above it "floats" — its apparent length is distorted by the segments below it, making cross-bar comparison unreliable once there are more than two or three bars.

## The Baseline Advantage

A segment touching the baseline has no stacked segments beneath it. Its length is its true proportional value, readable at a glance across all bars simultaneously.

## The Standard Limitation

A 100% stacked chart bound the ordinary way — one measure plus a category field in Series/Legend — draws its segments in whatever order Power BI sorts that category field. DAX can control values but cannot reach into the chart engine to reorder segments.

## The Solution

Trade "one measure split by a field" for **N separate measures, one per stacking position**. The selected category always becomes Position 1 (baseline), regardless of its original field sort order. Since Position 1 is always plotted first, it always sits on the baseline — no matter which category that is.

## Related

- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
- [[position-measures-stacked-chart]] — `function`
- [[color-by-position-visual-formatting]] — `pattern`
