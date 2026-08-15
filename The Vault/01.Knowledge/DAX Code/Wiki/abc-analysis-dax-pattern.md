---
created: 2026-08-11
updated: 2026-08-11
source: "ABC-Analysis-HowToPowerBI-Transcript.md"
note_type: pattern
tags: [power-bi, abc-analysis, dax]
---

# ABC Classification — DAX Pattern

Classify items into A/B/C buckets based on cumulative % contribution using DAX measures.

## Purpose

A DAX-only alternative to the visual-calculations Pareto chart. Use when ABC classification needs to be filterable, cross-visual, or embedded in other measures.

## Pattern

```dax
-- Step 1: % of total
[% of Total] :=
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], REMOVEFILTERS('Product'))
)

-- Step 2: Running sum (requires visual-level ORDER BY context — use RUNNINGSUM in visual calc for this)
-- For DAX-only: use a disconnected table + RANKX approach or handle in Power Query
```

## When to Use DAX vs Visual Calculations

| Scenario | Approach |
|----------|----------|
| ABC on a single visual (Pareto chart) | Visual Calculations |
| ABC as a filter/slicer value | DAX measure or calculated column |
| ABC needed in multiple visuals | DAX measure |
| ABC driving conditional formatting | DAX measure |

## Related

- [[abc-classification-visual-calculations]] — visual-calculations approach (recommended for charts)
