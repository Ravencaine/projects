---
created: 2026-08-02
updated: 2026-08-05
source: What Scatter Plots Tell You That Summary Statistics Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, scatter-plot, log-scale, aspect-ratio, validation]
---

# Scatter Plot Foundations: Log Scale, Aspect Ratio, Coordinate Validation

Before interpreting any scatter plot, validate the frame itself — most misleading scatter plots fail at the foundation, not in the statistics.

**1. Validate coordinates first.**
Every point needs a valid X and Y value. Nulls treated as zeros, mixed units, duplicate rows, and truncated values corrupt the relationship silently. Check data integrity before drawing any conclusions.

**2. Choose scale deliberately — linear vs log.**
The choice is analytical, not cosmetic:
- **Linear scale:** absolute differences are meaningful (x + 10)
- **Log-log scale:** if a log-log transformation straightens a curve, you may have found a **power-law relationship:** a fundamental discovery about the data's nature
- **Log-x or log-y:** single-axis log when one variable spans orders of magnitude
- Ask: "Am I interested in absolute or relative differences?" The scale answers that implicitly.

**3. Set aspect ratio honestly.**
Library defaults produce a square chart regardless of the data. But a shallow trend benefits from a wider plot (signal separates from noise); a steep trend benefits from a taller plot (prevents slope exaggeration). Don't let defaults dictate how steep the world appears.

**Rule of thumb:** the trend line should be approximately 45° relative to the data's natural orientation.
