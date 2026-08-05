---
created: 2026-08-02
updated: 2026-08-05
source: Why Simple Bar Charts Are Harder Than They Look
note_type: pattern
tags: [powerbi, pattern, data-visualization, bar-chart, baseline, axis, zero]
---

# Bar Chart Foundations: Zero Baseline — Non-Zero Axis = Visual Distortion

Bar charts encode value through length. The single most important rule: **always start the axis at zero.**

**Why zero matters:** If you start the axis at 4.5 to show the difference between 4.55 and 4.65, you visually imply that one value is massive and the other is tiny. It isn't. Length must correspond to the full value range.

**Non-zero axis (truncated axis) distortion:**
- One bar looks 10x taller than another when the true ratio is 1.01x
- Readers intuitively compare lengths — they cannot help it
- This is not a design preference; it is a perceptual contract with the viewer

**Log scale caveat:**
- Log scale is useful for multiplicative data, but destroys the "length equals value" intuition
- If you use a log scale, over-communicate what you're doing — readers won't assume it

**Distinguish zero from null:** Missing data is not the same as zero value. A bar at zero means "the value is known to be zero." A gap or missing bar means "no data." Conflating them corrupts the comparison.
