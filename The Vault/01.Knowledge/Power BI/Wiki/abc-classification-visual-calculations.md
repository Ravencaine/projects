---
created: 2026-08-11
updated: 2026-08-11
source: "ABC-Analysis-HowToPowerBI-Transcript.md"
note_type: pattern
tags: [power-bi, abc-analysis, visual-calculations, pareto]
---

# ABC Classification — Visual Calculations Pareto Chart

Visual calculations build an ABC/Pareto chart: % of total per item → running sum → three shaded buckets (A/B/C) with labeled boundaries.

## Purpose

Classify items into A (top ~40%), B (40-80%), C (rest) by cumulative revenue contribution. Overlay a Pareto line on a column chart with shaded A/B/C regions.

## Components

- **COLLAPSEDEALL:** sum of measure across all rows (ignores current filter context) — for % of total
- **RUNNINGSUM:** cumulative sum in rows order — for the Pareto line
- **ORDER BY:** sort rows by running sum descending
- **NEXT:** return the next row's value — for finding bucket boundary labels
- **Conditional logic:** `IF(running_sum <= 0.4, 0.4, BLANK())` for bucket shading

## Structure

```
Column Y-axis:
  [Total Sales]                   — bar (hidden, used in tooltips / RUNNINGSUM)
  [% of Total]  = DIVIDE(TotalSales, COLLAPSEDEALL(TotalSales))
  [Running Sum] = RUNNINGSUM([% of Total]) ORDER BY [Running Sum] DESC
  [Group A]     = IF([Running Sum] <= 0.4, 0.4, BLANK())
  [Group B]     = IF([Running Sum] > 0.4 && [Running Sum] <= 0.8, 0.8, BLANK())
  [Group C]     = 1

Line Y-axis:
  [Running Sum] = RUNNINGSUM([% of Total]) ORDER BY [Running Sum] DESC
```

## Formatting Tricks

- **Overlap series = 100%, category spacing = 0%** → merges bars into shaded regions
- **Flip overlap** to correct ordering of A/B/C regions
- **Hide** Total Sales from visual but keep on tooltips → enables sorting by sales without showing duplicate bars
- **Hide** Group A/B/C lines (show as bars only via formatting)
- **Labels:** use NEXT to find the last item in each bucket, then show a label on that single dot only

## Key Rules

- Do NOT hardcode product fields — use `ROWS` to keep the visual flexible across dimensions
- For visual calculations: a measure must be added to the visual before another visual calculation can reference it (even if hidden)
- Hide from visual ≠ delete: hidden measures are still used by RUNNINGSUM, NEXT, etc.

## Related

- [[visual-calculations-usage-guide]] — when to use visual calculations vs measures
- [[abc-analysis-dax-pattern]] — DAX-only ABC pattern (no visual calculations)
