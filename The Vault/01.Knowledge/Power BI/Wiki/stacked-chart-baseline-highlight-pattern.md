---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: pattern
tags: [power-bi, pattern, 100-stacked-chart, baseline-highlight, disconnected-table, position-measures, slicer]
---

# Stacked Chart Baseline Highlight Pattern

Complete implementation pattern for making a user-selected category segment always sit on the chart baseline in a 100% stacked bar or column chart, with all other segments stacked above it in grey.

## What It Does

- Reader picks a category via a slicer (e.g., "Large" pizza size)
- That category's segment drops to the **baseline** in the **highlight color**
- All other categories stack **above it** in **grey**
- Optional: bars re-sort by the highlighted segment's value, best-to-worst
- One slicer click re-highlights and re-bases every bar simultaneously

## Architecture

| Component | Type | Purpose |
|---|---|---|
| `Selector` | Disconnected DATATABLE | Powers the slicer — holds all category values |
| `Position 1` … `Position N` | Measures | One per stacking slot; Position 1 = selected category |
| Visual color formatting | Per-measure | Highlight color on Position 1, grey gradient on rest |
| (Optional) Sort by Position 1 | Visual formatting | Re-sort bars descending by highlighted value |
| (Optional) Tooltip Position table + Ord measures | Disconnected table + measures | Custom tooltip showing real category names |

## Requirements

- **2 or more segments** in the stacked chart
- **N distinct values** in the category column (method scales to any N)
- Disconnected `Selector` table — **no relationship** to the data model

## Wiring Steps

1. Create `Selector` DATATABLE via Modeling → New table
2. Create Position 1 through Position N measures
3. Build 100% Stacked Bar/Column chart
   - **Axis/Category**: the comparison dimension (e.g., pizza types)
   - **Values**: all N Position measures — NOT one measure + Category field in Legend
4. Add Slicer → `Selector[Category]` — single select
5. Format → Data colors: Position 1 = highlight color, Position 2…N = grey gradient
6. Format → Legend: **Off**

## Related

- [[stacked-chart-baseline-order-matters]] — `atomic`
- [[selector-datatable-disconnected-table]] — `function`
- [[position-measures-stacked-chart]] — `function`
- [[color-by-position-visual-formatting]] — `pattern`
- [[stacked-chart-custom-tooltip]] — `pattern`
- [[sort-column-pq-vs-dax]] — `pattern`
- [[circular-dependency-datatable-gotcha]] — `gotcha`
- [[stacked-highlight-test-checklist]] — `reference`
