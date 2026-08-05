---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: reference
tags: [power-bi, reference, 100-stacked-chart, test, checklist, position-measures, baseline-highlight]
---

# Stacked Baseline Highlight — Test Checklist

Verification steps to confirm the baseline highlight pattern is wired correctly. Run through each item for every possible slicer selection.

## Core Functionality Tests

### Position 1 — Selected Category
Pick each category in the slicer and confirm: **Position 1 always equals the selected category's value.**

### Position 2 … N — Remaining Categories
Confirm: **the other categories appear in their original relative order** (e.g., if the original order is S/M/L/XL/XXL and "L" is selected, Position 2 = M, Position 3 = XL, Position 4 = XXL, Position 5 = S).

### Sum of All Positions
Confirm: **sum of all positions equals the un-split total:** should be identical to the value before the feature was added.

### Nothing Selected
Confirm: **all positions are blank** (or your chosen default if you set a `SELECTEDVALUE` fallback).

### Legend
Confirm: **legend is off:** position-based series show meaningless labels if left visible.

### Custom Tooltip (if built)
Confirm: **`Ord Category` at position 1 matches the slicer selection** exactly.

## Visual Checks

- Highlight color is on Position 1 only
- Grey gradient is applied to Position 2 through N
- Bars re-sort correctly when switching selections (if sort-by-Position-1 is enabled)
- Tooltip page shows real category names, not "Position 1/2/3…"

## Related

- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
- [[color-by-position-visual-formatting]] — `pattern`
- [[stacked-chart-custom-tooltip]] — `pattern`
