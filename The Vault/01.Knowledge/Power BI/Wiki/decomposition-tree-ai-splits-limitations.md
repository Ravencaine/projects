---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring Data Analysis with Power BI's Decomposition Tree.md"
note_type: atomic
tags: [power-bi, decomposition-tree, ai-splits, limitation, on-prem, azure, atomic]
---

# Decomposition Tree AI Splits Limitations Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-decomposition-tree-power-bi]]

AI splits (High Value / Low Value) in the Decomposition Tree are NOT supported in four deployment scenarios. Manual drill-down (clicking + to add a dimension) works in all environments — AI splits are a cloud-only feature.

## Unsupported environments

| Environment | AI Splits supported? |
|-------------|---------------------|
| On-premises Analysis Services | No |
| Azure Analysis Services | No |
| Power BI Report Server | No |
| Publish to the Web | No |

## What works everywhere

Manual dimension selection (+ button → pick dimension) works in all environments. This is the fallback when AI splits are unavailable.

## Related

- [[decomposition-tree-setup-workflow]] — manual + AI setup
- [[decomposition-tree-filter-drillthrough-workflow]] — filters and drill-through work in all environments
