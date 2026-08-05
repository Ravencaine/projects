---
created: 2026-08-02
source: What Scatter Plots Tell You That Summary Statistics Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, scatter-plot, encoding, color, shape, bubble, cluster, centroid]
---

# Scatter Encoding: Categorical Color/Shape, Continuous Bubble Size, Cluster Centroids vs Separate Fit Lines

When data contains distinct populations, encoding a third variable separates groups and reveals whether the relationship itself changes across categories.

**Encoding categorical variables:**
- **Color** — primary tool; pre-attentive (eye groups automatically before conscious thought). Encode categorical group by color.
- **Shape** — weaker; readers must scan point-by-point. Reserve as accessibility backup (especially for colourblind readers) or when color is already encoding something else.

Beyond coloring: consider whether groups behave differently. Fit **separate trend lines per group** to reveal when the slope changes by category.

**Encoding continuous variables:**
- **Bubble chart** (varying point size) — encodes a third numeric variable. Use sparingly. If bubbles grow too large, they overlap and obscure the position encoding — the very thing that makes scatter plots useful.

**Showing clusters:**
When distinct clusters exist (different cohorts, markets, experimental conditions):

| Claim | Technique |
|-------|-----------|
| "These groups are distinct" | Add **centroid marker** per cluster — immediately reduces cognitive load |
| "These groups behave differently" | Fit and draw **separate fit lines** — a single pooled line can actively mislead |

**Paired data (before vs after):**
Add a diagonal reference line where x = y. Points above = improved; points below = declined. Gives the chart instant visual logic.

**Direct annotation beats legends** — color the high-cost or high-risk cases, add a reference line for the average, name the interesting outliers explicitly rather than leaving readers to hunt for them.
