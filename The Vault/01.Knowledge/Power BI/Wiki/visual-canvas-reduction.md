---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, performance, optimization, beginner, visual-design]
---

# Reducing Visuals and Slicers Per Page

After fixing the model and measures, visual count starts to matter — because most visuals issue one or more DAX queries on render.

## Why Visual Count Matters

Every visual queries the model. Open a page with 19 visuals → 19 queries fire simultaneously. Cut to 11 → 11 queries.

On a well-tuned model, this is a smaller effect. On an unoptimized model, it's compounding the existing slowness.

## What to Cut

- **Near-identical KPI cards** → merge into a multi-row card
- **"Nice to have" charts** → move to a drill-through page that loads on click
- **Unused slicers** → delete them (check with stakeholders first)
- **Decorative visuals** → if it doesn't answer a question, it adds latency

## Results

- Visuals on main page: 19 → 11
- One merged KPI card replaced three individual cards
- Two charts moved to drill-through
- One slicer deleted (nobody used it)

## Slicer-Specific Tips

Every slicer has two costs:
1. Queries the model to populate its own list of values
2. Re-triggers queries on all visuals it filters

**High-cardinality slicers** (8,000 customer names) are expensive. Fixes:
- Use **Top N** filters instead of showing all values
- Replace open dropdowns with banded ranges (e.g., "Top 10", "$100K+", etc.)

**Edit Interactions:** use Format → Edit Interactions to disable cross-filtering between visuals that don't need to talk to each other. Every blocked interaction = one fewer query.

## The Balance

Over-aggregating to hit performance goals can break the report's usefulness. Fast and useless is still useless. The goal is speed that serves the reader, not speed at the cost of function.

## Related

- [[performance-analyzer-workflow]] — measure which visuals are actually slow before cutting
- [[dax-measure-optimization-patterns]] — fix the query before cutting the visual
