---
created: 2026-08-09
updated: 2026-08-09
source: "Exploring Data Analysis with Power BI's Decomposition Tree.md"
note_type: atomic
tags: [power-bi, decomposition-tree, analyze-field, measure, aggregate, atomic]
---

# Decomposition Tree Analyze Field Requires Aggregate Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-decomposition-tree-power-bi]]

The Decomposition Tree's Analyze Field accepts only an aggregate or explicit measure. A plain column dropped into Analyze Field will not render correctly — the field must produce a single scalar value per context.

## Requirement

Analyze Field = measure or explicit aggregate (SUM, COUNT, etc.)

## Why this matters

If the Analyze Field shows blank or unexpected results, the field may not be aggregated. Create a measure or ensure the field has a default aggregation set.

## Related

- [[decomposition-tree-setup-workflow]] — field configuration
- [[decomposition-tree-ai-splits-limitations]] — AI split environment restrictions
