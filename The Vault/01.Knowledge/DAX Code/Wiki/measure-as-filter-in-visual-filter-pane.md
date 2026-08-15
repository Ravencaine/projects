---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
note_type: atomic
tags: [dax, measure, visual-filter-pane, filter-pane, granularity, atomic]
---

# Measure as Filter in Visual Filter Pane Atomic

**Type:** Atomic · **KB:** DAX Code · **Source:** [[source-filtering-measures-through-slicers]]

The Power BI visual filter pane allows placing a measure in the filter well — creating the illusion that measures can be filtered. The visual actually provides the granularity automatically; the filter is applied to the visual's grouping columns.

## How the visual filter pane works

When you drag a measure to the filter pane of a matrix visual:

1. Power BI evaluates the measure **per row group** (e.g., per Brand)
2. The filter condition (`Sales Amount > 100,000`) is checked per Brand
3. Brands failing the condition are excluded

The granularity is supplied by the visual — the matrix groups by Brand, and the measure is evaluated once per Brand.

## The key insight

```
Matrix groups by: Brand
Measure evaluated at: Brand granularity
Filter applied to: Brand rows where measure > threshold
```

The matrix **is** the granularity provider. Without the matrix's grouping, the measure has no context and cannot be filtered.

## Contrast with slicers

| Feature | Granularity source | Measure filter supported? |
|---------|-------------------|--------------------------|
| Visual filter pane | The visual itself | Yes (visual provides context) |
| Slicer | Slicer field selection | No (slicer cannot provide measure context) |

## Related

- [[measure-cannot-be-filtered-granularity-required]] — why slicers cannot filter measures
- [[slicer-filter-measure-implementation-workflow]] — correct implementation via calculation groups
