---
created: 2026-08-02
source: When a Line Chart Misleads (And What to Use Instead)
note_type: pattern
tags: [powerbi, pattern, data-visualization, line-chart, log-scale, exponential-growth, compounding]
---

# Compounding Growth on Linear Scale: Use Log Scale to Reveal Early Volatility

Plotting exponential or compounding growth on a standard linear axis flattens early variation and creates a deceptive "hockey stick."

**What happens:** The left side of a linear growth chart becomes visually flat, teaching the viewer that nothing interesting happened until the very end. Early volatility — the periods of highest relative change — is invisible.

**When to use log scale:**
- Compounding, exponential growth over long horizons
- When percentage change matters more than absolute change
- When you want to reveal early volatility that linear scale hides

**How it works:** On a log scale, equal vertical distances represent equal percentage changes. A 10→20 move and a 1000→2000 move look the same — both are +100%. This makes early-stage growth visible alongside mature-stage growth on the same chart.

**Design note:** Label the axis clearly ("log scale") so readers understand why the visual looks different from a linear chart. Consider annotating the actual values at key points.

**Alternative for multi-series comparison:** Index both series to a baseline (set to 100 at baseline date). Compute `Index = 100 × (value ÷ baseline)`. A single axis then compares true relative change across series accurately.
