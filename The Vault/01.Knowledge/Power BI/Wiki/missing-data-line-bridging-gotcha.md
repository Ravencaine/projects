---
created: 2026-08-02
updated: 2026-08-05
source: When a Line Chart Misleads (And What to Use Instead)
note_type: gotcha
tags: [powerbi, gotcha, data-visualization, line-chart, missing-data, gap, interpolation]
---

# Missing Data Bridging: Tool Auto-Connects Gaps → Silent Interpolation as "Stability"

Many analytics tools bridge missing periods by default with a straight diagonal segment from the last known point to the next.

**How to spot it:** A perfectly straight diagonal line cutting across a highly variable chart, or a massive immediate drop to baseline.

**The problem:** Missing data is not "no change" and not "zero." It is a complete lack of information. Bridging it with a solid line silently interpolates and turns missing data into an unjustified statement of stability — viewers are unaware anything was missing.

**Fixes:**
1. **Break the line** — show a visible gap where data is absent. The chart should reflect what was actually observed.
2. **Dotted segment** — if you must connect for visual context, use a clearly different encoding (dotted/dashed) and label it explicitly: "data unavailable."
3. Never let tools silently bridge gaps — always check what happens in periods where the pipeline failed.

**Design:** The empty space itself is information. A gap communicates "we don't know" honestly; a bridge communicates "we assume nothing changed."
