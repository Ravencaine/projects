---
created: 2026-08-02
updated: 2026-08-05
source: What Scatter Plots Tell You That Summary Statistics Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, scatter-plot, overplotting, alpha, hexbin, marginal, error-bar]
---

# Scatter Data Handling: Overplotting, Marginal Distributions, Error Bars for Estimates

Real-world data overlaps, clumps, and hides distributions. Three techniques to handle the mess honestly.

**Overplotting (points piled on each other):**

1. **Transparency first:** set alpha to 0.1, 0.05, or 0.02. Darker regions emerge = density revealed. Keep individual points visible.
2. **Hexbins / 2D histogram:** if transparency alone isn't enough, switch to binned density representation.
3. Don't jump straight to fancy density contours — low alpha usually does the job.

**Showing marginal distributions:**
A scatter plot hides what each variable looks like independently. Add marginal histograms or density curves along the axes — think of them as shadows cast onto the walls.

Marginals reveal: skew, truncation, ceiling effects, bimodality. Sometimes the central cloud looks like one population while the margins quietly show it was two all along.

**When dots represent estimates (means, predictions):**
A bare dot tells an incomplete story. Add error bars — always indicate whether they represent SD, SE, or CI. Without this, readers assume the wrong uncertainty measure.

**Design:** marginals belong on the same scale as the main axes — don't shrink them to the point where their distributions become unreadable.
