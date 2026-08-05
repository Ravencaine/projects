---
created: 2026-08-02
source: What Violin Plots Tell You That Boxplots Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, violin-plot, boxplot, kde, distribution, density]
---

# Violin vs Boxplot: Width = Density, Not Raw Counts; Reading Shape

Violin = boxplot + a smoothed picture of where data actually lives. Shows shape, not just a handful of summary numbers.

**Core encoding:** Width at any height = density (how many values are around that spot). Wide = common. Narrow = rare. The violin is mirrored around a central spine.

**Reading the shape:**
- **Wide regions** → lots of values cluster here
- **Thin regions** → not many values here
- **Pinched waist** → a gap in your data
- **Multiple bulges** → multiple groups mixed together (e.g., rush-hour + off-peak pretending to be one distribution)

**Important caveat:** Width shows *density*, not raw counts. Two violins can look similarly wide even if one has far more data points than the other.

**When violins beat boxplots:**
- "Are values in Group A more lopsided than Group B?"
- "Does one group have a long tail of extremes?"
- "Do we have two distinct patterns hiding in one box?"
- A boxplot tells you things are "spread out." A violin tells you *how*.

**When NOT to use violins:**
- Fewer than ~30 points per group — the KDE smoothing invents structure that isn't there. Use strip plot or beeswarm instead.
- Clearly discrete data (ratings 1–5, small integer counts) — violin implies continuity (2.7, 3.4) that doesn't exist. Use bar chart or dot plot.
- Hunting for specific outliers — violins stretch tails rather than marking outliers. Overlay actual points or use boxplot with explicit outlier markers.

**KDE smoothing choice:** Most tools pick sensible defaults. Too smooth = lose real patterns. Too spiky = see noise. The violin is an *estimate* of the distribution, not the raw data itself.
