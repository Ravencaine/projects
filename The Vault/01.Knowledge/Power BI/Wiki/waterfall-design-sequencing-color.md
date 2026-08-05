---
created: 2026-08-02
source: Why a Waterfall Chart is a Diagnostic Tool, Not Just a Dashboard Decoration
note_type: pattern
tags: [powerbi, pattern, data-visualization, waterfall-chart, design, color, sequencing]
---

# Waterfall Design: Sequencing Strategy, Materiality Rule, Orientation, Axis Truncation, Color by Meaning

**Sequencing strategy:**
- Chronological order for time-based stories
- Statutory order for financial statements
- Magnitude order only if the main argument is "biggest drivers first"
- The order shapes how the audience interprets cause and effect — choose deliberately

**Materiality rule:** If more than 7–10 steps, bundle the smallest into an "Other" category. Use a top-N or 80–90% threshold rule for what counts as "small."

**Orientation:** Long step labels → flip to horizontal waterfall. Gives labels room to breathe. Vertical default for short labels.

**Axis scaling trap:** If baseline is huge and changes are tiny, steps become invisible slivers. If you break/truncate the y-axis, signal it with a torn-axis marker — otherwise it misleads about scale.

**Color by meaning, not math:**
- Do NOT automatically use green=positive, red=negative
- Instead: use brand's "favorable" color for savings/wins (regardless of +/-), brand's "unfavorable" color for overspending/losses
- Example: spending less than budget is mathematically negative but favorable — color it as a win

**Multiple entities:** One waterfall = one story. For comparing 5+ regions/products, use a grid of small multiples.
