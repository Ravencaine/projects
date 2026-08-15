---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring Data Analysis with Power BI's Decomposition Tree.md"
note_type: atomic
tags: [power-bi, decomposition-tree, limits, 50-levels, 5000-data-points, atomic]
---

# Decomposition Tree 50 Levels 5000 Data Points Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-decomposition-tree-power-bi]]

Decomposition Tree has two hard limits: 50 hierarchical levels and 5,000 data points. Both are sufficient for most analyses but can be reached on very large or deeply nested datasets.

## Limits

| Limit | Value |
|-------|-------|
| Hierarchical levels | 50 |
| Data points | 5,000 |

## Practical implication

Deep product hierarchies or multi-level geographic structures can approach the 50-level limit. Very wide datasets (many dimensions) can hit the 5,000 data point ceiling. Plan the Explain By dimensions accordingly.

## Related

- [[decomposition-tree-setup-workflow]] — configuring dimensions
- [[decomposition-tree-filter-drillthrough-workflow]] — filtering to reduce data points
